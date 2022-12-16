from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class ExtraPriceProduct(models.Model):
    _inherit = 'product.product'
    _description = 'Extra Price'
    
    extra_price = fields.Float(string="Extra price", default=0.0)
    
    @api.depends('price_extra', 'extra_price')
    def _compute_product_price_extra(self, **kwargs):
        for product in self :
            product.price_extra = product.extra_price
    
    @api.constrains("price_extra", "extra_price")
    def _check_permission(self):
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        if (self.env.ref("haxs_security_groups.purchase_group_manager").id not in self.env.user.groups_id.ids):
            raise ValidationError(_("You are not authorized to change the extra price"))

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        return super(ExtraPriceProduct, self.with_context(disable_check=True)).create(values)