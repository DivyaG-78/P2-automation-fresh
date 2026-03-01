from playwright.sync_api import expect
from utilities import *
import conftest


# Helper Functions
def navigate_to_operational(page, delay, system_name):
    logger.info("Navigating to Operational section")
    page.get_by_role("textbox", name="Search").fill(system_name)
    page.wait_for_timeout(delay)
    page.get_by_role("img").nth(3).click()
    page.wait_for_timeout(delay)
    page.locator("xpath=(//a[@role='button'])[1]").click()


def open_action_menu(page, delay):
    logger.info("Opening action menu")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.wait_for_timeout(delay)


def take_screenshot(page, path):
    logger.info(f"Taking screenshot: {path}")
    page.screenshot(path=path)


# Test 1: Edit Core Name
def test_core_name_edit_1(page, credentials, delay):
    try:
        logger.info("Starting test: Edit Core Name")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, conftest.CORE_NAME)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Edit").click()
        page.wait_for_timeout(delay)
        name_box = page.get_by_role("textbox", name="Name *")
        name_box.clear()
        page.wait_for_timeout(delay)
        name_box.fill(conftest.EDITED_NAME)
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Edit").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_1_core_name_edit_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during core name edit: {e}")
        take_screenshot(page, "screenshots/dm/_1_core_name_edit_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _1_core_name_edit_")


# Test 2: Refresh License
def test_core_refresh_license_2(page, credentials, delay):
    try:
        logger.info("Starting test: Core Refresh License")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, conftest.CORE_NAME)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Refresh License").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Refresh").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_2_core_refresh_license_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during license refresh: {e}")
        take_screenshot(page, "screenshots/dm/_2_core_refresh_license_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _2_core_refresh_license_")


# Test 3: Network Test
def test_core_network_test_3(page, credentials, delay):
    try:
        logger.info("Starting test: Core Network Test")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, conftest.CORE_NAME)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Network Test").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Start").click()

        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_3_core_network_test_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during network test: {e}")
        take_screenshot(page, "screenshots/dm/_3_core_network_test_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _3_core_network_test_")


# Test 4: Edit edge Name
def test_edge_name_edit_4(page, credentials, organization, delay):
    try:
        logger.info("Starting test: Edit edge Name")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, organization)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Edit").click()
        page.wait_for_timeout(delay)
        name_box = page.get_by_role("textbox", name="Name *")
        name_box.clear()
        page.wait_for_timeout(delay)
        name_box.fill(conftest.EDITED_EDGE_NAME)
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Edit").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_4_edge_name_edit_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during edge name edit: {e}")
        take_screenshot(page, "screenshots/dm/_4_edge_name_edit_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _4_edge_name_edit_")


# Test 5: redeploy edge Name
def test_edge_redeploy_5(page, credentials, organization, delay):
    try:
        logger.info("Starting test: Edge Redeploy")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, organization)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Redeploy").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Redeploy").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_5_edge_redeploy_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during edge redeploy: {e}")
        take_screenshot(page, "screenshots/dm/_5_edge_redeploy_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _5_edge_redeploy_")


# Test 6: force resync edge Name
def test_edge_force_resync_5(page, credentials, organization, delay):
    try:
        logger.info("Starting test: Edge Force Resync")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, organization)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Force Resync").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Resync").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_6_edge_force_resync_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during edge force resync: {e}")
        take_screenshot(page, "screenshots/dm/_6_edge_force_resync_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _6_edge_force_resync_")


# Test 7: Refresh License
def test_edge_refresh_license_7(page, credentials, organization, delay):
    try:
        logger.info("Starting test: Edge Refresh License")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, organization)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Refresh License").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Refresh").click()
        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_7_edge_refresh_license_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during edge license refresh: {e}")
        take_screenshot(page, "screenshots/dm/_7_edge_refresh_license_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _7_edge_refresh_license_")


# Test 8: Network Test
def test_edge_network_test_8(page, credentials, organization, delay):
    try:
        logger.info("Starting test: Network Test")
        page.goto(conftest.REGISTER_LOGIN_URL)
        dm_log_in(page, credentials, delay)
        welcome(page, delay)

        navigate_to_operational(page, delay, organization)
        page.wait_for_timeout(delay)
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        open_action_menu(page, delay)

        page.get_by_role("menuitem", name="Network Test").click()
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="Start").click()

        page.wait_for_timeout(7000)
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)

        take_screenshot(page, "screenshots/dm/_8_edge_network_test_passed.png")
    except Exception as e:
        logger.error(f"An error occurred during edge network test: {e}")
        take_screenshot(page, "screenshots/dm/_8_edge_network_test_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _8_edge_network_test_")


