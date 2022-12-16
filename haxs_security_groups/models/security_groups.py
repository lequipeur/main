from odoo import models, fields

class SecurityGroups(models.Model):
    _name = "security.groups"
    _description = 'Create custom security group'
    
    name = fields.Char(string="name", required=True)