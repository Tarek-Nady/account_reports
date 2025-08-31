# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests.common import TransactionCase

class TestCheckNumberExtension(TransactionCase):
    
    def setUp(self):
        super().setUp()
        self.payment_model = self.env['account.payment']
        self.company = self.env.company
        
    def test_check_number_field_exists(self):
        """Test that the check_number field exists on account.payment model"""
        payment_fields = self.payment_model._fields
        self.assertIn('check_number', payment_fields)
        
    def test_check_number_field_type(self):
        """Test that the check_number field is of type Char"""
        payment_fields = self.payment_model._fields
        self.assertEqual(payment_fields['check_number'].type, 'char')
        
    def test_check_number_field_string(self):
        """Test that the check_number field has correct string label"""
        payment_fields = self.payment_model._fields
        self.assertEqual(payment_fields['check_number'].string, 'Check Number')
