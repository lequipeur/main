# -*- coding: utf-8 -*-
{
    'name': "Security Groups",

    'summary': """
        Create specific security groups""",

    'description': """
        Create specific security groups
    """,

    'author': "haxs",
    'website': "https://www.haxs.fr",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['product'],

    # always loaded
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv'
    ]
}