def test_dm_platform_alerts_9(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_alerts_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="AlertsAlert threshold: 0.84,").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min alert threshold *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min alert threshold *").fill("0.85")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min mask alert threshold *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min mask alert threshold *").fill("0.86")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="AlertsAlert threshold: 0.85,").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min alert threshold *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min alert threshold *").fill("0.84")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min mask alert threshold *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Min mask alert threshold *").fill("0.85")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        take_screenshot(page, "screenshots/dm/platform/_9_dm_platform_alerts.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform analytics: {e}")
        take_screenshot(page, "screenshots/dm/platform/_9_dm_platform_alerts_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_alerts_9_")


def test_dm_platform_camera_monitoring_10(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_camera_monitoring_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Camera MonitoringInactivity").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="hour").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="2 hours", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Camera MonitoringInactivity").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="2 hours").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="1 hour", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        take_screenshot(page, "screenshots/dm/platform/_10_dm_platform_camera_monitoring.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform camera monitoring: {e}")
        take_screenshot(page, "screenshots/dm/platform/_10_dm_platform_camera_monitoring_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_camera_monitoring_10_")


def test_dm_platform_email_domain_validation_11(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_email_domain_validation_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Email Domain").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Email Domain Validation").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox").fill("facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox").nth(1).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox").nth(1).fill("gatekeepersystems.in")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_11_dm_platform_email_domain_validation.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform email domain validation: {e}")
        take_screenshot(page, "screenshots/dm/platform/_11_dm_platform_email_domain_validation_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_email_domain_validation_11_")


def test_dm_platform_enrollment_quality_12(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_enrollment_quality_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Enrollments Quality").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_label("", exact=True).check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Enrollments Quality").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_label("", exact=True).uncheck()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_12_dm_platform_enrollment_quality.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform enrollment quality error: {e}")
        take_screenshot(page, "screenshots/dm/platform/_12_dm_platform_enrollment_quality_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_enrollment_quality_12_")


def test_dm_platform_system_offline_alerts_13(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_system_offline_alerts__")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="System Offline Alert").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enable Edge System Offline").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#emailRecipients").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#emailRecipients").fill("operator")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Report when Edge System has").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enable hourly email alerts").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="System Offline Alert").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enable Edge System Offline").uncheck()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_13_dm_platform_system_offline_alerts.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform system offline alerts: {e}")
        take_screenshot(page, "screenshots/dm/platform/_13_dm_platform_system_offline_alerts_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_system_offline_alerts_13_")


def test_dm_platform_face_detection_quality_14(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_face_detection_quality_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Face DetectionQuality").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Quality Threshold *").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Quality Threshold *").fill("0.52")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Masked Face Threshold *").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Masked Face Threshold *").fill("0.57")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Face DetectionQuality").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Quality Threshold *").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Quality Threshold *").fill("0.51")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Masked Face Threshold *").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Masked Face Threshold *").fill("0.56")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_14_dm_platform_face_detection_quality.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform face detection quality: {e}")
        take_screenshot(page, "screenshots/dm/platform/_14_dm_platform_face_detection_quality_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_face_detection_quality_14_")


def test_dm_platform_face_encode_15(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_face_encode_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Face EncodeParallel Search: 1").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="1").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="2").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Info").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="Debug").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Face EncodeParallel Search: 2").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="2").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="1").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Debug").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="Info").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_15_dm_platform_face_encode.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform face encode: {e}")
        take_screenshot(page, "screenshots/dm/platform/_15_dm_platform_face_encode_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_face_encode_15_")


def test_dm_platform_face_search_16(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_face_search_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Face SearchParallel Search: 1").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="1").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="2").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Info").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="Debug").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Face SearchParallel Search: 2").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="2").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="1").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Debug").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="Info").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_16_dm_platform_face_search.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform face search: {e}")
        take_screenshot(page, "screenshots/dm/platform/_16_dm_platform_face_search_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_face_search_16_")


def test_dm_platform_training_system_17(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_training_system_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Training System").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Training Acknowledgment").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Exempt usernames (up to 5,").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Exempt usernames (up to 5,").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Exempt usernames (up to 5,").fill("operator")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="Training System").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Training Acknowledgment").uncheck()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_17_dm_platform_training_system.png")
        page.wait_for_timeout(delay)  # Explicit delay
        operational_icon = page.locator("xpath=(//*[name()='svg'][@title='Operational'])[1]")
        operational_icon.wait_for(state="visible", timeout=conftest.TIMEOUT_LONG)
    except Exception as e:
        logger.error(f"An error occurred during dm platform training system: {e}")
        take_screenshot(page, "screenshots/dm/platform/_17_dm_platform_training_system_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_training_system_17_")


