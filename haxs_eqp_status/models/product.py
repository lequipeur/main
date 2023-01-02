from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    state = fields.Selection([
        ('stock', 'In Stock'),
        ('stock_shw', 'In Stock Showroom'),
        ('pto', 'Purchase To Order'),
        ('blocked', 'End Of Life')
    ], string="Status")

    # Change variants status if variant not in End of Life or Purchase To Order
    @api.onchange("state")
    def _compute_statusbar(self):
        self._check_permission_status()
        for template in self:
            variants = template.env['product.product'].search([
                ('product_tmpl_id.id', '=', template._origin.id),
                ('state', 'not in', ['blocked', 'pto'])
            ])
            for variant in variants: variant.state = template.state

    def _check_permission_status(self):
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        if (self.env.ref("haxs_security_groups.purchase_group_manager").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change the product status"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        return super(SaleOrderCheck, self).create(values)

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    state = fields.Selection([
        ('stock', 'In Stock'),
        ('stock_shw', 'In Stock Showroom'),
        ('pto', 'Purchase To Order'),
        ('blocked', 'End Of Life')
    ], string="Status")

    @api.onchange("state")
    def _check_permission_status(self):
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        if (self.env.ref("haxs_security_groups.purchase_group_manager").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change the product status"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        return super(SaleOrderCheck, self).create(values)