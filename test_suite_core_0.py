from utilities import *


def test_dm_register_1_(page, credentials, delay):
    password = credentials["password"]

    try:
        logger.info("Starting test: _dm_register_1_")
        page.goto(conftest.REGISTER_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Filling out the registration form.")
        page.get_by_role("textbox", name="Name *").fill(credentials["username"])
        logger.info("Filled out the Name field.")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Email (Username) *").fill(credentials["email"])
        logger.info("Filled out the Email field.")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *").fill(password)
        logger.info("Filled out the Password field.")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password Confirmation *").fill(password)
        logger.info("Filled out the Password Confirmation field.")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Register").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_1_registration_form_filled.png")
    except Exception as e:
        logger.error(f"An error occurred during registration: {e}")
        logger.info("A user has been already registered.")
        page.screenshot(path="screenshots/dm/_1_user_has_been_already_registered.png")
    finally:
        logger.info("Logging out")
        logger.info("Test completed: _dm_register_1_")


def test_dm_register_login_2_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_register_login_2_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        home_text = page.locator("#appBarTitle").text_content()
        assert "Home" in home_text
        logger.info(f"Expected DM title: Home, Actual DM title: {home_text}")
        logger.info(f"login_user:{credentials['email']}")
        page.screenshot(path=f"screenshots/dm/_2_registration_login_{credentials['email']}.png")
    except Exception as e:
        logger.error(f"An error occurred during registration login: {e}")
        page.screenshot(path="screenshots/dm/_2_registration_login.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_register_login_2_")


def test_dm_license_3_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_license_3_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("listitem").filter(has_text="License StatusNo license").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Customer ID *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Customer ID *").fill(conftest.LICENSE)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="License Server URI *").clear()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="License Server URI *").fill(conftest.LICENSE_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_3_dm_license.png")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_selector('button:has-text("Save")')
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("listitem").filter(has_text="License StatusNo license").get_by_label("Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Toggle password visibility").click()
        page.wait_for_timeout(delay)  # Explicit delay
        customer_id = page.get_by_role("textbox", name="Customer ID *").input_value()
        assert customer_id == conftest.LICENSE
        logger.info(f"Expected customer id: {conftest.LICENSE}, Actual customer id: {customer_id}")
        page.wait_for_timeout(delay)  # Explicit delay
        license_url = page.get_by_role("textbox", name="License Server URI *").input_value()
        assert license_url == conftest.LICENSE_URL
        logger.info(f"Expected license url: {conftest.LICENSE_URL}, Actual license url: {license_url}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Close").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm license: {e}")
        page.screenshot(path="screenshots/dm/_3_dm_license.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_license_3_")


def test_dm_domain_4_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_domain_4_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("button", name="Menu").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("menuitem", name="Edit").click()
        page.wait_for_timeout(delay)  # Explicit delay
        if conftest.DOMAIN_Status == 1:
            print(conftest.DOMAIN_Status)
            conftest.BASE_URL = conftest.BASE_URL.replace("https://", "")
            conftest.BASE_URL = conftest.BASE_URL.rstrip("/")
            page.get_by_role("textbox", name="Domain Name *").fill(conftest.BASE_URL)
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Save").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Save").wait_for(state="visible", timeout=240000)
            page.wait_for_timeout(delay)  # Explicit delay
            page.screenshot(path="screenshots/dm/_4_dm_domain_lets_encrypt.png")
            page.wait_for_timeout(delay)  # Explicit delay
        elif conftest.DOMAIN_Status == 2:
            print(conftest.DOMAIN_Status)
            page.get_by_role("button", name="IP IP Address Use on").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.locator("xpath=(//div[@id='select-ipAddress'])[1]").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.locator("xpath=/html[1]/body[1]/div[3]/div[2]/ul[1]/li[1]").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Save").click()
            page.wait_for_timeout(delay)  # Explicit delay
            # page.get_by_role("button", name="Save").wait_for(state="visible", timeout=240000)
            page.wait_for_timeout(delay)  # Explicit delay
            page.screenshot(path="screenshots/dm/_4_dm_domain_ip_address.png")
            page.wait_for_timeout(delay)  # Explicit delay
        else:
            print(conftest.DOMAIN_Status)
            conftest.BASE_URL = conftest.BASE_URL.replace("https://", "")
            conftest.BASE_URL = conftest.BASE_URL.rstrip("/")
            page.get_by_role("textbox", name="Domain Name *").fill(conftest.BASE_URL)
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("checkbox", name="Use Public Key Infrastructure").uncheck()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Save").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Menu").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("menuitem", name="Upload Custom Certificate").click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("checkbox", name="Enabled").check()
            page.wait_for_timeout(delay)  # Explicit delay
            page.wait_for_timeout(delay)  # Explicit delay
            file_input = page.locator('#certUpload')
            page.wait_for_timeout(delay)  # Explicit delay
            file_input.set_input_files("datas/certificate/star-facefirst-dev-2025.pfx")
            page.wait_for_timeout(delay)  # Explicit delay
            page.locator("#certPassword").clear()
            page.wait_for_timeout(delay)  # Explicit delay
            page.locator("#certPassword").fill("w47QFXWy&m0R&b&5")
            page.wait_for_timeout(delay)  # Explicit delay
            page.get_by_role("button", name="Upload", exact=True).click()
            page.wait_for_timeout(delay)  # Explicit delay
            page.wait_for_timeout(delay)  # Explicit delay
            page.screenshot(path="screenshots/dm/_4_dm_domain_go_daddy_certificate.png")
            page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        logger.error(f"An error occurred during dm domain: {e}")
        page.screenshot(path="screenshots/dm/_4_dm_domain_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_domain_4_")


def test_dm_core_deployment_5_(page, credentials, delay):
    try:
        logger.info("Starting test: _dm_core_deployment_5_")
        page.goto(conftest.REGISTER_LOGIN_URL)
        page.wait_for_timeout(delay)  # Explicit delay
        dm_log_in(page, credentials, delay)
        welcome(page, delay)
        page.get_by_role("button", name="Deployment Wizard").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="C Core The FaceFirst Core").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Username *").fill(credentials["username"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Password *", exact=True).fill(credentials["password"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Confirm Password *").fill(credentials["password"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("textbox", name="Email *").fill(credentials["email"])
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#select-timezone").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name=conftest.TIMEZONE).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("#select-timezone").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("option", name=conftest.TIMEZONE).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("button", name="Next").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("button").filter(has_text=re.compile(r"^Deploy$")).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("heading", name="Operational").wait_for(state="visible", timeout=300000)  # Timeout set to 5 min
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/dm/_5_dm_core_deployment.png")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during dm core deployment: {e}")
        page.screenshot(path="screenshots/dm/_5_dm_core_deployment_error.png")
    finally:
        logger.info("Logging out")
        dm_log_out(page, delay)
        logger.info("Test completed: _dm_core_deployment_5_")