def test_dm_platform_videos_18(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_platform_videos_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Enabled, retention indefinite").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Create a short evidence video").is_checked()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="indefinite").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="15 days").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(5)  # Explicit delay
        take_screenshot(page, "screenshots/dm/platform/_18_dm_platform_videos.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform videos: {e}")
        take_screenshot(page, "screenshots/dm/platform/_18_dm_platform_videos_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_videos_18_")


def test_dm_platform_dashboard_disable_19_(page, credentials, delay):
    try:
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        logger.info("Starting test: _dm_platform_dashboard_disable_19_")
        page.get_by_role("listitem").filter(has_text="Analytics/DashboardEnabled").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Insights Dashboard enabled").uncheck()
        page.screenshot(path="screenshots/dm/platform/_19_dm_platform_dashboard_disable.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        core_name = conftest.BASE_URL.split("//")[1].split(".")[0]
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Search").fill(core_name)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("img").nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//a[@role='button'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        try:
            page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=300000)
        except Exception as e:
            logger.error(f"{e}")
            page.locator("div").filter(has_text=re.compile(r"^Warning$")).nth(1).wait_for(state="visible", timeout=300000)
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//div[@role='button'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Logging in with provided credentials")
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name=conftest.BASE_URL).click()
            page.wait_for_timeout(delay)  # Explicit delay
        page1 = page1_info.value
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("textbox", name="Username").fill(USERNAME)
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("textbox", name="Password").fill(PASSWORD)
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_text("Login").click()
        try:
            page1.get_by_text("Insights Dashboard").click()
            logger.error("Insight Dashboard is Visible")
        except Exception as e:
            logger.error(f"{e}")
            logger.info("Insight Dashboard is Disabled")
        logger.info("Logging out")
        page1.get_by_text("Logout").click()
        page1.close()
    except Exception as e:
        logger.error(f"An error occurred during dm platform analytics: {e}")
        page.screenshot(path="screenshots/dm/platform/_19_dm_platform_dashboard_disable_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_dashboard_disable_19_")


def test_dm_edge_camera_delete_21_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_edge_camera_delete_21_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("textbox", name="Search").fill(organization)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("img").nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name=organization + " Status:").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Add Camera Manually").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="RS RTSP Stream Create camera").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="RTSP Stream").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="RTSP Stream").fill("rtsp://:8444/v2")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_21_dm_edge_camera_delete_not_enabled.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//button[@aria-label='More'])[2]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//li[normalize-space()='Edit'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Description").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Description").fill(organization + "/8444/v2")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enabled").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("tab", name="Geolocation").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("div").filter(has_text=re.compile(r"^Location$")).get_by_role("textbox").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("div").filter(has_text=re.compile(r"^Location$")).get_by_role("textbox").fill(conftest.GEOLocation)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=300000)  # Timeout set to 5 min
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//button[@aria-label='More'])[2]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//li[normalize-space()='Edit'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enabled").uncheck()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.wait_for_timeout(delay)  # Explicit delay
        page.reload()
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=300000)  # Timeout set to 5 min
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//button[@aria-label='More'])[2]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Delete Camera").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Delete").click()
        page.screenshot(path="screenshots/dm/_21_dm_edge_camera_delete_enabled.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm edge camera configuration: {e}")
        page.screenshot(path="screenshots/dm/_21_dm_edge_camera_delete_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_edge_camera_delete_21_")


