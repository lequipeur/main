# -*- coding: utf-8 -*-
{
    'name': "Sale Type shw/b2b",

    'summary': """
        Show a popup to select type of sale (shw or b2b) at confirm""",

    'description': """
        Show a popup to select type of sale (shw or b2b) at confirm
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
    'depends': ['base','product','stock', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/dialog_selection_wizard_view.xml',
        'views/sale_order.xml',
        'report/sale_order_sale_type_report.xml'
    ]
}
