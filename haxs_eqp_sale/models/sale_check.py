from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class SaleOrderCheck(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):
        message = _("You are not authorized to confirm a sale order")
        groups_id = [self.env.ref("haxs_security_groups.sales_group_user").id]
        groups_id.append(self.env.ref("haxs_security_groups.manager_group_manager").id)
        self._check_permission(groups_id, message)
        
        self._check_product("00PAC")
        self._check_delivery_email()
        return super(SaleOrderCheck, self).action_confirm()

    def action_cancel(self):
        group_id = self.env.ref("haxs_security_groups.sales_group_manager").id
        message = _("You are not authorized to cancel a sale order")
        self._check_permission(group_id, message)
        return super(SaleOrderCheck, self).action_cancel()
    
    def _check_product(self, product_name):
        for sale in self:
            if sum(1 for product in sale.order_line if product.product_id.default_code == product_name) > 0 :
                raise ValidationError(_("Please remove the following product : ") + product_name)
            
    def _check_delivery_email(self):
        for sale in self:
            if not sale.partner_shipping_id.email :
                raise ValidationError(_("Please provide a delivery email."))

    def _check_permission(self, groups_id, message):
        # for the default value on create
        if self.env.context.get("disable_check", False):
            return True
        is_allowed = False
        for group_id in groups_id:
            if group_id in self.env.user.groups_id.ids:
                is_allowed = True
        if not is_allowed:
            raise ValidationError(message)

    # on create just call the super with the context to disable the stage change, to allow it as "default" value
    @api.model_create_multi
    def create(self, values):
        groups_id = [self.env.ref("haxs_security_groups.sales_group_user").id]
        message = _("You are not authorized to create a sale order")
        self._check_permission(groups_id, message)
        return super(SaleOrderCheck, self).create(values)