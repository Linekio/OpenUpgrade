from openupgradelib import openupgrade

tofix = [
    (
        "account_tax_report_line_1a_telecom_service_tag",
        "account_tax_report_line_1a_telecom_service",
    ),
    (
        "account_tax_report_line_1a_other_sales_balance",
        "account_tax_report_line_1a_other_sales",
    ),
    (
        "account_tax_report_line_1a_app_goods_non_bus_tag",
        "account_tax_report_line_1a_app_goods_non_bus",
    ),
    (
        "account_tax_report_line_1a_non_bus_gs_tag",
        "account_tax_report_line_1a_non_bus_gs",
    ),
    (
        "account_tax_report_line_1b_1_intra_community_goods_pi_vat_tag",
        "account_tax_report_line_1b_1_intra_community_goods_pi_vat",
    ),
    ("account_tax_report_line_1b_2_export_tag", "account_tax_report_line_1b_2_export"),
    (
        "account_tax_report_line_1b_3_other_exemptions_art_43_tag",
        "account_tax_report_line_1b_3_other_exemptions_art_43",
    ),
    (
        "account_tax_report_line_1b_4_other_exemptions_art_44_et_56quater_tag",
        "account_tax_report_line_1b_4_other_exemptions_art_44_et_56quater",
    ),
    (
        "account_tax_report_line_1b_5_manufactured_tobacco_vat_collected_tag",
        "account_tax_report_line_1b_5_manufactured_tobacco_vat_collected",
    ),
    (
        "account_tax_report_line_1b_8_supplies_carried_out_domestic_tag",
        "account_tax_report_line_1b_8_supplies_carried_out_domestic",
    ),
    (
        "account_tax_report_line_1b_9_supplies_carried_out_cross_border_tag",
        "account_tax_report_line_1b_9_supplies_carried_out_cross_border",
    ),
    (
        "account_tax_report_line_1b_6_a_subsequent_to_intra_community_tag",
        "account_tax_report_line_1b_6_a_subsequent_to_intra_community",
    ),
    (
        "account_tax_report_line_1b_6_b1_non_exempt_customer_vat_tag",
        "account_tax_report_line_1b_6_b1_non_exempt_customer_vat",
    ),
    (
        "account_tax_report_line_1b_6_b2_exempt_ms_customer_tag",
        "account_tax_report_line_1b_6_b2_exempt_ms_customer",
    ),
    (
        "account_tax_report_line_1b_6_c_supplies_scope_special_arrangement_tag",
        "account_tax_report_line_1b_6_c_supplies_scope_special_arrangement",
    ),
    (
        "account_tax_report_line_1b_6_d_supplies_other_referred_tag",
        "account_tax_report_line_1b_6_d_supplies_other_referred",
    ),
    (
        "account_tax_report_line_1b_7_inland_supplies_for_customer_tag",
        "account_tax_report_line_1b_7_inland_supplies_for_customer",
    ),
    (
        "account_tax_report_line_1c_taxable_turnover_balance",
        "account_tax_report_line_1c_taxable_turnover",
    ),
    ("account_tax_report_line_2a_base_17_tag", "account_tax_report_line_2a_base_17"),
    ("account_tax_report_line_2a_base_16_tag", "account_tax_report_line_2a_base_16"),
    ("account_tax_report_line_2a_base_14_tag", "account_tax_report_line_2a_base_14"),
    ("account_tax_report_line_2a_base_13_tag", "account_tax_report_line_2a_base_13"),
    ("account_tax_report_line_2a_base_8_tag", "account_tax_report_line_2a_base_8"),
    ("account_tax_report_line_2a_base_7_tag", "account_tax_report_line_2a_base_7"),
    ("account_tax_report_line_2a_base_3_tag", "account_tax_report_line_2a_base_3"),
    ("account_tax_report_line_2a_base_0_tag", "account_tax_report_line_2a_base_0"),
    ("account_tax_report_line_2a_tax_17_tag", "account_tax_report_line_2a_tax_17"),
    ("account_tax_report_line_2a_tax_16_tag", "account_tax_report_line_2a_tax_16"),
    ("account_tax_report_line_2a_tax_14_tag", "account_tax_report_line_2a_tax_14"),
    ("account_tax_report_line_2a_tax_13_tag", "account_tax_report_line_2a_tax_13"),
    ("account_tax_report_line_2a_tax_8_tag", "account_tax_report_line_2a_tax_8"),
    ("account_tax_report_line_2a_tax_7_tag", "account_tax_report_line_2a_tax_7"),
    ("account_tax_report_line_2a_tax_3_tag", "account_tax_report_line_2a_tax_3"),
    ("account_tax_report_line_2b_base_17_tag", "account_tax_report_line_2b_base_17"),
    ("account_tax_report_line_2b_base_16_tag", "account_tax_report_line_2b_base_16"),
    ("account_tax_report_line_2b_base_14_tag", "account_tax_report_line_2b_base_14"),
    ("account_tax_report_line_2b_base_13_tag", "account_tax_report_line_2b_base_13"),
    ("account_tax_report_line_2b_base_8_tag", "account_tax_report_line_2b_base_8"),
    ("account_tax_report_line_2b_base_7_tag", "account_tax_report_line_2b_base_7"),
    ("account_tax_report_line_2b_base_3_tag", "account_tax_report_line_2b_base_3"),
    (
        "account_tax_report_line_2b_base_exempt_tag",
        "account_tax_report_line_2b_base_exempt",
    ),
    (
        "account_tax_report_line_2b_manufactured_tobacco_tag",
        "account_tax_report_line_2b_manufactured_tobacco",
    ),
    ("account_tax_report_line_2b_tax_17_tag", "account_tax_report_line_2b_tax_17"),
    ("account_tax_report_line_2b_tax_16_tag", "account_tax_report_line_2b_tax_16"),
    ("account_tax_report_line_2b_tax_14_tag", "account_tax_report_line_2b_tax_14"),
    ("account_tax_report_line_2b_tax_13_tag", "account_tax_report_line_2b_tax_13"),
    ("account_tax_report_line_2b_tax_8_tag", "account_tax_report_line_2b_tax_8"),
    ("account_tax_report_line_2b_tax_7_tag", "account_tax_report_line_2b_tax_7"),
    ("account_tax_report_line_2b_tax_3_tag", "account_tax_report_line_2b_tax_3"),
    (
        "account_tax_report_line_2c_acquisitions_triangular_transactions_base_tag",
        "account_tax_report_line_2c_acquisitions_triangular_transactions_base",
    ),
    (
        "account_tax_report_line_2d_1_base_17_tag",
        "account_tax_report_line_2d_1_base_17",
    ),
    (
        "account_tax_report_line_2d_1_base_16_tag",
        "account_tax_report_line_2d_1_base_16",
    ),
    (
        "account_tax_report_line_2d_1_base_14_tag",
        "account_tax_report_line_2d_1_base_14",
    ),
    (
        "account_tax_report_line_2d_1_base_13_tag",
        "account_tax_report_line_2d_1_base_13",
    ),
    ("account_tax_report_line_2d_1_base_8_tag", "account_tax_report_line_2d_1_base_8"),
    ("account_tax_report_line_2d_1_base_7_tag", "account_tax_report_line_2d_1_base_7"),
    ("account_tax_report_line_2d_1_base_3_tag", "account_tax_report_line_2d_1_base_3"),
    (
        "account_tax_report_line_2d_1_base_exempt_tag",
        "account_tax_report_line_2d_1_base_exempt",
    ),
    (
        "account_tax_report_line_2d_1_manufactured_tobacco_tag",
        "account_tax_report_line_2d_1_manufactured_tobacco",
    ),
    (
        "account_tax_report_line_2d_2_base_17_tag",
        "account_tax_report_line_2d_2_base_17",
    ),
    (
        "account_tax_report_line_2d_2_base_16_tag",
        "account_tax_report_line_2d_2_base_16",
    ),
    (
        "account_tax_report_line_2d_2_base_14_tag",
        "account_tax_report_line_2d_2_base_14",
    ),
    (
        "account_tax_report_line_2d_2_base_13_tag",
        "account_tax_report_line_2d_2_base_13",
    ),
    ("account_tax_report_line_2d_2_base_8_tag", "account_tax_report_line_2d_2_base_8"),
    ("account_tax_report_line_2d_2_base_7_tag", "account_tax_report_line_2d_2_base_7"),
    ("account_tax_report_line_2d_2_base_3_tag", "account_tax_report_line_2d_2_base_3"),
    (
        "account_tax_report_line_2d_2_base_exempt_tag",
        "account_tax_report_line_2d_2_base_exempt",
    ),
    ("account_tax_report_line_2d_1_tax_17_tag", "account_tax_report_line_2d_1_tax_17"),
    ("account_tax_report_line_2d_1_tax_16_tag", "account_tax_report_line_2d_1_tax_16"),
    ("account_tax_report_line_2d_1_tax_14_tag", "account_tax_report_line_2d_1_tax_14"),
    ("account_tax_report_line_2d_1_tax_13_tag", "account_tax_report_line_2d_1_tax_13"),
    ("account_tax_report_line_2d_1_tax_8_tag", "account_tax_report_line_2d_1_tax_8"),
    ("account_tax_report_line_2d_1_tax_7_tag", "account_tax_report_line_2d_1_tax_7"),
    ("account_tax_report_line_2d_1_tax_3_tag", "account_tax_report_line_2d_1_tax_3"),
    ("account_tax_report_line_2d_2_tax_17_tag", "account_tax_report_line_2d_2_tax_17"),
    ("account_tax_report_line_2d_2_tax_16_tag", "account_tax_report_line_2d_2_tax_16"),
    ("account_tax_report_line_2d_2_tax_14_tag", "account_tax_report_line_2d_2_tax_14"),
    ("account_tax_report_line_2d_2_tax_13_tag", "account_tax_report_line_2d_2_tax_13"),
    ("account_tax_report_line_2d_2_tax_8_tag", "account_tax_report_line_2d_2_tax_8"),
    ("account_tax_report_line_2d_2_tax_7_tag", "account_tax_report_line_2d_2_tax_7"),
    ("account_tax_report_line_2d_2_tax_3_tag", "account_tax_report_line_2d_2_tax_3"),
    (
        "account_tax_report_line_2e_1_a_base_17_tag",
        "account_tax_report_line_2e_1_a_base_17",
    ),
    (
        "account_tax_report_line_2e_1_a_base_16_tag",
        "account_tax_report_line_2e_1_a_base_16",
    ),
    (
        "account_tax_report_line_2e_1_a_base_14_tag",
        "account_tax_report_line_2e_1_a_base_14",
    ),
    (
        "account_tax_report_line_2e_1_a_base_13_tag",
        "account_tax_report_line_2e_1_a_base_13",
    ),
    (
        "account_tax_report_line_2e_1_a_base_8_tag",
        "account_tax_report_line_2e_1_a_base_8",
    ),
    (
        "account_tax_report_line_2e_1_a_base_7_tag",
        "account_tax_report_line_2e_1_a_base_7",
    ),
    (
        "account_tax_report_line_2e_1_a_base_3_tag",
        "account_tax_report_line_2e_1_a_base_3",
    ),
    (
        "account_tax_report_line_2e_1_b_exempt_tag",
        "account_tax_report_line_2e_1_b_exempt",
    ),
    (
        "account_tax_report_line_2e_2_base_17_tag",
        "account_tax_report_line_2e_2_base_17",
    ),
    (
        "account_tax_report_line_2e_2_base_16_tag",
        "account_tax_report_line_2e_2_base_16",
    ),
    (
        "account_tax_report_line_2e_2_base_14_tag",
        "account_tax_report_line_2e_2_base_14",
    ),
    (
        "account_tax_report_line_2e_2_base_13_tag",
        "account_tax_report_line_2e_2_base_13",
    ),
    ("account_tax_report_line_2e_2_base_8_tag", "account_tax_report_line_2e_2_base_8"),
    ("account_tax_report_line_2e_2_base_7_tag", "account_tax_report_line_2e_2_base_7"),
    ("account_tax_report_line_2e_2_base_3_tag", "account_tax_report_line_2e_2_base_3"),
    ("account_tax_report_line_2e_2_exempt_tag", "account_tax_report_line_2e_2_exempt"),
    (
        "account_tax_report_line_2e_3_base_17_tag",
        "account_tax_report_line_2e_3_base_17",
    ),
    (
        "account_tax_report_line_2e_3_base_16_tag",
        "account_tax_report_line_2e_3_base_16",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_17_tag",
        "account_tax_report_line_2e_1_a_tax_17",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_16_tag",
        "account_tax_report_line_2e_1_a_tax_16",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_14_tag",
        "account_tax_report_line_2e_1_a_tax_14",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_13_tag",
        "account_tax_report_line_2e_1_a_tax_13",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_8_tag",
        "account_tax_report_line_2e_1_a_tax_8",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_7_tag",
        "account_tax_report_line_2e_1_a_tax_7",
    ),
    (
        "account_tax_report_line_2e_1_a_tax_3_tag",
        "account_tax_report_line_2e_1_a_tax_3",
    ),
    ("account_tax_report_line_2e_2_tax_17_tag", "account_tax_report_line_2e_2_tax_17"),
    ("account_tax_report_line_2e_2_tax_16_tag", "account_tax_report_line_2e_2_tax_16"),
    ("account_tax_report_line_2e_2_tax_14_tag", "account_tax_report_line_2e_2_tax_14"),
    ("account_tax_report_line_2e_2_tax_13_tag", "account_tax_report_line_2e_2_tax_13"),
    ("account_tax_report_line_2e_2_tax_8_tag", "account_tax_report_line_2e_2_tax_8"),
    ("account_tax_report_line_2e_2_tax_7_tag", "account_tax_report_line_2e_2_tax_7"),
    ("account_tax_report_line_2e_2_tax_3_tag", "account_tax_report_line_2e_2_tax_3"),
    ("account_tax_report_line_2e_3_tax_17_tag", "account_tax_report_line_2e_3_tax_17"),
    ("account_tax_report_line_2e_3_tax_16_tag", "account_tax_report_line_2e_3_tax_16"),
    (
        "account_tax_report_line_2f_supply_goods_base_17_tag",
        "account_tax_report_line_2f_supply_goods_base_17",
    ),
    (
        "account_tax_report_line_2f_supply_goods_base_8_tag",
        "account_tax_report_line_2f_supply_goods_base_8",
    ),
    (
        "account_tax_report_line_2f_supply_goods_base_7_tag",
        "account_tax_report_line_2f_supply_goods_base_7",
    ),
    (
        "account_tax_report_line_2f_supply_goods_tax_17_tag",
        "account_tax_report_line_2f_supply_goods_tax_17",
    ),
    (
        "account_tax_report_line_2f_supply_goods_tax_8_tag",
        "account_tax_report_line_2f_supply_goods_tax_8",
    ),
    (
        "account_tax_report_line_2f_supply_goods_tax_7_tag",
        "account_tax_report_line_2f_supply_goods_tax_7",
    ),
    (
        "account_tax_report_line_2g_special_arrangement_tag",
        "account_tax_report_line_2g_special_arrangement",
    ),
    (
        "account_tax_report_line_2h_total_tax_due_balance",
        "account_tax_report_line_2h_total_tax_due",
    ),
    (
        "account_tax_report_line_3a_1_invoiced_by_other_taxable_person_tag",
        "account_tax_report_line_3a_1_invoiced_by_other_taxable_person",
    ),
    (
        "account_tax_report_line_3a_2_due_respect_intra_comm_goods_tag",
        "account_tax_report_line_3a_2_due_respect_intra_comm_goods",
    ),
    (
        "account_tax_report_line_3a_3_due_paid_respect_importation_goods_tag",
        "account_tax_report_line_3a_3_due_paid_respect_importation_goods",
    ),
    (
        "account_tax_report_line_3a_4_due_respect_application_goods_tag",
        "account_tax_report_line_3a_4_due_respect_application_goods",
    ),
    (
        "account_tax_report_line_3a_5_due_under_reverse_charge_tag",
        "account_tax_report_line_3a_5_due_under_reverse_charge",
    ),
    (
        "account_tax_report_line_3a_6_paid_joint_several_guarantee_tag",
        "account_tax_report_line_3a_6_paid_joint_several_guarantee",
    ),
    (
        "account_tax_report_line_3a_7_adjusted_tax_special_arrangement_tag",
        "account_tax_report_line_3a_7_adjusted_tax_special_arrangement",
    ),
    (
        "account_tax_report_line_3b1_rel_trans_tag",
        "account_tax_report_line_3b1_rel_trans",
    ),
    (
        "account_tax_report_line_3b2_ded_prop_tag",
        "account_tax_report_line_3b2_ded_prop",
    ),
    (
        "account_tax_report_line_3b2_input_tax_margin_tag",
        "account_tax_report_line_3b2_input_tax_margin",
    ),
    (
        "account_tax_report_line_4a_total_tax_due_balance",
        "account_tax_report_line_4a_total_tax_due",
    ),
]


def fix_expression_xmlids(cr):
    for xmlid, parent_xml_id in tofix:
        cr.execute(
            """
            SELECT id
            FROM account_report_expression
            WHERE label = 'balance' AND report_line_id IN (SELECT res_id FROM ir_model_data WHERE module = 'l10n_lu' AND name = %s)
            LIMIT 1
            """,
            (parent_xml_id,),
        )
        for (res_id,) in cr.fetchall():
            openupgrade.add_xmlid(
                cr, "l10n_lu", xmlid, "account.report.expression", res_id
            )


def migrate(cr, version):
    fix_expression_xmlids(cr)
