# -*- coding: utf-8 -*-
{
    'name': "Eqp Sale",

    'summary': """
        EQP config for sale module""",

    'description': """
        EQP check and config for sale module
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
    'depends': ['sale','sale_stock', 'haxs_security_groups'],

    # always loaded
    'data': [
        'views/sale_order_change.xml',
    ]
}
