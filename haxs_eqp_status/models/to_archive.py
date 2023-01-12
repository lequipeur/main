from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = "product.template"

    to_archive = fields.Boolean(string='To archive')

    def write(self, vals):
        if 'to_archive' in vals:
            self.mapped('product_variant_ids').write({'to_archive': vals.get('to_archive')})
        res = super(ProductTemplate, self).write(vals)
        return res

    @api.constrains('to_archive')
    def _check_permission_to_archive(self):
        test = {
            "key1": 1,
            "key2": 2
        }
        _logger.info(test.keys())
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        if (self.env.ref("haxs_security_groups.purchase_group_manager").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change set a product to 'to archive'"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        return super(ProductTemplate, self.with_context(disable_check=True)).create(values)

class ProductProduct(models.Model):
    _inherit = "product.product"

    to_archive = fields.Boolean(string='To archive')

    @api.constrains("to_archive")
    def _check_permission(self):
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        if (self.env.ref("haxs_security_groups.purchase_group_manager").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change set a product to 'to archive'"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        return super(ProductProduct, self.with_context(disable_check=True)).create(values)

    def is_document_in_progress(self):
        for product in self:
            templates_ids_to_archive = []
            templates_ids_to_keep = []

            nb_doc = self.env["stock.quant"].search_count([
                ("location_id.usage", "in", ["internal", "transit"]),
                ("product_id", "=", product.id),
                ("quantity", "!=", 0.0),
            ])
            nb_doc += self.env["stock.move"].search_count([
                ("product_id", "=", product.id),
                ("state", "not in", ["done", "cancel"]),
                ])
            nb_doc += self.env["stock.move.line"].search_count([
                ("product_id", "=", product.id),
                ("state", "not in", ["done", "cancel"]),
                ])
            
            _logger.info(nb_doc)
            if nb_doc == 0:
                if product.product_tmpl_id.id not in templates_ids_to_archive:
                    templates_ids_to_archive.append(product.product_tmpl_id.id)
                product.action_archive()
            else:
                if product.product_tmpl_id.id not in templates_ids_to_keep:
                    templates_ids_to_keep.append(product.product_tmpl_id.id)
        
        return list(set(templates_ids_to_archive) - set(templates_ids_to_keep))


    def action_cron_to_archive(self, nb_template=0, search_field=False):
        
        # Get all variants to archive 
        args = [('active', '=', True),('to_archive', '=', True)]
        if search_field:
            args.append((search_field, '=', True))
        products = self.env['product.product'].search(args, limit=nb_template)
        
        template_ids = products.is_document_in_progress()
        
        templates = self.env['product.template'].search([
            ('active', '=', True),
            '|',
            ('to_archive', '=', True),
            ('id', 'in', template_ids),
        ])
        for template in templates:
            to_archive = True
            # Check if all variants are set to 'to_archive'
            for prod in template.product_variant_ids:
                to_archive = False if prod.active else to_archive

            # Archive template
            if to_archive:
                template.action_archive()