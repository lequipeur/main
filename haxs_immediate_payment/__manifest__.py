# -*- coding: utf-8 -*-
{
    'name': "Immediate Payment",

    'summary': """
        Show a warning Popup if immediate payment""",

    'description': """
        Show a warning Popup if immediate payment
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
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/immediat_payment.xml',
    ]
}
