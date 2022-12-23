from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    global_discount = fields.Float(string="Global Discount", default=0.0)

    @api.onchange("global_discount")
    def apply_discount(self):
        for sale in self:
            for line in sale.order_line:
                line.discount = sale.global_discount * 100