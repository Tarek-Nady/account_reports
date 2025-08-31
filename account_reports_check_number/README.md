# Account Reports Check Number Extension

This module extends the Odoo 18 Accounting Reports module to add a `check_number` field to payments and display it in the General Ledger report.

## Features

- Adds a `check_number` field to the `account.payment` model
- Displays the check number in the General Ledger report when a move line is related to a payment
- Integrates seamlessly with the existing account_reports module

## Installation

1. Place this module in your Odoo addons directory
2. Update the addons list in Odoo
3. Install the module from the Apps menu

## Usage

1. **Adding Check Numbers to Payments:**
   - Go to Accounting > Payments
   - Create or edit a payment
   - You will see a new "Check Number" field where you can enter the check number

2. **Viewing Check Numbers in General Ledger:**
   - Go to Accounting > Reporting > General Ledger
   - When you expand account lines, you will see the check number displayed for move lines related to payments
   - The check number appears below the line name with a "Check:" prefix

## Technical Details

- **Model Extension:** Extends `account.payment` to add the `check_number` field
- **Report Extension:** Extends the General Ledger report handler to include check_number data
- **UI Extension:** Custom template to display check numbers in the report
- **Database Query:** Modified SQL query to join with account_payment table and fetch check_number

## Dependencies

- Odoo 18.0+
- account_reports module

## Files Structure

```
account_reports_check_number/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── account_payment.py
│   └── account_general_ledger.py
├── views/
│   └── account_payment_views.xml
├── data/
│   └── general_ledger_check_number.xml
└── static/
    └── src/
        ├── assets.xml
        └── components/
            └── general_ledger/
                ├── line_name.js
                ├── line_name.xml
                └── line_name.scss
```

## Customization

To modify the display of check numbers:
- Edit `static/src/components/general_ledger/line_name.xml` for template changes
- Edit `static/src/components/general_ledger/line_name.scss` for styling changes
- Edit `static/src/components/general_ledger/line_name.js` for JavaScript functionality

## Support

This module is designed to work with Odoo 18.0+ and the core account_reports module.
