# -*- coding: utf-8 -*-
{
    'name': "Sale Price",

    'summary': """
        Manage Sale price""",

    'description': """
        Add permission to price update
        Manage variants with direct Extra Price
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
    'depends': ['sale', 'product','haxs_security_groups'],

    # always loaded
    'data': [
        'views/extra_price.xml',
        'views/global_discount.xml',
        'views/invoice_field.xml',
    ]
}
