# -*- coding: utf-8 -*-
{
    'name': "Chatter Position",

    'summary': """
        Move chatter to bottom""",

    'description': """
        Move chatter to bottom
    """,

    'author': "haxs",
    'website': "https://www.haxs.fr",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'views/assets.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'haxs_chatter_position/static/src/scss/chatter_position.scss',
        ],
    }
}
