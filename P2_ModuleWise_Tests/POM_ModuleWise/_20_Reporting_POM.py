
from utilities import *
from conftest import *

def Verify_Reporting_is_visible_and_clickable_in_dashboard_items_click_on_Reporting_and_verify_it_is_navigating_to_reporting_panel(page, credentials, delay):
    try:
        status = []
        logger.info('Verify_Reporting_is_visible_and_clickable_in_dashboard_items_click_on_Reporting_and_verify_it_is_navigating_to_reporting_panel')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        #click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        #verifying reporting panel heading
        logger.info("verifying reporting panel is opened successfully.")
        if page.locator("div.panel-heading-container p",has_text="Reporting").is_visible():
            page.wait_for_timeout(delay)
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "Verify_Reporting_is_visible_and_clickable_in_dashboard_items", screenshot_path)
            return False
        else:
            return True

    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_Reporting_is_visible_and_clickable_in_dashboard_items')
        save_screenshot(page, "test_tc_reporting_07", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_SOE(page, credentials, delay):

    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[3]["name"], delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_039", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_039", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_ABE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_ABE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[0]["name"], delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_040", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_ABE')
        save_screenshot(page, "test_tc_Reporting_040", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_PTE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_PTE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_041", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_PTE')
        save_screenshot(page, "test_tc_Reporting_041", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_Fraude(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_Fraude')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_042", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_Fraude')
        save_screenshot(page, "test_tc_Reporting_042", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_vipe(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_vipe')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_043", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_with_group_selected_as_vipe')
        save_screenshot(page, "test_tc_Reporting_043", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_044", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_044", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_ABE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_045", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_045", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_PTE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_046", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_046", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_FraudE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_047", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_047", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_vipE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on report dropdown")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("selecting number of enrollments")
        page.locator("#reportField1Menu").select_option(label="number of enrollments")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuC").click()
        page.wait_for_timeout(delay)
        logger.info("selecting  zone")
        page.locator("#reportField2MenuC").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        expected_text = "number of enrollments by zone"
        heading = page.locator(".panel-heading", has_text="enrollments").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_048", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_048", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
        page, credentials, delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES

        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_085", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_085", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_086", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_086", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_087", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_087", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_088", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_088", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)



def Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
        page, credentials, delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_089", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(f'exception: Verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_089", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_090", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_090", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
        page, credentials, delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_091", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_091", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
        page, credentials, delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page, ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_092", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_092", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_093", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_093", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    status = []
    try:

        logger.info(
            'Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # SELECT REPORT
        logger.info("clicking on report dropdown and selecting a number of zones")
        page.locator("#reportField1Menu").select_option(label="number of zones")
        page.wait_for_timeout(delay)

        # SELECT BY = enrollment
        logger.info("clicking on by dropdown and selecting  enrollment option")
        page.locator("#reportField2MenuB").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # SET DATE RANGE (USE CORRECT PARAMS)
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)

        # SELECT GROUPS + ZONES
        logger.info("selecting groups and zones")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)
        # VALIDATION
        expected_text = "number of zones by enrollment"
        heading = page.locator(".panel-heading", has_text="zones").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_094", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_zones_by_enrollment_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_094", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_SOE(page, credentials,delay):
    
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_245", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_245", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_ABE(page, credentials,delay):
   
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_ABE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=TIMEOUT_LONG)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_246", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_ABE')
        save_screenshot(page, "test_tc_Reporting_246", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_PTE(page, credentials,delay):
   
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_PTE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_247", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_PTE')
        save_screenshot(page, "test_tc_Reporting_247", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_FRAUDE(page, credentials,delay):
  
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_FRAUDE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_248", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_FRAUDE')
        save_screenshot(page, "test_tc_Reporting_248", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE(page, credentials,delay):
    
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_249", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_249", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_SOE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_250", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_250", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_ABE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_251", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_251", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_PTE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_PTE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_252", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_PTE')
        save_screenshot(page, "test_tc_Reporting_252", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_FRAUDE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_FRAUDE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_253", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_FRAUDE')
        save_screenshot(page, "test_tc_Reporting_253", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_VIPE(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="enrollment")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date,delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page, ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by enrollment"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_254", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_enrollment_with_daterange_from_jsonfile_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_254", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_256.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_256", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_257.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_257", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_258.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_258", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_259.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_259", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_260.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hourofday_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_260", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_261.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_261", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_262.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_262", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_263.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_263", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_264.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_264", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)



def Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_265.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_265", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_Alldevices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_Alldevices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_267.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_Alldevices')
        save_screenshot(page, "test_tc_Reporting_267", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_Alldevices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_Alldevices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_268.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_Alldevices')
        save_screenshot(page, "test_tc_Reporting_268", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_Alldevices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_Alldevices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_269.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_Alldevices')
        save_screenshot(page, "test_tc_Reporting_269", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_Alldevices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_Alldevices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_270.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_Alldevices')
        save_screenshot(page, "test_tc_Reporting_270", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_Alldevices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_Alldevices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("clicking on  start date checkbox")
        click_start_date_checkbox(page)
        logger.info('clicked on start date checkbox successfully')
        logger.info("clicking on end date checkbox")
        click_end_date_checkbox(page)
        logger.info('clicked on end date checkbox successfully')
        page.wait_for_timeout(delay)

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_271.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_defaultdates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_Alldevices')
        save_screenshot(page, "test_tc_Reporting_271", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_272.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_272", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_273.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_273", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_274.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_274", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[1]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_275.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_275", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(
        page, credentials,delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="day of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by day of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            page.screenshot(path="test_tc_Reporting_276.png", full_page=True)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_day_of_week_with_daterange_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_276", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_278", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_278", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_279", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_279", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_280", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_280", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_281", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_281", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_282", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_282", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_283", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_283", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_284", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_284", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_285", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_285", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of week")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of week"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_286", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_286", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="hour of day")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_one_group_and_all_zones_and_generate_report(page,ENROLLMENT_GROUPS[4]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by hour of day"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_287", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices')
        save_screenshot(page, "test_tc_Reporting_287", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_SOE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[3]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_289", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_289", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)

def Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_ABE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_ABE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_290", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_ABE')
        save_screenshot(page, "test_tc_Reporting_290", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_PTE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_PTE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_291", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_PTE')
        save_screenshot(page, "test_tc_Reporting_291", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_FRAUDE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_FRAUDE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_291", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_FRAUDE')
        save_screenshot(page, "test_tc_Reporting_291", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_VIPE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        click_start_date_checkbox(page)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        click_end_date_checkbox(page)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_293", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_numberof_probable_match_events_by_zone_with_default_dates_last_1_month_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_293", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_SOE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_SOE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[2]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_294", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_SOE')
        save_screenshot(page, "test_tc_Reporting_294", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_ABE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_ABE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_295", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_ABE')
        save_screenshot(page, "test_tc_Reporting_295", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_PTE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_PTE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_296", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_PTE')
        save_screenshot(page, "test_tc_Reporting_296", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)


def Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_FRAUDE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_FRAUDE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_297", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_FRAUDE')
        save_screenshot(page, "test_tc_Reporting_297", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)



def Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_VIPE(page, credentials, delay):
    try:
        status = []
        logger.info(
            'Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_VIPE')
        print('logging in to portal')
        logger.info('logging in to portal')
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)
        logger.info('login to portal successful')

        # click on reporting menu
        logger.info('clicking  on report menu on dashboard')
        page.wait_for_timeout(delay)
        page.locator("div.dashboard-menu-item:has(p:has-text('Reporting'))").click()
        page.wait_for_timeout(delay)

        # ----------------- SELECT REPORT -----------------
        logger.info("clicking on 'report' dropdown ")
        page.locator("#reportField1Menu").click()
        page.wait_for_timeout(delay)
        logger.info("clicking on number of probable match events option")
        page.locator("#reportField1Menu").select_option(label="number of probable match events")
        page.wait_for_timeout(delay)

        # ----------------- SELECT BY = ZONE -----------------
        logger.info("clicking on by dropdown")
        page.locator("#reportField2MenuA").wait_for(state="visible", timeout=10000)
        logger.info("selecting a enrollment option")
        page.locator("#reportField2MenuA").select_option(label="zone")
        page.wait_for_timeout(delay)

        # ----------------- PICK DATES -----------------
        logger.info("selecting  start date")
        select_start_date_with_checkbox_and_confirm(page, reporting_start_date, delay)
        logger.info("selecting start date successfully")
        logger.info("selecting end date")
        select_end_date_with_checkbox_and_confirm(page, delay)
        page.wait_for_timeout(delay)
        logger.info("selecting end date successfully")

        # ----------------- SELECT GROUPS -----------------
        print("Selecting required groups...")
        select_single_group(page,ENROLLMENT_GROUPS[0]["name"],delay)
        page.wait_for_timeout(delay)

        # VALIDATION
        expected_text = "number of probable match events by zone"
        heading = page.locator(".panel-heading", has_text="probable match events").first
        heading.wait_for(state="visible")
        actual_text = heading.inner_text().replace("TSV", "").strip()
        if actual_text.lower() == expected_text.lower():
            print(f"Expected: '{expected_text}', Actual: '{actual_text}'")
            status.append(True)
        else:
            status.append(False)
        logger.info(f"status is {status}")
        if False in status:
            save_screenshot(page, "test_tc_Reporting_298", screenshot_path)
            return False
        else:
            return True
    except Exception as ex:
        logger.error(f'Exception: {type(ex).__name__}')
        print(f'Exception: {type(ex).__name__}')
        print(
            f'exception: Verify_report_for_number_of_probable_match_events_by_zone_with_date_range_with_group_selected_as_VIPE')
        save_screenshot(page, "test_tc_Reporting_298", screenshot_path)
    finally:
        logout_if_logged_in(page,delay)















