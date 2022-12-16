from odoo import models, fields, _
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type = fields.Selection(
        [('empty', '-'), ('shw', 'Showroom'), ('btob', 'BtoB')],
        copy = False,
        string = 'Sale type',
        default = 'empty',
        tracking = 1
        )
    
    def action_confirm(self):
        # if self.team_id.id != 6:
        #     self.saleType = 'btob'
        if self.sale_type in [False, 'empty']:
            return self.env['ir.actions.act_window']._for_xml_id('haxs_sale_shw_b2b.sale_type_selection_action')
        
            #idem as following
            #return {
            #    'name': 'Type de vente ?',
            #    'type': 'ir.actions.act_window',
            #    'view_mode': 'form',
            #    'res_model': 'saletype.selection.wizard',
            #    'target': 'new'
            #}

        res = super(SaleOrder, self).action_confirm()
        return res
