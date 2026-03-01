from playwright.sync_api import expect
from utilities import *


def test_dm_json_import_1_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_json_import_1_")
        page.goto(conftest.JSONUrl)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Authorize").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="auth-basic-username").fill(credentials["username"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="auth-basic-password").fill(credentials["password"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Apply credentials").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Close").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="GET /api/AntiForgery", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Try it out").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Execute", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="GET /api/AntiForgery", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="POST /api/Regions/import Import multiple regions from a JSON file to set up").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Try it out").click()
        page.wait_for_timeout(delay)  # Explicit delay
        try:
            page.locator("input[type='file']").set_input_files(conftest.JSONFile)
        except Exception as e:
            logger.info(f"{e}")
            page.get_by_role("textbox").set_input_files(conftest.JSONFile)
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Execute", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/json/_1_dm_json_import.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm json import: {e}")
        page.screenshot(path="screenshots/dm/json/_1_dm_json_import_error.png")
    finally:
        logger.info("Logging out")
        # dm_log_out(page, delay)
        logger.info("Test completed: _dm_json_import_1_")


def test_dm_edge_deployment_2_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_edge_deployment_2_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("textbox", name="Search").fill(organization)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("img").nth(3).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name=organization + " Status: Undeployed").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Deployment Wizard").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="E Edge This option is").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        print('\nclicked first next btn')
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("input[type=\"checkbox\"]").first.check()
        print('clicked first checkbox')
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next", exact=True).click()
        print('clicked second next btn')
        page.wait_for_timeout(delay)  # Explicit delay
        # page.locator("input[type=\"checkbox\"]").first.check()
        # print('clicked second checkbox')
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next", exact=True).click()
        print('clicked third next btn')
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_text("Kroger Queens - KQS").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Yes").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#select-timezone").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="(UTC+05:30) Chennai, Kolkata").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        expect(page.get_by_role("checkbox")).to_contain_text("Timezone: (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Back").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_text(conftest.SELECTRegion).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Yes").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#select-timezone").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name=conftest.TIMEZONE).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("button").filter(has_text=re.compile(r"^Deploy$")).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=300000)
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_2_dm_edge_deployment.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm edge deployment: {e}")
        page.screenshot(path="screenshots/dm/_2_dm_edge_deployment.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_edge_deployment_2_")


def test_dm_edge_camera_configuration_3_(page, credentials, organization, delay):
    try:
        logger.info("Starting test: _dm_edge_camera_configuration_3_")
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
        page.get_by_role("textbox", name="RTSP Stream").fill("rtsp://:" + conftest.RTSPPort)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_3_dm_edge_camera_not_enabled.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//button[@aria-label='More'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//li[normalize-space()='Edit'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Description").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Description").fill(organization + "/" + conftest.RTSPPort)
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
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=300000)  # Timeout set to 5 min
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_3_dm_edge_camera_enabled.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm edge camera configuration: {e}")
        page.screenshot(path="screenshots/dm/_3_dm_edge_camera_configuration_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_edge_camera_configuration_3_")


def test_dm_domain_verify_user_need_not_to_fill_domain_url_4_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_domain_verify_user_need_not_to_fill_domain_url_under_Domain_Status_4_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("button", name="Menu").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        domain_text = page.get_by_role("heading").inner_text()
        assert "Domain Settings Unavailable" in domain_text
        logger.info(f"Expected Domain Text: Domain Settings Unavailable, Actual Domain Text: {domain_text}")
        page.get_by_role("button", name="OK").click()
    except Exception as e:
        logger.error(f"An error occurred during dm core deployment: {e}")
        page.screenshot(path="screenshots/dm/_4_dm_domain_verify_user_need_not_to_fill_domain_url_4_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_domain_verify_user_need_not_to_fill_domain_url_4_")


