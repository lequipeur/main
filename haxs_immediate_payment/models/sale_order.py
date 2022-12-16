from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    is_immediat_payment = fields.Boolean(string="Immediate payment?", compute="_compute_is_immediate_payment")

    def _compute_is_immediate_payment(self):
        for sale in self:
            sale.is_immediat_payment = sale.payment_term_id.id == 1
    