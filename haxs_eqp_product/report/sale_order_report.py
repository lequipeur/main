from odoo import models, fields, _

class SaleReport(models.Model):
    _inherit = "sale.report"

    supplier_id = fields.Many2one("res.partner", string = "Default Supplier", readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['supplier_id'] = "t.supplier_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            t.supplier_id"""
        return res