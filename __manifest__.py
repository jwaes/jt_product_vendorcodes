# -*- coding: utf-8 -*-
{
    'name': "jt_product_vendorcodes",

    'summary': "Product vendor codes",
    'application': True,

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','purchase','jt_mrp_otf'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/vendorcode_views.xml',
        'report/purchase_order_templates.xml',
        'report/report_deliveryslip.xml',
        'report/report_invoice.xml',
    ],
}
