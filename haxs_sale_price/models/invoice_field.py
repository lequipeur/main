from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    amount_already_invoiced = fields.Float(string="Already invoiced", default=0.0, compute="on_update", store=True)
    amount_to_invoice = fields.Float(string="To invoice", default=0.0, compute="on_update", store=True)
    amount_waiting_delivery = fields.Float(string="Waiting delivery", default=0.0, compute="on_update", store=True)

    @api.depends("invoice_ids", "order_line.qty_delivered", "state")
    def on_update(self):
        for sale in self:
            amount_already_invoiced = amount_to_invoice = amount_waiting_delivery = 0
            if sale.state not in ['draft', 'sent', 'cancel']:
                for line in sale.order_line:
                    price_unit = line.price_subtotal / line.product_uom_qty

                    amount_already_invoiced += line.qty_invoiced * price_unit
                    if line.product_id.invoice_policy == 'delivery':
                        amount_waiting_delivery += (line.product_uom_qty - line.qty_delivered) * price_unit
                        amount_to_invoice += (line.qty_delivered - line.qty_invoiced) * price_unit
                    elif line.product_id.invoice_policy == 'order':
                        amount_to_invoice += (line.product_uom_qty - line.qty_invoiced) * price_unit
                
            sale.amount_already_invoiced = amount_already_invoiced
            sale.amount_to_invoice = amount_to_invoice
            sale.amount_waiting_delivery = amount_waiting_delivery
