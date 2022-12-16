from odoo import api, models, fields

class SaleTypeSelectionWizard(models.TransientModel):
    _name="sale.type.selection.wizard"
    _description="Sale type selection"

    def saletype_selection(self):
        saleTypeValue = self.env.context.get('saleTypeValue')
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        sale_order.update({'sale_type':saleTypeValue})
        sale_order.action_confirm()