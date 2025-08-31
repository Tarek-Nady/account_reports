# Installation Guide for Account Reports Check Number Extension

## Prerequisites
- Odoo 18.0+ installed
- account_reports module already installed and working
- Access to Odoo addons directory

## Installation Steps

### 1. **Copy Module to Addons Directory**
```bash
# Copy the entire account_reports_check_number folder to your Odoo addons directory
cp -r account_reports_check_number /path/to/odoo/addons/
```

### 2. **Update Addons List in Odoo**
- Go to Apps menu in Odoo
- Click "Update Apps List" button
- Wait for the update to complete

### 3. **Install the Module**
- Search for "Account Reports Check Number Extension" in the Apps menu
- Click "Install" button
- Wait for installation to complete

### 4. **Verify Installation**
- Go to Accounting > Payments
- Create a new payment or edit an existing one
- You should see a "Check Number" field

## Testing the Functionality

### 1. **Add Check Numbers to Payments**
- Create a new payment in Accounting > Payments
- Fill in the required fields (amount, partner, journal, etc.)
- Enter a check number in the "Check Number" field
- Save the payment

### 2. **View in General Ledger**
- Go to Accounting > Reporting > General Ledger
- Set your date range and other filters
- Click "Search" to generate the report
- Expand any account line that has payment-related moves
- You should see the check number displayed below the line name

## Troubleshooting

### **Check Number Not Showing**
- Ensure the payment is posted
- Verify the move line has a payment_id
- Check browser console for JavaScript errors
- Clear browser cache and refresh

### **Module Not Installing**
- Verify Odoo version compatibility (18.0+)
- Check that account_reports module is installed
- Review Odoo logs for error messages
- Ensure proper file permissions

### **Field Not Visible in Payment Form**
- Check if the view inheritance is working
- Verify the account.view_account_payment_form reference exists
- Clear Odoo cache and restart the service

## Uninstallation

To remove the module:
1. Go to Apps menu
2. Find "Account Reports Check Number Extension"
3. Click "Uninstall"
4. Confirm uninstallation

**Note**: Uninstalling will remove the check_number field and all associated data.

## Support

If you encounter issues:
1. Check the Odoo logs for error messages
2. Verify all dependencies are met
3. Test with a fresh Odoo installation
4. Review the module code for any customizations

## Customization

The module is designed to be easily customizable:
- Modify templates in `static/src/components/general_ledger/`
- Adjust styling in the SCSS files
- Extend functionality in the Python models
- Add new features through inheritance

## Performance Considerations

- The module adds a LEFT JOIN to the General Ledger query
- Impact on performance is minimal for most installations
- For large databases, consider adding database indexes on payment_id
- Monitor query performance in production environments