def test_dm_health_metrics_22_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_health_metrics_22_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        li = [conftest.CORE_NAME, organization]
        page.get_by_role("textbox", name="Search").fill(li[0])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("img").nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=((//a[@role='button'])[1])").click()
        page.wait_for_timeout(delay)  # Explicit delay
        core_text = f"Health Metrics - {li[0]}-vm"
        locator1 = page.get_by_text(core_text)
        logger.info(locator1.inner_text())
        assert locator1.is_visible(), "Health Metrics core is not visible!"
        page.locator("xpath=(//div[@role='button'])[1]").click()
        page.get_by_role("textbox", name="Search").fill(li[1])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("img").nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=((//a[@role='button'])[1])").click()
        page.wait_for_timeout(delay)  # Explicit delay
        edge_text = f"Health Metrics - {organization}"
        locator2 = page.get_by_text(edge_text)
        logger.info(locator2.inner_text())
        assert locator2.is_visible(), "Health Metrics edge is not visible!"
        page.locator("xpath=(//div[@role='button'])[1]").click()
    except Exception as e:
        logger.error(f"Health Metrics Error: {e}")
        page.screenshot(path="screenshots/dm/_22_dm_health_metrics_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_health_metrics_22_")


def test_dm_add_user_verify_user_23_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_health_metrics_22_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        logger.info(f"Add New User")
        page.get_by_role("button", name="Manage Users").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Add User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Name *").fill("demo")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Email (Username) *").fill("demo@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password Confirmation *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Create User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Logout").click()
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info(f"Login Using New Added User")
        page.get_by_role("textbox", name="Email (Username) *").fill("demo@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Logout").click()
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info(f"Normal User Delete Newly Added User")
        dm_log_in(page, credentials, delay)
        page.get_by_role("button", name="Manage Users").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Delete").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Delete").nth(1).click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"Add User Verify Error: {e}")
        page.screenshot(path="screenshots/dm/_23_dm_add_user_verify_user_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_add_user_verify_user_23_")


def test_dm_duplicate_user_not_allowed_24_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_duplicate_user_not_allowed_24_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        logger.info(f"Add New User with same username")
        page.get_by_role("button", name="Manage Users").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Add User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Name *").fill(CORE_NAME)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Email (Username) *").fill(EMAIL)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password Confirmation *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Create User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        pattern = r"Username '.*' is already taken\."
        expect(page.get_by_role("main")).to_contain_text(re.compile(pattern))
        logger.info(f"Added New User with Same Username Not Allowed")
    except Exception as e:
        logger.error(f"Duplicate User NOt Allowed Error: {e}")
        page.screenshot(path="screenshots/dm/_24_dm_duplicate_user_not_allowed_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_duplicate_user_not_allowed_24_")


def test_dm_new_user_password_update_25_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_new_user_password_update_25_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        logger.info(f"login with old user and Add New User")
        page.get_by_role("button", name="Manage Users").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Add User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Name *").fill("demo")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Email (Username) *").fill("demo@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password Confirmation *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Create User").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Logout").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info(f"New user is created/added")
        logger.info(f"login with new added user and update the password")
        page.get_by_role("textbox", name="Email (Username) *").fill("demo@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("link", name="Profile").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Old Password *").fill(PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="New Password *").fill("Left_1r1s")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password Confirmation *").fill("Left_1r1s")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Update").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Logout").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info(f"Login again with newly added user with updated password")
        page.get_by_role("textbox", name="Email (Username) *").fill("demo@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill("Left_1r1s")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Login").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Logout").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info(f"login with old user, delete newly added User and updated passed")
        dm_log_in(page, credentials, delay)
        page.get_by_role("button", name="Manage Users").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Delete").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Delete").nth(1).click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"Add User Verify Error: {e}")
        page.screenshot(path="screenshots/dm/_25_dm_new_user_password_update_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Test completed: _dm_new_user_password_update_25_")


def test_enroll_subjects_roc_20_(page, credentials, users, image_files_roc, num_subjects_roc, organization, delay):
    try:
        logger.info("Starting test: _enroll_subjects_roc_20_")
        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        subjects = image_files_roc[:num_subjects_roc]  # Get the list of image files from the directory
        logger.info(f"Subjects to enroll: {subjects}")

        groups = [
            ("abe (Serious Offender - Medium)", "300"),
            ("fraude (Serious Offender - None)", "50"),
            ("pte (Serious Offender - Low)", "150"),
            ("soe (Serious Offender - High)", "500"),
            ("vipe (Serious Offender - None)", "0")
        ]

        group_size = num_subjects_roc // len(groups)
        page.wait_for_timeout(delay)  # Explicit delay

        for i, subject in enumerate(subjects):
            group_index = i // group_size
            if group_index >= len(groups):
                group_index = len(groups) - 1

            enroll_subject(page, subject, groups[group_index], organization, i, delay)

    except Exception as e:
        logger.error(f"An error occurred during identity & enroll: {e}")
        page.screenshot(path=f"screenshots/_20_enroll_subjects_roc_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Test completed: _enroll_subjects_roc_20_")


def test_approve_subjects_roc_26_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_approve_subjects_roc_26_")

        first_user = users[4]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Enrollments (filter approve) page")
        page.get_by_text("Enrollments").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Filtering pending review enrollments")
        filter_pending_review(page, delay)

        logger.info("Approving enrollments")
        approve_enrollments(page, delay)

        logger.info("Closing the enrollments page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Taking final success screenshot")
        page.screenshot(path=f"screenshots/_26_approve_enroll_subjects_roc_success.png")
    except Exception as e:
        logger.error(f"An error occurred during approve enrollment: {e}")
        page.screenshot(path=f"screenshots/_26_approve_enroll_subjects_roc_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_approve_subjects_roc_26_")
