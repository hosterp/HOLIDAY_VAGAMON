# -*- coding: utf-8 -*-
{
    'name': 'HRMS Extend',
    'version': '1.0.0',
    'author': 'Hiworth Solutions Pvt Ltd',
    'category': 'Point Of Sale',
    'website': 'http://www.hiworthsolutions.com',
    'depends': ['hiworth_accounting','board_frontdesk','hotel_housekeeping','purchase','google_calendar','hiworth_delete_purchase_stock_move'],
    'data': [
        'security/hide_sale_pos.xml',
        'security/hotel_security.xml',

        'report/custom_external_layout.xml',
        'report/restaurant_bill.xml',
        'report/invoice_report2.xml',
        'report/checkin_and_checkout_list.xml',
        'report/outstanding_report.xml',
        'report/night_audit.xml',
        'wizard/maintenance_wizard_views.xml',
        'views/reservation_filters.xml',
        'views/res_partner_view.xml',
        'views/reservation_new_features.xml',
        'views/bill2.xml',
        'views/reservation_email.xml',


        'views/bill_no_sequence.xml',
        'views/account_entry_sequence.xml',
        'views/reservation_email.xml',
        'views/default_accounts.xml',
        'views/report_invoice2.xml',
        'views/report_restaurant_cash_credit.xml',
        'views/restaurant_sl_no_sequnece.xml',
        'views/report_restaurant_menu_card.xml',
        'views/hiworth_customer_reservation.xml',
        'views/service_bill_seuence.xml',
        'views/service_invoice_bill.xml',
        'views/invoice_email_template.xml',
        'report/reminder_report.xml',
        'report/check_in_out_report.xml',
        'report/daily_invoice_report.xml',
        'views/agency.xml',
        'views/room_summary_inherit.xml',
        'report/check_in_out_summary.xml',
        'views/calendar.xml',
        'security/ir.model.access.csv',
        'views/house_keeping.xml',
        'views/template_rate_details.xml',
        'report/style.xml',
        'report/invoice_report.xml',
        'views/meal_plan.xml',
        'views/tax_mapping.xml',
        'views/voucher_view.xml',
        'report/reservation_customer_report.xml',
        'report/occupancy_report.xml',
        'report/kot_report.xml',
        'report/table_order_report.xml',
        'views/room_status.xml',
        'views/kitchen_order_ticket_print.xml',
        'views/wizard_selection.xml',
        'views/inventory.xml',
        'report/purchase_register_report.xml',
        'report/room_rent_report.xml',
        'data/data_sequence.xml',
        'wizard/report_wizards.xml',
        'wizard/product_usage_report.xml',
        'views/collection_and_expenses_views.xml',
    ],
    'qweb': ['static/src/xml/room_summary_template.xml'],
    'installable': True,
    'auto_install': False,
}
