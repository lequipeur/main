from odoo import models, fields, api, _
import datetime
import statistics
from statistics import mode

class ProductEQP(models.Model):
    _inherit = "product.template"

    supplier_id = fields.Many2one("res.partner", string = "Default Supplier", compute = "_get_default_supplier", store=True)
    
    # Get default supplier
    # Check for most frequent supplier in the active pricelist
    # If equal get smaller partner id
    @api.depends("seller_ids.write_date")
    def _get_default_supplier(self):
        now = fields.Date.context_today(self)
        for prod in self:
            seller = prod.env["product.supplierinfo"].search([
                "&", ("product_tmpl_id", "=", prod.id),
                "&", "|", ("date_start", "=", False), ("date_start", "<=", now),
                "|", ("date_end", "=", False), ("date_end", ">=", now)
            ])
            seller_list = []
            for sel in seller:
                seller_list.append(sel.partner_id.id)

            supplier_id = ProductEQP.most_frequent(seller_list)

            if supplier_id != False:
                prod.supplier_id = supplier_id

    # Return most frequent element in list
    def most_frequent(List):
        return mode(List) if len(List) > 0 else False
    
    # Override completly the function to be able to have a default_code for template
    def _compute_default_code(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.default_code = template.product_variant_ids.default_code
        # for template in (self - unique_variants):
        #     template.default_code = False