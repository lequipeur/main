from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductTemplateActive(models.Model):
    _inherit = 'product.template'
    
    def action_archive(self):
        groups_id = [self.env.ref("haxs_security_groups.purchase_group_manager").id]
        message = _("You are not authorized to archive a product")
        self._check_permission_active(groups_id, message)

        res = super(ProductTemplateActive, self).action_archive()
        return res

    def action_unarchive(self):
        groups_id = [self.env.ref("haxs_security_groups.purchase_group_manager").id]
        message = _("You are not authorized to unarchive a product")
        self._check_permission_active(groups_id, message)

        res = super(ProductTemplateActive, self).action_unarchive()
        return res
    
    def _check_permission_active(self, groups_id, message):
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
        return super(ProductTemplateActive, self.with_context(disable_check=True)).create(values)

class ProductProductActive(models.Model):
    _inherit = 'product.product'
    
    def action_archive(self):
        groups_id = [self.env.ref("haxs_security_groups.purchase_group_manager").id]
        message = _("You are not authorized to archive a product")
        self._check_permission_active(groups_id, message)

        res = super(ProductProductActive, self).action_archive()
        return res

    def action_unarchive(self):
        groups_id = [self.env.ref("haxs_security_groups.purchase_group_manager").id]
        message = _("You are not authorized to unarchive a product")
        self._check_permission_active(groups_id, message)

        res = super(ProductProductActive, self).action_unarchive()
        return res
    
    def _check_permission_active(self, groups_id, message):
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
        return super(ProductProductActive, self.with_context(disable_check=True)).create(values)