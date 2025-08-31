# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class AccountPayment(models.Model):
    _inherit = 'account.payment'
    
    check_number = fields.Char(
        string='Check Number',
        help='Check number for this payment',
        copy=False,
    )
