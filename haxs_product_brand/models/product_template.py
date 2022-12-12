from odoo import fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    brand_id = fields.Many2one(
        "product.brand",
        string = "Brand",
        help = _("Select a brand for this product.")
    )
    