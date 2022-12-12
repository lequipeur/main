from odoo import fields, models, _

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brand'

    name = fields.Char(_("Brand"), required=True)
    logo = fields.Binary(_("Logo"))
    website = fields.Char(_("Website"))
    description = fields.Text(_("Description"), translate=True)
