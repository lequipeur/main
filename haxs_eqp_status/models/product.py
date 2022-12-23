from odoo import models, fields, api, _

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
        for template in self:
            variants = template.env['product.product'].search([
                ('product_tmpl_id.id', '=', template._origin.id),
                ('state', 'not in', ['blocked', 'pto'])
            ])
            for variant in variants: variant.state = template.state

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    state = fields.Selection([
        ('stock', 'In Stock'),
        ('stock_shw', 'In Stock Showroom'),
        ('pto', 'Purchase To Order'),
        ('blocked', 'End Of Life')
    ], string="Status")