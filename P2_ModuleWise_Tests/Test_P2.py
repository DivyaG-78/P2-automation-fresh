# IMPORT ONLY REQUIRED AND REMOVE UNWANTED LIBS
# IMPORT ---- IMPORT BEGIN ----
# ******************** Import Libraries Which are in Use *************************
import pytest as pytest

from conftest import *

from P2_ModuleWise_Tests.POM_ModuleWise._20_Reporting_POM import *





# *********************************************************************************
# IMPORT ---- END -----


# Add Only PORTAL LOGIN and LOGO CHANGES test cases inside block below.
# PORTAL LOGIN ---- BEGIN -----
# ************************* 1. PORTAL LOGIN and LOGO CHANGES Test Cases  *****************************


# Add Only REPORTING test cases inside block below.
# REPORTING ---- BEGIN -----
# ************************* 20. REPORTING Test Cases  *******************************
@pytest.mark.reporting
def test_tc_reporting_001(page, credentials, screenshot_path, delay):
    if Verify_Reporting_is_visible_and_clickable_in_dashboard_items_click_on_Reporting_and_verify_it_is_navigating_to_reporting_panel(page, credentials, delay):
        assert True
    else:
        assert False


@pytest.mark.reporting
def test_tc_reporting_039(page, credentials, delay):
    #
    if Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_SOE(page, credentials, delay):
        assert True
    else:
        assert False


@pytest.mark.reporting
def test_tc_reporting_040(page, credentials, delay):
    if Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_ABE(page, credentials,delay):
        assert True
    else:
        assert False


@pytest.mark.reporting
def test_tc_reporting_041(page, credentials, delay):
    if Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_PTE(page, credentials,delay):
        assert True
    else:
        assert False


@pytest.mark.reporting
def test_tc_reporting_042(page, credentials, delay):
    if Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_Fraude(page, credentials,delay):
        assert True
    else:
        assert False


# @pytest.mark.reporting
# def test_tc_reporting_043(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_vipe(page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_044(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_045(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_ABE(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_046(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_PTE(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_047(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_FraudE(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_048(page, credentials, delay):
#     if Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_vipE(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_085(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_086(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_087(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_088(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_089(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_090(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_091(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_092(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_093(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_094(page, credentials, groups,delay):
#     if Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#             page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_245(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_SOE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_246(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_ABE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_247(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_PTE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_248(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_FRAUDE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_249(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_250(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_250(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_SOE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_251(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_SOE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_252(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_PTE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_253(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_FRAUDE(
#         page, credentials, delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_254(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_VIPE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_256(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_257(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_258(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_259(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_260(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_261(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_262(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_263(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_264(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_265(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_267(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_Alldevices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_268(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_Alldevices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_269(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_Alldevices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_tc_reporting_270(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_Alldevices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_271(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_Alldevices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_272(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_273(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_274(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_275(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_tc_reporting_276(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_278(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_279(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_280(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_281(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_282(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_283(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_284(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_285(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_286(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_287(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
# @pytest.mark.reporting
# def test_TC_Reporting_289(page, credentials, delay):
#     if Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_SOE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_290(page, credentials, delay):
#     if Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_ABE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_291(page, credentials, delay):
#     if Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_PTE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_292(page, credentials, delay):
#     if Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_FRAUDE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_293(page, credentials, delay):
#     if Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_VIPE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_294(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_SOE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_295(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_ABE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_296(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_PTE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_297(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_FRAUDE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.reporting
# def test_TC_Reporting_298(page, credentials, delay):
#     if Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_FRAUDE(
#         page, credentials,delay):
#         assert True
#     else:
#         assert False












# ***********************************************************************************
# REPORTING ---- END -----


# Add Only ACCOUNT cases inside block below.
# ACCOUNT ---- BEGIN -----
# ************************* 21. ACCOUNT Test Cases  ************************************
