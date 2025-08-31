# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Account Reports Check Number Extension',
    'summary': 'Add check_number field to payments and display in General Ledger',
    'category': 'Accounting/Accounting',
    'version': '18.0.1.0.0',
    'depends': ['account_reports'],
    'data': [
        'views/account_payment_views.xml',
        'data/general_ledger_check_number.xml',
    ],
    'assets':{
        'web.assets_backend':[
            'account_reports_check_number/static/src/components/general_ledger/line_name.js',
            'account_reports_check_number/static/src/components/general_ledger/line_name.xml',
            'account_reports_check_number/static/src/components/general_ledger/line_name.scss',
        ]
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
