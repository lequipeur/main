from odoo import models, fields, _

class SaleReport(models.Model):
    _inherit = "sale.report"

    sale_type = fields.Selection(
        [('empty', '-'), ('shw', 'Showroom'), ('btob', 'BtoB')],
        string = 'Sale type',
        readonly = True
        )

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['sale_type'] = "s.sale_type"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.sale_type"""
        return res

    # def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
    #     fields['saleType'] = ", s.saleType as saleType"
    #     groupby += ', s.saleType'
    #     return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)