def test_dm_roc_license_request_button_Enable_roc_license_5_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_roc_license_request_button_Enable_roc_license_5_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="Additional Algo License").get_by_label("Edit").click()
        with page.expect_download() as download_info:
            page.get_by_role("button", name="Request").click()
            page.wait_for_timeout(delay)  # Explicit delay
        download = download_info.value
        download.save_as(f'screenshots/roc_downloads/{download.suggested_filename}')
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enable Additional Algo").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_label("Browse").set_input_files("datas/certificate/ROC-client (900b7652-eded-4a93-8588-b59625fcc2e1).lic")
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(7000)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm core deployment: {e}")
        page.screenshot(path="screenshots/dm/_5_dm_roc_license_request_button_Enable_roc_license_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_roc_license_request_button_Enable_roc_license_5_")


def test_dm_platform_dashboard_6_(page, credentials, delay):
    try:
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        logger.info("Starting test: _dm_platform_analytics_6_")
        page.get_by_role("listitem").filter(has_text="Analytics/DashboardDisabled").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Insights Dashboard enabled").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Include masked faces").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="hours").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="8 hours", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_6_dm_platform_analytics.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform analytics: {e}")
        page.screenshot(path="screenshots/dm/platform/_6_dm_platform_analytics_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_analytics_6_")


def test_dm_platform_email_7_(page, credentials, delay):
    try:
        # global result
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Starting test: _dm_platform_email_7_")
        page.get_by_role("listitem").filter(has_text="EmailDisabled").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Email enabled").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Host *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Host *").fill("smtp.office365.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Sender *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Sender *").fill("qanotifications@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Use Credentials").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Username *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Username *").fill("qanotifications@facefirst.com")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#smtpPassword").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#smtpPassword").fill("Q@F@ceFirst1234")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_7_dm_platform_email.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform email: {e}")
        page.screenshot(path="screenshots/dm/platform/_7_dm_platform_email_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_email_7_")


def test_dm_platform_message_broker_8_(page, credentials, delay):
    try:
        # global result
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Starting test: _dm_platform_message_broker_8_")
        page.get_by_role("listitem").filter(has_text="Message BrokerDisabled").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("checkbox", name="Enable MessageBroker").check()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Host *").fill("127.0.0.1")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Port *").fill("1883")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Username *").fill(conftest.USERNAME)
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#password").fill(conftest.PASSWORD)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Base Topic *").fill("FaceFirst")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_8_dm_platform_message_broker.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform Session: {e}")
        page.screenshot(path="screenshots/dm/platform/_8_dm_platform_message_broker_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_message_broker_8_")


def test_dm_platform_session_9_(page, credentials, delay):
    try:
        # global result
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Starting test: _dm_platform_Session_9_")
        page.get_by_role("listitem").filter(has_text="Session Time Out15 minutes").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="minutes").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name="24 hours").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_9_dm_platform_Session.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform Session: {e}")
        page.screenshot(path="screenshots/dm/platform/_9_dm_platform_Session_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_Session_9_")


def test_dm_platform_visitor_10_(page, credentials, delay):
    try:
        # global result
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Starting test: _dm_platform_Visitorsclustering_10_")
        page.get_by_role("listitem").filter(has_text="Visitorsclustering at 0.8").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("spinbutton", name="Visitor Retention (Days) *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("spinbutton", name="Visitor Retention (Days) *").fill("14")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_10_dm_platform_Visitorsclustering.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform Visitorsclustering: {e}")
        page.screenshot(path="screenshots/dm/platform/_10_dm_platform_Visitorsclustering_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_platform_Visitorsclustering_10_")


def test_post_dm_platform_verify_core_operational_11_(page, credentials, organization, delay):
    try:
        # global result
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
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
            logger.info(f"{e}")
        page.get_by_role("heading", name="Warning").wait_for(state="visible", timeout=300000)
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/platform/_11_post_dm_platform_verify_core_operational.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm platform Visitorsclustering: {e}")
        page.screenshot(path="screenshots/dm/platform/_11_post_dm_platform_verify_core_operational_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _post_dm_platform_verify_core_operational_11_")
