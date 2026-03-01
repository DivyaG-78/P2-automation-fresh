import pandas as pd
from conftest import *
import conftest
from datetime import timedelta
import re

logger = logging.getLogger(__name__)


def log_in(page, username, password, delay):
    logger.info("Navigating to login page")
    page.goto(conftest.BASE_URL)
    page.wait_for_timeout(delay)  # Explicit delay

    logger.info("Filling in username")
    if page.get_by_role("textbox", name="Username").is_visible():
        page.get_by_role("textbox", name="Username").fill(username)
        logger.info("Filled Username")
    else:
        logger.warning("Username textbox not found")

    page.wait_for_timeout(delay)  # Explicit delay

    logger.info("Filling in password")
    if page.get_by_role("textbox", name="Password").is_visible():
        page.get_by_role("textbox", name="Password").fill(password)
        logger.info("Filled Password")
    else:
        logger.warning("Password textbox not found")

    page.wait_for_timeout(delay)  # Explicit delay

    logger.info("Clicking login button")
    if page.get_by_text("Login").is_visible():
        page.get_by_text("Login").click()
        logger.info("Clicked Login button")
    else:
        logger.warning("Login button not found")

    page.wait_for_timeout(delay)  # Explicit delay


def agree_to_term(page, delay):
    logger.info("Agreeing to terms")
    print("Agreeing to terms")
    if page.get_by_role("button", name="Click Here to Agree and Continue").is_visible():
        logger.info("Agree button is visible")
        print("Agree button is visible")
        page.get_by_role("button", name="Click Here to Agree and Continue").click()
        logger.info("Clicked Agree button")
        print("Clicked Agree button")
        page.wait_for_timeout(delay)  # Explicit delay
    else:
        print("Agree button is not visible")


def log_out(page, delay):
    logger.info("Checking if logout button is visible")
    if page.get_by_text("Logout").is_visible():
        logger.info("Logout button is visible")
        page.get_by_text("Logout").click()
        logger.info("Clicked Logout button")
        page.wait_for_timeout(delay)  # Explicit delay
    else:
        logger.warning("Logout button is not visible")


def verify_duplicates(page, locate):
    # Fetch the list of existing users
    check_duplicates = page.query_selector_all(locate)
    existing_data = [element.inner_text() for element in check_duplicates]
    return existing_data


def fill_user_details(page, user, credentials, delay):
    logger.info("Filling in user details")

    page.get_by_role("textbox", name="Username", exact=True).fill(user["username"])
    logger.info("Filled Username")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="First Name").fill(user["username"] + "F")
    logger.info("Filled First Name")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="Last Name").fill(user["username"] + "L")
    logger.info("Filled Last Name")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"userRoleId\"]").select_option(user["role_id"])
    logger.info("Selected User Role")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="New Password", exact=True).fill(credentials["password"])
    logger.info("Filled Password")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="Confirm Password").fill(credentials["password"])
    logger.info("Filled Confirm Password")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_text("Region Selection").click()
    logger.info("Clicked Region Selection")
    page.wait_for_timeout(delay)  # Explicit delay

    print(f'region searching: {user["region"]}')
    page.get_by_text(user["region"]).click()
    logger.info("Selected Region")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("region-search").get_by_text("Save").click()
    logger.info("Clicked Save in Region Search")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="User Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled User Email")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="Alert Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled Alert Email")
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        page.locator("select[name=\"timezoneId\"]").select_option(user["timezone"])
    except Exception as e:
        logger.info(f"{e}")
        page.locator("select[name=\"timezoneID\"]").select_option(user["timezone"])

    logger.info("Selected Timezone")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("a").filter(has_text="Save").click()
    logger.info("Clicked Save")
    page.wait_for_timeout(delay)  # Explicit delay


def create_user(page, user, credentials, delay):
    logger.info(f"Creating user: {user['username']}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create User", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_user_details(page, user, credentials, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Verifying user creation")
    page.wait_for_timeout(delay)  # Explicit delay
    assert page.get_by_text("Success! A user has been created.").is_visible()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_2_user_creation_success_{user['username']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing user creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large"
    ).first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def fill_store_group_details(page, store_group, delay):
    logger.info("Filling in store group details")
    page.get_by_role("textbox", name="Name").fill(store_group["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Description").fill(store_group["name"] + "_des")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Org Selection").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#tree-root div").filter(has_text=store_group["org"]).locator("i").nth(1).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save").first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_store_group(page, store_group, delay, screenshot_path):
    status = []
    try:
        logger.info(f"Creating store group: {store_group['name']}")
        page.locator("a").filter(has_text="Action").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_text("Create Store Group", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        fill_store_group_details(page, store_group, delay)
        page.wait_for_timeout(delay)  # Explicit delay
        success_message = page.locator(
            "div.message-to-user-bubble:visible"
        ).filter(has_text="Success")
        success_message.wait_for(state="visible", timeout=8000)
        msg_text = success_message.inner_text().lower()
        if "store group" in msg_text:
            return True
        else:
            save_screenshot(page, "test_TC_SG_15", screenshot_path)
            return False
    except Exception as e:
        print(f"Success message not visible: {e}")
        save_screenshot(page, "test_TC_SG_15", screenshot_path)
        return False
    finally:
        logger.info("Verifying store group creation")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path=f"screenshots/_3_store_group_creation_success_{store_group['name']}.png")
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info("Closing store group creation panel")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator(
            "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large"
        ).click()
        page.wait_for_timeout(delay)  # Explicit delay


def fill_additional_user_details(page, user, credentials, store_group, delay):
    logger.info("Filling in user details")
    page.get_by_role("textbox", name="Username", exact=True).fill(user["username"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="First Name").fill(user["username"] + "F")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Last Name").fill(user["username"] + "L")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("select[name=\"userRoleId\"]").select_option(user["role_id"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="New Password", exact=True).fill(credentials["password"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Confirm Password").fill(credentials["password"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Region Selection").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(user["region"]).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("select[name=\"storeGroupId\"]").select_option(store_group["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="User Email").fill(user["username"] + "@facefirst.com")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Alert Email").fill(user["username"] + "@facefirst.com")
    page.wait_for_timeout(delay)  # Explicit delay
    try:
        page.locator("select[name=\"timezoneId\"]").select_option(user["timezone"])
    except Exception as e:
        logger.info(f"{e}")
        page.locator("select[name=\"timezoneID\"]").select_option(user["timezone"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Save").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_additional_user(page, user, credentials, store_group, delay):
    logger.info(f"Creating additional user: {user['username']}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create User", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_additional_user_details(page, user, credentials, store_group, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Verifying user creation")
    page.wait_for_timeout(delay)  # Explicit delay
    assert page.get_by_text("Success! A user has been created.").is_visible()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_4_additional_user_creation_success_{user['username']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing user creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large"
    ).first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def fill_notification_group_details(page, ng, delay):
    logger.info("Filling in notification group details")
    page.get_by_role("textbox", name="Name", exact=True).fill(ng["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Description", exact=True).fill(ng["name"] + "_des")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Save").click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_users_to_notification_group(page, ng, delay):
    logger.info("Adding users to notification group")
    page.get_by_role("button", name="Users").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#UserView a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Unlinked Users").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#UserView").get_by_role("listitem").filter(has_text=ng["user_ng"]).get_by_role("insertion").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#UserView a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Add User(s) to Alert").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_5_NG_creation_success_{ng['name']}_linking_user_{ng['user_ng']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing notification group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#UserView > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_notification_group(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    add_users_to_notification_group(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing notification group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def fill_enrollment_group_details(page, eg, delay):
    logger.info("Filling in enrollment group details")
    page.get_by_role("textbox", name="Name").fill(eg["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Description").fill(eg["name"] + "_des")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").fill("0.84")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").fill("0.85")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("form[name=\"caseGroupForm\"] div").filter(has_text="Alert Color None Red Orange").locator(
        "#priority-select").select_option(eg["color"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("form[name=\"caseGroupForm\"] div").filter(has_text="Serious Offender High Medium").locator(
        "#priority-select").select_option(eg["priority"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_notification_groups_to_enrollment_group(page, eg, delay):
    logger.info("Adding notification groups to enrollment group")
    page.get_by_role("button", name="Notification Groups").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#AlertGroupIndex a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Unlinked Notification Groups").click()
    page.wait_for_timeout(delay)  # Explicit delay
    ng_name = eg["eg_ng"].split()[0]
    ng_row = page.locator("#AlertGroupIndex li", has_text=ng_name)
    ng_row.wait_for(state="visible", timeout=5000)
    ng_row.locator(".icheckbox_polaris .iCheck-helper").click(force=True)
    page.locator("#AlertGroupIndex a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Add To Enrollment Groups").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_6_EG_creation_success_{eg['name']}_linking_user_{eg['eg_ng']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing enrollment group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#AlertGroupIndex > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_enrollment_group(page, eg, delay):
    logger.info(f"Creating enrollment group: {eg['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Enrollment Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_enrollment_group_details(page, eg, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    add_notification_groups_to_enrollment_group(page, eg, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing enrollment group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def fill_tag_details(page, tag, delay):
    logger.info("Filling in tag details")
    page.get_by_role("textbox", name="Name", exact=True).fill(tag["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    if tag["serious_event"]:
        page.locator("#tag-serious-event").check()
        page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_tag(page, tag, delay):
    logger.info(f"Creating tag: {tag['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Tag").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_tag_details(page, tag, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_7_Tag_creation_success_{tag['name']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing tag creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def enroll_subject(page, subject, group, organization, index, delay):
    logger.info("Navigating to Identify & Enroll page")
    logger.info(f"Enrolling subject: {subject}")
    page.get_by_text("Identify & Enroll").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay

    identify_enroll_locator = page.locator("xpath=(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]")
    identify_enroll_locator.click()
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        print(text)
        logger.info(f"Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.info(f"{e}")
        logger.info(f"Add Details text is not visible")
        identify_enroll_locator = page.locator("div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)")
        identify_enroll_locator.click()
        page.wait_for_timeout(delay)  # Explicit delay

    page.screenshot(path=f"screenshots/_8_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"basis\"]").select_option("number:3")
    page.wait_for_timeout(delay)  # Explicit delay

    internal_group, spinbutton_value = group
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"internal_group\"]").select_option(internal_group)
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SELECT", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(organization).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").fill(f"store_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"enrollmentNumber\"]").fill(f"enroll_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("spinbutton").fill(spinbutton_value)
    page.wait_for_timeout(delay)  # Explicit delay
    input_box = page.get_by_placeholder("mm/dd/yyyy HH:mm")
    current_iso = datetime.now().strftime("%Y-%m-%dT%H:%M")
    max_attr = input_box.get_attribute("max")
    fill_value = current_iso if not max_attr or current_iso <= max_attr else max_attr
    input_box.click()
    input_box.press("Control+A")
    input_box.press("Delete")
    input_box.fill(fill_value)
    assert input_box.input_value() == fill_value
    page.wait_for_timeout(delay)  # Explicit delay
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"action\"]").fill(f"action_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    try:
        page.get_by_text("SUBMIT REVIEW").click()
    except Exception as e:
        logger.info(f"{e}")
        page.get_by_text("SAVE").click()
    page.wait_for_timeout(10000)  # Explicit delay

    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def next_5_days_strings():
    now = datetime.now()
    return [
        (now + timedelta(days=i)).strftime("%m/%d/%Y %H:%M")
        for i in range(1, 6)  # next 1..5 days
    ]


def enroll_subject_with_expiry_date(page, subject, group, organization, index, delay):
    logger.info("Navigating to Identify & Enroll page")
    logger.info(f"Enrolling subject: {subject}")
    page.get_by_text("Identify & Enroll").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay

    identify_enroll_locator = page.locator("xpath=(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]")
    identify_enroll_locator.click()
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        # print(text)
        logger.info("Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.info(f"Add Details text is not visible: {e}")
        identify_enroll_locator = page.locator("div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)")
        identify_enroll_locator.click()
        page.wait_for_timeout(delay)  # Explicit delay

    page.screenshot(path=f"screenshots/_8_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay

    dates = next_5_days_strings()
    # print(f"dates: {dates}")

    page.locator("//input[@id=\"expirationDateInputEl\"]").fill(dates[index])
    page.get_by_title("Close the picker").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"basis\"]").select_option("number:3")
    page.wait_for_timeout(delay)  # Explicit delay
    page.wait_for_timeout(delay)  # Explicit delay
    internal_group, spinbutton_value = group
    page.wait_for_timeout(delay)  # Explicit delay

    select = page.locator('select[name="internal_group"]')
    select.wait_for(state="visible")

    # Get all option texts and values
    option_texts = select.locator('option').all_text_contents()
    option_values = select.locator('option').evaluate_all('els => els.map(e => e.value)')

    needle = internal_group
    match_index = next(
        (i for i, t in enumerate(option_texts) if needle.lower() in (t or "").lower()),
        None
    )
    if match_index is None:
        raise Exception(f'No option contains "{needle}"')

    exact_label = option_texts[match_index].strip()
    exact_value = option_values[match_index]

    if exact_value:
        select.select_option(value=exact_value)
    else:
        select.select_option(label=exact_label)

    logger.info(f'Selected: label="{exact_label}", value="{exact_value}"')

    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SELECT", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(organization).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").fill(f"store_{internal_group.split(' ')[0].lower()}_ex_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"enrollmentNumber\"]").fill(f"enroll_{internal_group.split(' ')[0].lower()}_ex_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("spinbutton").fill(spinbutton_value)
    page.wait_for_timeout(delay)  # Explicit delay

    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
    # Locate by placeholder and fill
    page.get_by_placeholder("mm/dd/yyyy HH:mm").fill(current_time)
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("input[name=\"action\"]").fill(f"action_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SUBMIT REVIEW").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def select_expiry_date_range(page, sd, ed, delay):
    result = []
    expiration_date_start_checkbox = page.locator("//input[@ng-model='userSelectedStartExpirationDate']")
    if expiration_date_start_checkbox.is_visible():
        expiration_date_start_checkbox.click()
        logger.info("Clicked on start expiration date checkbox")
        page.wait_for_timeout(delay)
        logger.info(f"Selected ex start date: {sd.day}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)
    page.evaluate("document.body.style.zoom = '0.9'")
    page.wait_for_timeout(delay)
    # page.locator("#userSelectedEndExpirationDateEl").check()
    expiration_date_end_checkbox = page.locator("//input[@ng-model='userSelectedEndExpirationDate']")
    if expiration_date_end_checkbox.is_visible():
        expiration_date_end_checkbox.click()
        logger.info("Clicked on end expiration date checkbox")
        page.wait_for_timeout(delay)
        page.locator("#endExpirationDateField").click()
        pick_end_date_in_bootstrap_datetimepicker(page, "#endExpirationDateField", target=ed, delay=delay)
        page.wait_for_timeout(delay)
        logger.info(f"Selected ex end date: {ed.day}")
        # logger.info("Selected date:", enrollment_search_end_date.day)
        # page.get_by_role("cell", name="23").click()
        result.append(True)
    else:
        result.append(False)
    return result


def select_enrollment_date_range(page, delay):
    result = []
    sd = date.today() - timedelta(days=2)
    enrollment_date_start_checkbox = page.locator("//input[@ng-model='userSelectedStartEnrollDate']")
    if enrollment_date_start_checkbox.is_visible():
        enrollment_date_start_checkbox.click()
        logger.info("Clicked on start enrollment date checkbox")
        page.wait_for_timeout(delay)
        # page.locator("##startEnrollDateField").click()
        # pick_start_date_in_bootstrap_datetimepicker(page, "##startEnrollDateField", target=sd)
        # page.wait_for_timeout(3000)
        # logger.info(f"Selected start date: ")
        # logger.info("Selected date:", enrollment_search_start_date.day)
        # page.get_by_role("cell", name="17").click()
        page.wait_for_timeout(delay)
        # page.locator("#startEnrollDateField").click()
        pick_enrollment_start_date_in_bootstrap_datetimepicker(page, "#startEnrollDateField", target=sd)
        page.wait_for_timeout(delay)
        logger.info(f"Selected start date: {sd}")
        page.get_by_title("Close the picker").click()
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)
    # page.evaluate("document.body.style.zoom = '0.9'")
    # page.wait_for_timeout(1000)
    # page.locator("#userSelectedEndExpirationDateEl").check()
    page.wait_for_timeout(delay)
    enrollment_date_end_checkbox = page.locator("//input[@ng-model='userSelectedEndEnrollDate']")
    if enrollment_date_end_checkbox.is_visible():
        enrollment_date_end_checkbox.click()
        logger.info("Clicked on end enrollment date checkbox")
        page.wait_for_timeout(delay)
        # page.locator("#endEnrollDateField").click()
        # pick_end_date_in_bootstrap_datetimepicker(page, "#endEnrollDateField", target=ed)
        # page.wait_for_timeout(3000)
        # logger.info(f"Selected end date: ")
        # logger.info("Selected date:", enrollment_search_end_date.day)
        # page.get_by_role("cell", name="23").click()
        result.append(True)
    else:
        result.append(False)
    return result


def select_org_hierarchy_for_enrollment_search(page, organization, delay):
    logger.info("Selecting region")
    page.get_by_text("Org/Hierarchy Selection").click()
    page.wait_for_timeout(delay)  # Explicit delay
    regions = page.locator("//div[@ng-click=\"saveRegionSelection(this)\"]").all()
    for i, region in enumerate(regions):
        if region.inner_text() == organization:
            region.click()
    logger.info(f"Selected region: {organization}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay


def verify_selected_region_in_search_criteria_at_top(page, organization, delay):
    result = []
    region_criteria = page.locator("//div[@ng-bind=\"('Region' | i18n)+': '+(regionSelected.name)\"]")
    page.wait_for_timeout(delay)
    if region_criteria.is_visible():
        result.append(True)
        logger.info(f"Region criteria visible at top")
    else:
        result.append(False)
        logger.info("Region criteria not visible at top")
    page.wait_for_timeout(delay)
    if organization in region_criteria.inner_text():
        result.append(True)
        logger.info(f"Selected Region name visible at top: {region_criteria.inner_text()}")
    else:
        result.append(False)
        logger.info("Selected Region name not visible at top..")
    page.wait_for_timeout(delay)
    remove_region_criteria_button = page.locator("//div[@ng-click=\"removeRegionIdFromSearch( )\"]")
    if remove_region_criteria_button.is_visible():
        result.append(True)
        logger.info("Remove region criteria button is visible")
    else:
        result.append(False)
        logger.info("Remove region criteria button is not visible")
    page.wait_for_timeout(delay)
    return result


def verify_selected_region_in_enrollment_list(page, organization, delay):
    result = []
    page.wait_for_timeout(delay)
    enrollment_region_name = page.locator("//div[@ng-bind=\"enrollment.regionName\"]").all()
    for region_name in enrollment_region_name:
        if region_name.inner_text() == organization:
            result.append(True)
        else:
            result.append(False)
    return result


def verify_expiry_enrollments(page, sd, ed, delay):
    result = []
    expiry_on_label = page.locator("//div[@ng-bind=\"'TEXT-EXPIRES-ON' | i18n\"]").all()
    for i, label in enumerate(expiry_on_label):
        # logger.info(f"{label.inner_text()}")
        if label.inner_text() == "EXPIRE DATE":
            logger.info("Expire Date label is displayed.")
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)
    expire_date = page.locator("//div[@ng-bind=\"::(enrollment.expiration | userAbsTime:timezoneID)\"]").all()
    ex_date = []
    for j, d in enumerate(expire_date):
        logger.info(f"Expire On Date: {d.inner_text()}")
        ex = d.inner_text().split(' ')
        # ex = ex.split(',')
        ex_dt = ex[1]
        ex_mn = ex[0]
        dt = ex_mn + " " + ex_dt
        ex_date.append(dt)
        if ex_mn == sd.month or ed.month:
            result.append(True)
            logger.info(f"Expiry month is {ex_mn}")
        else:
            result.append(False)
            logger.info(f"Expiry month is not as expected: {ex_mn}")
        page.wait_for_timeout(delay)
        if (ex_dt <= str(ed.day)) or (ex_dt >= str(sd.day)):
            result.append(True)
            logger.info(f"Expiry date is within range: {ex_dt}")
        else:
            result.append(False)
            logger.info(f"Expiry date is not within range: {ex_dt}")
        page.wait_for_timeout(delay)
        # logger.info(f"Expire month date: {ex_date}")
    logger.info(f"All expiry dates : {ex_date}")
    return result


# def verify_enrolled_date_enrollments(page, sd, ed):
#     result = []
#
#     enrolled_on = page.locator("//div[@ng-bind=\"::('Enrolled On' | i18n)\"]")
#     if enrolled_on.count() > 0:
#         logger.info("Enrolled On label is displayed")
#         result.append(True)
#     else:
#         logger.error("Enrolled On label is NOT displayed")
#         result.append(False)
#
#     enrolled_dates = page.locator(
#         "//span[@ng-bind=\"::( enrollment.enrolled | userAbsTime:timezoneID )\"]"
#     ).all()
#
#     for d in enrolled_dates:
#         text = d.inner_text()
#         logger.info(f"Enrolled Date: {text}")
#
#         enrolled_dt = datetime.strptime(text, "%b %d, %Y %I:%M %p").date()
#
#         if sd <= enrolled_dt <= ed:
#             logger.info("Enrolled date is within range")
#             result.append(True)
#         else:
#             logger.error("Enrolled date is OUTSIDE range")
#             result.append(False)
#
#     return result


# def verify_enrollment_number_in_search_criteria_at_top1(page, en):
#     result = []
#
#     criteria = page.locator("//div[contains(text(),'Search Criteria')]")
#     criteria.wait_for(state="visible", timeout=10000)
#     result.append(True)
#
#     value = page.locator(
#         "//div[contains(text(),'Search Criteria')]//following-sibling::div[2]"
#     ).inner_text().strip()
#
#     sv1 = f"ENROLLMENT NUMBER: {en}"
#     sv2 = f"ENROLLMENT NUMBER: {en.lower()}"
#
#     if value == sv1 or value == sv2:
#         logger.info(f"Search Criteria: {value}")
#         result.append(True)
#     else:
#         logger.error("Enrollment number mismatch in Search Criteria")
#         result.append(False)
#
#     remove_btn = page.locator(
#         "//div[contains(text(),'Search Criteria')]//following-sibling::div[2]//i"
#     )
#     result.append(remove_btn.is_visible())
#
#     return result
#

def verify_enrollment_dates_on_enrollments(page, sd, ed, delay):
    result = []
    sd1 = sd - timedelta(days=2)
    enrolled_on_label = page.locator("//div[@ng-bind=\"::('Enrolled On' | i18n)\"]").all()
    for i, label in enumerate(enrolled_on_label):
        # logger.info(f"{label.inner_text()}")
        if label.inner_text() == "ENROLLED ON":
            logger.info("ENROLLED ON label is displayed.")
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)
    enrolled_on_date = page.locator("//div//span[@ng-bind=\"::( enrollment.enrolled | userAbsTime:timezoneID )\"]").all()
    ex_date = []
    for j, d in enumerate(enrolled_on_date):
        logger.info(f"Enrolled On Date: {d.inner_text()}")
        ex = d.inner_text().split(' ')
        # ex = ex.split(',')
        # logger.info(f"ex: {ex}")
        ex_dt = ex[1]
        ex_mn = ex[0]
        dt = ex_mn + " " + ex_dt
        ex_date.append(dt)
        if ex_mn == sd1.month or ed.month:
            result.append(True)
            logger.info(f"Enrolled month is {ex_mn}")
        else:
            result.append(False)
            logger.info(f"Enrolled month is not as expected: {ex_mn}")
        page.wait_for_timeout(delay)
        ex_dt = ex_dt.split(",")
        ex_dt = ex_dt[0]
        if (ex_dt <= str(ed.day)) or (ex_dt >= str(sd1.day)):
            result.append(True)
            logger.info(f"Enrolled on date is within range: {ex_dt}")
        else:
            result.append(False)
            logger.info(f"Enrolled on date is not within range: {ex_dt}")
        page.wait_for_timeout(delay)
        # logger.info(f"Expire month date: {ex_date}")
    logger.info(f"All enrolled on dates : {ex_date}")
    return result


def verify_expiration_date_in_search_criteria_at_top(page, sd, ed, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria = page.locator("//div[contains(text(),'Search Criteria')]")
    if search_criteria.is_visible():
        logger.info(f"{search_criteria.inner_text()} is visible")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria_value = page.locator("//div[@ng-show=\"startExpirationDateToDisplay && endExpirationDateToDisplay\"]//div[1]").inner_text()
    logger.info(f"Expiration date range: {search_criteria_value}")

    sd_date_str = str(sd)
    converted_sd = datetime.strptime(sd_date_str, "%Y-%m-%d").strftime("%m/%d/%Y")
    logger.info(f"Expiry Start date: {converted_sd}")

    ed_date_str = str(ed)
    converted_ed = datetime.strptime(ed_date_str, "%Y-%m-%d").strftime("%m/%d/%Y")
    logger.info(f"Expiry End date: {converted_ed}")
    page.wait_for_timeout(delay)  # Explicit delay
    date_range_selected = ("Expiration: " + converted_sd + " to (optional) ")
    if date_range_selected in search_criteria_value:
        result.append(True)
        logger.info(F"Expiration criteria is same as entered..")
    else:
        result.append(False)
        logger.info(f"Expiration: " + converted_sd + " to (optional) " + converted_ed)
        logger.info("Expiration criteria is not same as entered..")
    page.wait_for_timeout(delay)  # Explicit delay
    remove_criteria = page.locator("//div[@ng-show=\"startExpirationDateToDisplay && endExpirationDateToDisplay\"]//div[2]")
    if remove_criteria.is_visible():
        logger.info("Remove criteria button is visible.")
        result.append(True)
    else:
        logger.info("Remove criteria button is not visible.")
        result.append(False)
    return result


# def verify_enrolled_date_in_search_criteria_at_top(page, sd, ed):
#     result = []
#
#     search_criteria_value = page.locator(
#         "//div[@ng-show=\"startEnrollDateToDisplay && endEnrollDateToDisplay\"]//div[1]"
#     ).inner_text()
#
#     logger.info(f"Enrolled date range: {search_criteria_value}")
#
#     ui_sd = sd.strftime("%m/%d/%Y")
#     ui_ed = ed.strftime("%m/%d/%Y")
#
#     if "Enrolled:" in search_criteria_value and ui_sd in search_criteria_value:
#         result.append(True)
#     else:
#         logger.error("Enrolled criteria is not same as entered")
#         result.append(False)
#
#     remove_btn = page.locator(
#         "//div[@ng-show='startEnrollDateToDisplay && endEnrollDateToDisplay']//div[2]"
#     )
#     result.append(remove_btn.is_visible())
#
#     return result


# def select_start_and_end_enrolled_date_checkboxes(page):
#     try:
#         start_enroll_chk = page.locator("#userSelectedStartEnrollmentDateEl")
#         end_enroll_chk = page.locator("#userSelectedEndEnrollmentDateEl")
#
#         start_enroll_chk.wait_for(state="visible", timeout=5000)
#         end_enroll_chk.wait_for(state="visible", timeout=5000)
#
#         if not start_enroll_chk.is_checked():
#             start_enroll_chk.check()
#             logger.info("Start Enroll Date checkbox selected")
#
#         if not end_enroll_chk.is_checked():
#             end_enroll_chk.check()
#             logger.info("End Enroll Date checkbox selected")
#
#         return True
#
#     except Exception as e:
#         logger.error(f"Failed to select Enrolled Date checkboxes: {e}")
#         page.screenshot(path="enrolled_date_checkbox.png", full_page=True)
#         return False


def verify_enrollment_date_in_search_criteria_at_top(page, sd, ed, delay):
    result = []
    date_yes = sd - timedelta(days=2)
    page.wait_for_timeout(delay)  # Explicit delay
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria = page.locator("//div[contains(text(),'Search Criteria')]")
    if search_criteria.is_visible():
        logger.info(f"{search_criteria.inner_text()} is visible")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria_value = page.locator("//div[@ng-show=\"startEnrollDateToDisplay && endEnrollDateToDisplay\"]//div[1]").inner_text()
    logger.info(f"Enrollment date range: {search_criteria_value}")

    sd_date_str = str(date_yes)
    converted_sd = datetime.strptime(sd_date_str, "%Y-%m-%d").strftime("%m/%d/%Y")
    logger.info(f"Enrollment Start date: {converted_sd}")

    ed_date_str = str(ed)
    converted_ed = datetime.strptime(ed_date_str, "%Y-%m-%d").strftime("%m/%d/%Y")
    logger.info(f"Enrollment End date: {converted_ed}")
    page.wait_for_timeout(delay)  # Explicit delay
    if search_criteria_value == ("Enrolled: " + converted_sd + " 12:00 AM to (optional) " + converted_ed) + " 11:59 PM":
        result.append(True)
        logger.info(F"Enrollment date criteria is same as entered..")
    else:
        result.append(False)
        logger.info(f"Enrolled: " + converted_sd + " 12:00 AM to (optional) " + converted_ed + " 11:59 PM")
        logger.info("Enrollment date criteria is not same as entered..")
    page.wait_for_timeout(delay)  # Explicit delay
    remove_criteria = page.locator("//div[@ng-show=\"startEnrollDateToDisplay && endEnrollDateToDisplay\"]//div[2]")
    if remove_criteria.is_visible():
        logger.info("Remove criteria button is visible.")
        result.append(True)
    else:
        logger.info("Remove criteria button is not visible.")
        result.append(False)
    return result


def verify_sort_by_enrollment_number_descending(page, delay):  # for expired enrollments
    result = []
    page.wait_for_timeout(delay)
    sort_key = page.locator(
        "//div[@class=\"current-filter-heading-band\"]//div[contains(text(),'Sort Key')]").inner_text()
    if "ENROLLMENT NUMBER" in sort_key:
        logger.info(f"{sort_key}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    remove_sort = page.locator("//div[@tiptitle='Remove Sort']")
    if remove_sort.is_visible():
        logger.info("Remove sort is visible")
        result.append(True)
    else:
        logger.info("Remove sort is not visible")
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    enrollment_displayed = page.locator("//div[@ng-show=\"enrollments.length\"]")
    if enrollment_displayed.is_visible():
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value_label = page.locator("//span[@ng-bind=\"'TEXT-SORT-VALUE' | i18n\"]").all()
    for sort in sort_value_label:
        if sort.is_visible():
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value = page.locator("//span[@ng-bind=\"enrollment.metaData[ currentSearchSortObj.internal_name ]\"]").all()
    sort = []
    for value in sort_value:
        if value.is_visible():
            result.append(True)
            sort.append(value.inner_text())
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    loc_enrollment_number = page.locator(
        "//li[@ng-show=\"enrollments\"]//div[@ng-bind=\"enrollment.shortDesc[0].value\"]").all()
    enrollment_numbers = []
    for i, number in enumerate(loc_enrollment_number):
        lo_en = number.inner_text().split(' ')
        en = lo_en[1]
        # has_soe = "soe" in en.lower()
        # if has_soe:
        enrollment_numbers.append(en)
        #     result.append(True)
        # else:
        #     result.append(False)
    logger.info(f"Enrollment numbers: {enrollment_numbers}")
    # logger.info(f"Sort: {sort}")
    if sort == enrollment_numbers:
        result.append(True)
        logger.info("Sort values and enrollment numbers are same")
    else:
        result.append(False)
        logger.info("Sort values and enrollment numbers are not same")
    page.wait_for_timeout(delay)  # Explicit delay
    # asc = sorted(enrollment_numbers, key=natural_key)
    desc = sorted(enrollment_numbers, key=str.lower, reverse=True)
    page.wait_for_timeout(delay)  # Explicit delay
    # logger.info("Ascending:", asc)
    logger.info(f"Descending:  {desc}")
    if enrollment_numbers == desc:
        result.append(True)
        logger.info(f"Enrollments are sorted by Descending order:{desc}")
    else:
        result.append(False)
        logger.info(f"Enrollments are not sorted by Descending order: {desc}")
    return result


def verify_enrollment_dates_with_sort_by_enrollment_number_descending(page, delay):
    result = []
    page.wait_for_timeout(delay)
    sort_key = page.locator(
        "//div[@class=\"current-filter-heading-band\"]//div[contains(text(),'Sort Key')]").inner_text()
    if "ENROLLMENT NUMBER" in sort_key:
        logger.info(f"{sort_key}")
        result.append(True)
    else:
        result.append(False)
    remove_sort = page.locator("//div[@tiptitle='Remove Sort']")
    if remove_sort.is_visible():
        logger.info("Remove sort is visible")
        result.append(True)
    else:
        logger.info("Remove sort is not visible")
        result.append(False)
    enrollment_displayed = page.locator("//div[@ng-show=\"enrollments.length\"]")
    if enrollment_displayed.is_visible():
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value_label = page.locator("//span[@ng-bind=\"'TEXT-SORT-VALUE' | i18n\"]").all()
    for sort in sort_value_label:
        if sort.is_visible():
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value = page.locator("//span[@ng-bind=\"enrollment.metaData[ currentSearchSortObj.internal_name ]\"]").all()
    sort = []
    for value in sort_value:
        if value.is_visible():
            result.append(True)
            sort.append(value.inner_text())
        else:
            result.append(False)

    page.wait_for_timeout(delay)  # Explicit delay
    # asc = sorted(enrollment_numbers, key=natural_key)
    desc = sorted(sort, key=str.lower, reverse=True)
    # desc = sorted(sort, key=natural_key, reverse=True)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info(f"Sort Value:  {sort}")
    # logger.info("Ascending:", asc)
    logger.info(f"Descending:  {desc}")
    if sort == desc:
        result.append(True)
        logger.info(f"Enrollments are sorted by Descending order:{desc}")
    else:
        result.append(False)
        logger.info(f"Enrollments are not sorted by Descending order: {desc}")
    return result


def verify_sort_by_location_store_descending(page, delay):
    result = []
    page.wait_for_timeout(delay)
    sort_key = page.locator(
        "//div[@class=\"current-filter-heading-band\"]//div[contains(text(),'Sort Key')]").inner_text()
    if "LOCATION/STORE" in sort_key:
        logger.info(f"{sort_key}")
        result.append(True)
    else:
        result.append(False)
    remove_sort = page.locator("//div[@tiptitle='Remove Sort']")
    if remove_sort.is_visible():
        logger.info("Remove sort is visible")
        result.append(True)
    else:
        logger.info("Remove sort is not visible")
        result.append(False)
    enrollment_displayed = page.locator("//div[@ng-show=\"enrollments.length\"]")
    if enrollment_displayed.is_visible():
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value_label = page.locator("//span[@ng-bind=\"'TEXT-SORT-VALUE' | i18n\"]").all()
    for sort in sort_value_label:
        if sort.is_visible():
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value = page.locator("//span[@ng-bind=\"enrollment.metaData[ currentSearchSortObj.internal_name ]\"]").all()
    sort = []
    for value in sort_value:
        if value.is_visible():
            result.append(True)
            sort.append(value.inner_text())
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    loc_enrollment_number = page.locator(
        "//li[@ng-show=\"enrollments\"]//div[@ng-bind=\"enrollment.shortDesc[0].value\"]").all()
    location_stores = []
    for i, number in enumerate(loc_enrollment_number):
        lo_en = number.inner_text().split(' ')
        lo = lo_en[0]
        # has_soe = "soe" in en.lower()
        # if has_soe:
        location_stores.append(lo)
        #     result.append(True)
        # else:
        #     result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info(f"Location Stores: {location_stores}")
    if sort == location_stores:
        result.append(True)
        logger.info("Sort values and location stores are same")
    else:
        result.append(False)
        logger.info("Sort values and location stores are not same")
    page.wait_for_timeout(delay)  # Explicit delay
    # asc = sorted(location_stores, key=natural_key)
    desc = sorted(location_stores, key=str.lower, reverse=True)
    page.wait_for_timeout(delay)  # Explicit delay
    # logger.info("Ascending:", asc)
    logger.info(f"Descending:  {desc}")
    if location_stores == desc:
        result.append(True)
        logger.info(f"Enrollments are sorted by Descending order:{desc}")
    else:
        result.append(False)
        logger.info(f"Enrollments are not sorted by Descending order: {desc}")
    return result


def verify_enrollment_dates_with_sort_by_location_store_descending(page, delay):
    result = []
    page.wait_for_timeout(delay)
    sort_key = page.locator(
        "//div[@class=\"current-filter-heading-band\"]//div[contains(text(),'Sort Key')]").inner_text()
    if "LOCATION/STORE" in sort_key:
        logger.info(f"{sort_key}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    remove_sort = page.locator("//div[@tiptitle='Remove Sort']")
    if remove_sort.is_visible():
        logger.info("Remove sort is visible")
        result.append(True)
    else:
        logger.info("Remove sort is not visible")
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    enrollment_displayed = page.locator("//div[@ng-show=\"enrollments.length\"]")
    if enrollment_displayed.is_visible():
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value_label = page.locator("//span[@ng-bind=\"'TEXT-SORT-VALUE' | i18n\"]").all()
    for sort in sort_value_label:
        if sort.is_visible():
            result.append(True)
        else:
            result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    sort_value = page.locator("//span[@ng-bind=\"enrollment.metaData[ currentSearchSortObj.internal_name ]\"]").all()
    sort = []
    for value in sort_value:
        if value.is_visible():
            result.append(True)
            sort.append(value.inner_text())
        else:
            result.append(False)

    page.wait_for_timeout(delay)  # Explicit delay
    # asc = sorted(enrollment_numbers, key=natural_key)
    desc = sorted(sort, key=str.lower, reverse=True)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info(f"Sort Value:  {sort}")
    # logger.info("Ascending:", asc)
    logger.info(f"Descending:  {desc}")
    if sort == desc:
        result.append(True)
        logger.info(f"Enrollments are sorted by Descending order:{desc}")
    else:
        result.append(False)
        logger.info(f"Enrollments are not sorted by Descending order: {desc}")
    return result


def verify_enrollment_number_in_search_criteria_at_top(page, en, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria = page.locator("//div[contains(text(),'Search Criteria')]")
    if search_criteria.is_visible():
        logger.info(f"{search_criteria.inner_text()} is visible")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria_value = page.locator(
        "//div[contains(text(),'Search Criteria')]//following-sibling::div[2]").inner_text()
    sv1 = "ENROLLMENT NUMBER: " + en
    sv2 = "ENROLLMENT NUMBER: " + en.lower()
    if search_criteria_value == sv1 or search_criteria_value == sv2:
        logger.info(f"Search Criteria:{search_criteria_value}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    remove_criteria = page.locator("//div[contains(text(),'Search Criteria')]//following-sibling::div[2]//div//i")
    if remove_criteria.is_visible():
        logger.info("Remove criteria button is visible.")
        result.append(True)
    else:
        logger.info("Remove criteria button is not visible.")
        result.append(False)
    return result


def verify_enrollment_number_in_enrollment_list(page, en, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay)
    page.wait_for_timeout(delay)
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]')
    count = menus.count()
    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay)
        details_button.nth(i).click()
        page.wait_for_timeout(delay)
        locator = page.locator("//td[contains(text(),'ENROLLMENT NUMBER')]//following-sibling::td[@ng-if=\"field.type !== 'textarea'\"]")
        location_store = locator.inner_text()
        if en in location_store or location_store.lower():
            result.append(True)
            logger.info(f"ENROLLMENT NUMBER: {locator.inner_text()}")
        else:
            result.append(False)
        page.wait_for_timeout(delay)
        page.locator('//p[text()="Enrollment - Details"]//parent::div//child::div').click()
        page.wait_for_timeout(delay_2_second)
    return result


def verify_location_store_in_search_criteria_at_top(page, lo, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria = page.locator("//div[contains(text(),'Search Criteria')]")
    if search_criteria.is_visible():
        logger.info(f"{search_criteria.inner_text()} is visible")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria_value = page.locator(
        "//div[contains(text(),'Search Criteria')]//following-sibling::div[1]").inner_text()
    sv1 = "LOCATION/STORE: " + lo
    sv2 = "LOCATION/STORE: " + lo.lower()
    if search_criteria_value == sv1 or sv2:
        logger.info(f"Search Criteria:{search_criteria_value}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    remove_criteria = page.locator("//div[contains(text(),'Search Criteria')]//following-sibling::div[1]//div//i")
    if remove_criteria.is_visible():
        logger.info("Remove criteria button is visible.")
        result.append(True)
    else:
        logger.info("Remove criteria button is not visible.")
        result.append(False)
    return result


def verify_location_store_in_enrollment_list(page, lo, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay_1_second)
    page.wait_for_timeout(delay_5_second)
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]')
    count = menus.count()
    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay_2_second)
        details_button.nth(i).click()
        page.wait_for_timeout(delay_2_second)
        locator = page.locator("//td[contains(text(),'LOCATION/STORE')]//following-sibling::td[@ng-if=\"field.type !== 'textarea'\"]")
        location_store = locator.inner_text()
        if lo in location_store or location_store.lower():
            result.append(True)
            logger.info(f"LOCATION/STORE: {locator.inner_text()}")
        else:
            result.append(False)
        page.wait_for_timeout(delay_2_second)
        page.locator('//p[text()="Enrollment - Details"]//parent::div//child::div').click()
        page.wait_for_timeout(delay_2_second)
    return result


def verify_enrollment_basis_in_search_criteria_at_top(page, en_basis, delay):
    result = []
    page.wait_for_timeout(delay)  # Explicit delay
    search_criteria = page.locator("//div[contains(text(),'Search Criteria')]")
    if search_criteria.is_visible():
        logger.info(f"{search_criteria.inner_text()} is visible")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    en_basis_in_search_criteria = page.locator("//div[@ng-show=\"enrollmentBasis\"]//div[1]").inner_text()

    if en_basis in en_basis_in_search_criteria:
        logger.info(f"Search Criteria has:{en_basis_in_search_criteria}")
        result.append(True)
    else:
        result.append(False)
    page.wait_for_timeout(delay)  # Explicit delay
    remove_basis_criteria = page.locator("//div[@ng-show=\"enrollmentBasis\"]//div[2]")
    if remove_basis_criteria.is_visible():
        logger.info("Remove basis criteria button is visible.")
        result.append(True)
    else:
        logger.info("Remove basis criteria button is not visible.")
        result.append(False)
    return result


def verify_enrollment_basis_in_enrollment_list(page, en_basis, delay):
    result = []
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay)
    page.wait_for_timeout(delay)
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]')
    count = menus.count()
    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay)
        details_button.nth(i).click()
        page.wait_for_timeout(delay)
        locator = page.locator('//td[@ng-if="!editingMode && enrollment.basis"]')
        if en_basis in locator.inner_text():
            result.append(True)
            logger.info(f"Enrollment basis: {locator.inner_text()}")
        else:
            result.append(False)
        page.wait_for_timeout(delay)
        page.locator('//p[text()="Enrollment - Details"]//parent::div//child::div').click()
        page.wait_for_timeout(delay)
    return result


def filter_pending_review(page, delay):
    page.locator("a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Pending Review").click()
    page.wait_for_timeout(delay)  # Explicit delay


def filter_enabled(page, delay):
    page.locator("a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Enabled").click()
    page.wait_for_timeout(delay)  # Explicit delay


def filter_disabled(page, delay):
    page.locator("a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Disabled").click()
    page.wait_for_timeout(delay)  # Explicit delay


def approve_enrollments(page, delay):
    while not page.get_by_text(
            "There are no enrollments matching the current search criteria or current filter.").is_visible():
        checkboxes = page.locator(
            "li > .right-margin-menu > .right-menu-checkbox-container > .icheckbox_polaris > .iCheck-helper")
        page.wait_for_timeout(delay)  # Explicit delay
        for i in range(checkboxes.count()):
            checkboxes.nth(i).click()
            page.wait_for_timeout(delay)  # Explicit delay
        page.locator("a").filter(has_text="Action").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_text("APPROVE Selected Enrollments").click()
        page.wait_for_timeout(delay)  # Explicit delay
        loadbutton = page.get_by_role("button", name="Load More")
        page.wait_for_timeout(delay)  # Explicit delay
        if loadbutton.is_visible():
            continue
        page.wait_for_timeout(delay)  # Explicit delay


def search_enrollment_group(page, eg, delay):
    page.locator("a").filter(has_text="Search").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Enrollment Group Selection").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="filter enrollment group list").fill(eg["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#enrollmentGroup-selection-menu").get_by_role("checkbox").check()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Search", exact=True).nth(2).click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_tags_to_events(page, eg, delay):
    checkboxes = page.locator("li > .event-row > .right-margin-menu > .right-menu-checkbox-container")
    page.wait_for_timeout(delay)  # Explicit delay
    for j in range(checkboxes.count()):
        checkboxes.nth(j).click()
        page.wait_for_timeout(delay)  # Brief delay to ensure click is registered
        if j == 5:
            break
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Edit Tags").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("menu").get_by_text("Unlinked Tags").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("div:nth-child(5) > .right-menu-checkbox-container").first.click()
    page.wait_for_timeout(delay)  # Explicit delay

    if eg["name"] == "abe":
        xpath = '//li[@ng-repeat="tag in tags | filter:filterModel"]/p[contains(text(),"assault")]/following-sibling::div/div'
        # page.locator("li:nth-child(2) > .right-margin-menu > .right-menu-checkbox-container").click()
        page.locator(xpath).click()
        page.wait_for_timeout(delay)  # Explicit delay
    elif eg["name"] in ["fraude", "vipe"]:
        xpath = '//li[@ng-repeat="tag in tags | filter:filterModel"]/p[contains(text(),"fraud")]/following-sibling::div/div'
        # page.locator("li:nth-child(3) > .right-margin-menu > .right-menu-checkbox-container").click()
        page.locator(xpath).click()
        page.wait_for_timeout(delay)  # Explicit delay
    elif eg["name"] == "pte":
        xpath = '//li[@ng-repeat="tag in tags | filter:filterModel"]/p[contains(text(),"push cart")]/following-sibling::div/div'
        # page.locator("li:nth-child(4) > .right-margin-menu > .right-menu-checkbox-container").click()
        page.locator(xpath).click()
        page.wait_for_timeout(delay)  # Explicit delay
    elif eg["name"] == "soe":
        xpath = '//li[@ng-repeat="tag in tags | filter:filterModel"]/p[contains(text(),"threat")]/following-sibling::div/div'
        # page.locator("li:nth-child(5) > .right-margin-menu > .right-menu-checkbox-container").click()
        page.locator(xpath).click()
        page.wait_for_timeout(delay)  # Explicit delay

    page.locator(
        "xpath=(//a[@class='btn dropdown-toggle pull-right toolbar-btn trigger-hide-search nav-pills-small'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Add Tag(s) to Selected Event(").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay


def set_search_date_and_time(page, delay):
    page.locator("#includeStartDateEl").check()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#startDateField").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Next Month").click()
    # Set the date
    # page.wait_for_timeout(delay)
    # page.get_by_role("cell", name=conftest.search_date.strftime("%B %Y Toggle Date and")).click()
    page.wait_for_timeout(delay)  # Explicit delay
    print("Search date success")
    # page.get_by_text(conftest.search_date.strftime("%b"), exact=True).click()
    # page.get_by_role('cell', name="5").first.click()
    print(f'date: {conftest.search_date.strftime("%#d")}')
    page.get_by_role('cell', name=f'{conftest.search_date.strftime("%#d")}').first.click()
    print("Search time success")
    page.wait_for_timeout(delay)  # Explicit delay
    try:
        page.get_by_role("cell", name=str(conftest.search_date.day)).nth(1).click()
    except:
        page.get_by_role("cell", name=str(conftest.search_date.day)).click()
    page.wait_for_timeout(delay)  # Explicit delay

    # Set the time
    page.get_by_title("Select Time").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Pick Hour").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("cell", name=conftest.search_time.strftime("%I")).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Pick Minute").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("cell", name=conftest.search_time.strftime("%M")).click()
    page.wait_for_timeout(delay)  # Explicit delay
    # page.get_by_role("button", name=conftest.search_time.strftime("%p")+" Toggle AM/PM").click()
    # toggle_am_pm = conftest.search_time.strftime("%p")
    if conftest.search_time.strftime("%p") == "AM":
        page.get_by_title("Toggle Period").click()
        page.get_by_title("Toggle Period").click()
    else:
        page.get_by_title("Toggle Period").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Close the picker").click()
    page.wait_for_timeout(delay)  # Explicit delay


def select_organization(page, organization, delay):
    logger.info("Selecting organization")
    page.get_by_text("Org/Hierarchy Selection").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(organization).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay


def crop_with_mouse(page, target_selector, start_offset=(40, 20), rect_size=(160, 200)):
    """
    Click-drags a rectangle across an image/crop area to simulate user cropping.
    - target_selector: CSS selector for the image/crop container.
    - start_offset: pixels from top-left of the element to start the drag.
    - end_offset: pixels from bottom-right of the element to end the drag
                  (use negative values to stay inside the element).
    """
    el = page.locator(target_selector).first
    el.wait_for(state="visible")

    # Get the element's bounding box in page coordinates
    box = el.bounding_box()
    if not box:
        raise RuntimeError("Could not compute bounding box for the element.")

    # Compute absolute coordinates on the page for the drag
    start_x = box["x"] + start_offset[0]
    start_y = box["y"] + start_offset[1]

    # Compute end (bottom-right of desired rectangle)
    end_x = start_x + rect_size[0]
    end_y = start_y + rect_size[1]

    # Ensure the element is in view
    el.scroll_into_view_if_needed()

    # Perform the mouse drag
    page.mouse.move(start_x, start_y)
    page.mouse.down()
    page.mouse.move(end_x, end_y, steps=20)  # steps for smoother drag
    page.mouse.up()

    # Return the rectangle that was drawn (page coordinates)
    print(f"x: {start_x}, y: {start_y}, width: {max(1, end_x - start_x)}, height: {max(1, end_y - start_y)}")


def submit_search(page, delay):
    logger.info("Submitting search")
    page.get_by_role("button", name="Submit Search").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.wait_for_selector("text=VISITOR SEARCH COMPLETE", state="visible")
    page.wait_for_timeout(delay)  # Explicit delay


def submit_search_for_incomplete(page, delay):
    logger.info("Submitting search")
    page.get_by_role("button", name="Submit Search").click()
    print('clicked on search btn.')
    page.wait_for_timeout(delay)  # Explicit delay


def perform_visitor_image_search(page, subject, index, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_11_vs_image_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay


def perform_visitor_image_meta_search(page, subject, index, organization, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    set_search_date_and_time(page, delay)
    select_organization(page, organization, delay)
    page.get_by_role("combobox").select_option("string:15")
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.screenshot(path=f"screenshots/_12_vs_image_meta_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay


def perform_vsj_image_meta_search(page, subject, index, organization, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    set_vsj_search_date_and_time(page, delay)
    select_organization(page, organization, delay)
    # page.get_by_role("combobox").select_option("string:15")
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.screenshot(path=f"screenshots/_12_vs_image_meta_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay


def enroll_mask_subject(page, subject, group, organization, delay):
    logger.info(f"Enrolling subject: {subject}")
    page.get_by_text("Identify & Enroll").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay

    identify_enroll_locator = page.locator("xpath=(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]")
    identify_enroll_locator.click()
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        logger.info(f"Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.info(f"Add Details text is not visible")
        identify_enroll_locator = page.locator("div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)")
        identify_enroll_locator.click()
        page.wait_for_timeout(delay)  # Explicit delay

    page.screenshot(path=f"screenshots/_14_subject_mask_uploaded.png")

    page.locator("select[name=\"basis\"]").select_option("number:3")
    page.wait_for_timeout(delay)  # Explicit delay

    internal_group, spinbutton_value = group
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"internal_group\"]").select_option(internal_group)
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SELECT", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(organization).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").fill(f"store_mask")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"enrollmentNumber\"]").fill(f"enroll_mask")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("spinbutton").fill(spinbutton_value)
    page.wait_for_timeout(delay)  # Explicit delay
    input_box = page.get_by_placeholder("mm/dd/yyyy HH:mm")
    current_iso = datetime.now().strftime("%Y-%m-%dT%H:%M")
    max_attr = input_box.get_attribute("max")
    fill_value = current_iso if not max_attr or current_iso <= max_attr else max_attr
    input_box.click()
    input_box.press("Control+A")
    input_box.press("Delete")
    input_box.fill(fill_value)
    assert input_box.input_value() == fill_value
    page.locator("input[name=\"action\"]").fill(f"action_mask")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SUBMIT REVIEW").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_face_and_note_to_subject(page, delay):
    page.get_by_text("Enrollments").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("right-margin-menu > div:nth-child(2)").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(conftest.FACE)
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-click='skipCropping(); $event.stopPropagation();'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-click='addPhoto(); $event.stopPropagation();'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-mousedown='closeCurrentPanel(panel); $event.stopPropagation();'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("right-margin-menu > div:nth-child(3)").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    # page.locator(".right-margin-extended-button > .fa").first.click()
    # page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#Notes").get_by_text("Action", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Add A New Note To Person").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(conftest.NOTE)
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-click='skipCropping(); $event.stopPropagation();'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-click='addImage(); $event.stopPropagation();'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("button", name="  Add Location").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Find Location").fill("bengakuru")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Kempegowda International").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("button", name="Kempegowda International").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@ng-click='closeCurrentPanel(panel);'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//a[normalize-space()='Save'])[1]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[3]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".close-button-large").first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def pick_enrollment_start_date_in_bootstrap_datetimepicker(page, input_selector, target):
    # 1) Open the calendar
    page.locator(input_selector).click()
    page.wait_for_timeout(delay_2_second)
    # 2) Navigate month/year (selectors may differ per theme/markup)
    # Typical eonasdan structure has .bootstrap-datetimepicker-widget with nav buttons:
    while True:
        current_month = page.locator(".bootstrap-datetimepicker-widget .datepicker-days .picker-switch").text_content()
        # e.g., "December 2025"
        if current_month and current_month.strip().lower() == target.strftime("%B %Y").lower():
            break
        # Choose next or previous
        # Next month button often has '.next' or a button in the header; adjust to your DOM

        # Then perform the click
        if page.locator(".bootstrap-datetimepicker-widget .datepicker-days .next").is_visible():
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days .next").click()
        else:
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days .prev").click()

    # 3) Click the day cell by visible text
    d = page.locator(f".bootstrap-datetimepicker-widget .day:text-is('{target.day}')").all()
    # logger.info(f"{len(d)}")
    if len(d) > 1:
        d[0].click()
    else:
        page.locator(f".bootstrap-datetimepicker-widget .day:text-is('{target.day}')").click()

    # 4) If time is enabled, select time similarly (hours/minutes views), or press Enter/close
    # page.keyboard.press("Enter")


def pick_end_date_in_bootstrap_datetimepicker(page, input_selector, target, delay):
    # 1) Open the calendar
    page.locator(input_selector).click()
    page.wait_for_timeout(delay)
    # 2) Navigate month/year (selectors may differ per theme/markup)
    # Typical eonasdan structure has .bootstrap-datetimepicker-widget with nav buttons:
    while True:
        current_month = page.locator(".bootstrap-datetimepicker-widget .datepicker-days .picker-switch").text_content()
        # e.g., "December 2025"
        if current_month and current_month.strip().lower() == target.strftime("%B %Y").lower():
            break
        # Choose next or previous
        # Next month button often has '.next' or a button in the header; adjust to your DOM

        # Then perform the click
        if page.locator(".bootstrap-datetimepicker-widget .datepicker-days .next").is_visible():
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days .next").click()
        else:
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days .prev").click()
    page.wait_for_timeout(delay)
    # 3) Click the day cell by visible text

    d = page.locator(f".bootstrap-datetimepicker-widget .day:text-is('{target.day}')").all()
    # logger.info(f"{len(d)}")
    if len(d) > 1:
        d[1].click()
    else:
        page.locator(f".bootstrap-datetimepicker-widget .day:text-is('{target.day}')").click()

    # 4) If time is enabled, select time similarly (hours/minutes views), or press Enter/close
    # page.keyboard.press("Enter")


def detect_face(page, image_file, delay):
    logger.info(f"Detect Face Subject: {image_file}")
    page.get_by_text("Detect Faces", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name='image']").first.set_input_files(image_file)
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_17_detect_face_subject_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".select-areas-background-area").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("i:nth-child(2)").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    with page.expect_download() as download_info:
        page.locator("right-margin-menu div").first.click()
        page.wait_for_timeout(delay)  # Explicit delay
    download = download_info.value
    download.save_as('screenshots/detect_face/' + download.suggested_filename)
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".close-button-large").first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def configure_notifier(page, delay):
    page.get_by_text("Notifier", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#notifier-settings-button").nth(1).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Collapse all").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Expand all").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Select all", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Unselect all").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Search").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Search").fill("mxeast")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#tree-root div").filter(has_text="Kroger MX East - MXEAST").locator("i").nth(1).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("link", name="Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_16_notifier_should_be_empty.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#notifier_1 div").filter(has_text="FACEFIRST Notifier Notifier").locator("i").first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def generate_report(page, delay):
    page.locator("#reportField1Menu").select_option("string:number of events")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#reportField2MenuA").select_option("string:person")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#panel-container div").filter(has_text="Generate Report").nth(4).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_17_reporting_number_of_probable_match_events_by_enrollment.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#chart_1 div").filter(has_text="Reporting").locator("div").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("#reportField2MenuA").select_option("string:zone")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#panel-container div").filter(has_text="Generate Report").nth(4).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_17_reporting_number_of_probable_match_events_by_zone.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#chart_2 div").filter(has_text="Reporting").locator("div").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("#reportField1Menu").select_option("string:number of people")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#reportField2MenuC").select_option("string:zone")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#panel-container div").filter(has_text="Generate Report").nth(4).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_17_reporting_number_of_enrollments_by_zone.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#chart_3 div").filter(has_text="Reporting").locator("div").click()
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("#reportField1Menu").select_option("string:number of zones")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#reportField2MenuB").select_option("string:person")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#panel-container div").filter(has_text="Generate Report").nth(4).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_17_reporting_number_of_zones_by_enrollment.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("#chart_4 div").filter(has_text="Reporting").locator("div").click()
    page.wait_for_timeout(delay)  # Explicit delay


def update_enrollment_group(page, delay):
    page.get_by_text("Enrollment Groups").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("right-margin-menu > div:nth-child(4)").first.click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Action").nth(1).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Edit").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").fill("0.87")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").fill("0.87")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path="screenshots/_18_enrollment_group_update_for_audit_log_report.png")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def verify_dashboard_metrics(page1, delay):
    assert (page1.locator("#LossPrevented-0").text_content()) == "Total Loss Prevented$5,000"
    assert (page1.locator("#ActiveEnrollments-0").text_content()) == "Total New Enrollments26"
    assert (page1.locator("#AllActiveEnrollmentsRegardlessOfTimeCreated-0").text_content()) == ("Total FaceFirst "
                                                                                                "Enrollments26")
    assert (page1.locator("#TotalMatchEvents-0").text_content()) == "Total Probable Match Events25"
    assert (page1.locator("#VisitorSearches-0").text_content()) == "Visitor Searches11"
    assert (page1.locator(
        "#InvestigationSavingsTimeInHours-0").text_content()) == "Investigation Savings Time (hours)88"
    assert (page1.locator(
        "#TotalIdentifiedEventLossValue-0").text_content()) == "Total Identified Event Loss Value$5,000"
    assert (page1.locator("#TotalActiveEnrollmentsReportedLoss-0").text_content()) == (
        "Total Active Enrollments Reported Loss$5,500")
    assert page1.locator("#RepeatPeopleOfInterest-0").text_content() == "Repeat People of Interest0"
    # assert page1.locator(
    #     "div:nth-child(10) > .ff--dynamic-widget__wrapper > .ant-card > .ant-card-body").text_content() == "Tag NameResponded Probable Match EventsDeterred Probable Match Eventsassualt55push cart55threat55"
    # assert page1.locator(
    #     "div:nth-child(11) > .ff--dynamic-widget__wrapper > .ant-card > .ant-card-body").text_content() == "Enrollment GroupTotal Probable Match EventsResponded Probable Match EventsDeterred Probable Match Eventsabe555pte555soe555"
    page1.screenshot(path="screenshots/_19_insight_dashboard_overview.png")
    page1.wait_for_timeout(delay)  # Explicit delay
    page1.wait_for_timeout(delay)  # Explicit delay
    page1.wait_for_timeout(delay)  # Explicit delay


def verify_event_dashboard_matrices(page1, delay):
    page1.get_by_role("button", name="Overview Dashboard caret-down").click()
    page1.wait_for_timeout(delay)  # Explicit delay
    page1.get_by_text("Probable Match Events Dashboard").click()
    page1.wait_for_timeout(delay)  # Explicit delay

    assert page1.locator("#deterred-events").text_content() == "Deterred Probable Match Events25"
    assert page1.locator("#TotalTaggedEvents-0").text_content() == "Total Tagged Probable Match Events25"
    assert page1.locator(
        "#SeriousOffenderTaggedEvents-0").text_content() == "Serious Offender Tagged Probable Match Events15"
    assert page1.locator("#TotalMatchEvents-0").text_content() == "Total Probable Match Events25"
    page1.screenshot(path="screenshots/_20_insight_dashboard_events_1_.png")
    page1.wait_for_timeout(delay)  # Explicit delay

    with page1.expect_popup() as page2_info:
        page1.locator("div:nth-child(14) > div > .ant-card > .ant-card-body > div > div > div > canvas").click(position={"x": 725, "y": 123})
    page1.wait_for_timeout(delay)  # Explicit delay
    page1.screenshot(path="screenshots/_20_insight_dashboard_events_2_.png")
    page2 = page2_info.value
    page2.wait_for_timeout(delay)  # Explicit delay
    page2.screenshot(path="screenshots/_20_insight_dashboard_events_3_.png")
    page2.wait_for_timeout(delay)  # Explicit delay

    try:
        page2.close()
    except Exception as e:
        logger.error(f"An error occurred during Insight dashboard overview report: {e}")
        page2.screenshot(path="screenshots/_20_insight_dashboard_events_closing_error_1_.png")

    page1.wait_for_timeout(delay)  # Explicit delay

    try:
        page1.close()
    except Exception as e:
        logger.error(f"An error occurred during Insight dashboard overview report: {e}")
        page1.screenshot(path="screenshots/_20_insight_dashboard_events_closing_error_2_.png")


def verify_enrollment_dashboard_metrics(page1, delay):
    page1.get_by_role("button", name="Overview Dashboard caret-down").click()
    page1.wait_for_timeout(delay)  # Explicit delay
    page1.get_by_text("Enrollments Dashboard").click()
    page1.wait_for_timeout(delay)  # Explicit delay

    assert page1.locator(".ff--scorecard").first.text_content() == "Total New Enrollments26"
    assert page1.locator(".ff--scorecard").nth(1).text_content() == "Total FaceFirst Enrollments26"
    page1.screenshot(path="screenshots/_21_insight_dashboard_enrollment_1_.png")
    page1.wait_for_timeout(delay)  # Explicit delay

    try:
        page1.close()
    except Exception as e:
        logger.error(f"An error occurred during Insight dashboard enrollment report: {e}")
        page1.screenshot(path="screenshots/_21_insight_dashboard_enrollment_closing_error.png")


def enroll_visitor(page, organization, delay):
    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        print(text)
        print("Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        print(f"Add Details text is not visible: {e}")
        page.locator(
            "//p[contains(text(),'Visitor Search Results')]//parent::div//div[@tiptitle=\"Close Panel\"]").click()
        page.locator("//p[contains(text(),'Visitor Search')]//parent::div//div[@tiptitle=\"Close Panel\"]").click()
        page.locator("//div[@ng-controller=\"IdentifyResultsCtrl\"]//div[@tiptitle=\"Close Panel\"]").click()

        print("Identify Results panel closed")
        page.wait_for_timeout(delay)  # Explicit delay
        print("waiting for IE Button.")
        identify_enroll_locator = page.locator(
            "(//p[contains(text(), \"Click 'Enroll' to enroll\")]//parent::div//preceding-sibling::div)[3]//div[@ng-click=\"enrollmentStep1()\"]")
        page.wait_for_timeout(delay)
        identify_enroll_locator.click()
        print("Clicked on IE Button.")
    try:
        print("Adding details to panel started")
        page.wait_for_timeout(delay)
        page.locator("select[name=\"basis\"]").select_option("number:3")
        # page.locator("select[name=\"internal_group\"]").select_option(
        #     "DefaultEnrollmentGroup (Serious Offender - None)")
        internal_group = "fraude"
        page.wait_for_timeout(delay)  # Explicit delay

        select = page.locator('select[name="internal_group"]')
        select.wait_for(state="visible")

        # Get all option texts and values
        option_texts = select.locator('option').all_text_contents()
        option_values = select.locator('option').evaluate_all('els => els.map(e => e.value)')

        needle = internal_group
        match_index = next(
            (i for i, t in enumerate(option_texts) if needle.lower() in (t or "").lower()),
            None
        )
        if match_index is None:
            raise Exception(f'No option contains "{needle}"')

        exact_label = option_texts[match_index].strip()
        exact_value = option_values[match_index]

        if exact_value:
            select.select_option(value=exact_value)
        else:
            select.select_option(label=exact_label)

        logger.info(f'Selected: label="{exact_label}", value="{exact_value}"')
        page.wait_for_timeout(delay)  # Explicit delay

        page.get_by_text("SELECT", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        print(f"organization: {organization}")
        page.locator("region-search").get_by_text(organization).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("region-search").get_by_text("Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        print(f"region selected")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('input[name="storeId"]').fill(f"Kormangala")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('input[name="enrollmentNumber"]').fill("EN Through Image Search")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("spinbutton").fill("100")
        page.wait_for_timeout(delay)  # Explicit delay

        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
        print(f"current date: {current_time}")
        # Locate by placeholder and fill
        page.get_by_placeholder("mm/dd/yyyy HH:mm").fill(current_time)
        page.wait_for_timeout(delay)  # Explicit delay

        page.locator('input[name="action"]').fill(f"reported cop")
        page.wait_for_timeout(delay)  # Explicit delay

        page.get_by_text("SUBMIT REVIEW").click()
        page.wait_for_timeout(10000)  # Explicit delay

        page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        print(f"Failed to enroll visitor: {e}")


def enroll_large_image(page, organization, storeID, EN, delay):
    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        logger.info(f"{text}")
        logger.info("Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.info(f"Add Details text is not visible: {e}")
        logger.info("waiting for IE Button.")
        identify_enroll_locator = page.locator("//p[@ng-bind=\"'Enroll' | i18n\"]//parent::div")
        page.wait_for_timeout(delay)
        identify_enroll_locator.click()
        logger.info("Clicked on IE Button.")
    try:
        logger.info("Adding details to panel started")
        page.wait_for_timeout(delay)
        page.locator("select[name=\"basis\"]").select_option("number:3")
        page.wait_for_timeout(delay)
        # page.locator("select[name=\"internal_group\"]").select_option("number:2")
        internal_group = conftest.ENROLLMENT_GROUPS[1]["name"]
        # internal_group = "fraude"
        page.wait_for_timeout(delay)  # Explicit delay

        select = page.locator('select[name="internal_group"]')
        select.wait_for(state="visible")

        # Get all option texts and values
        option_texts = select.locator('option').all_text_contents()
        option_values = select.locator('option').evaluate_all('els => els.map(e => e.value)')

        needle = internal_group
        match_index = next(
            (i for i, t in enumerate(option_texts) if needle.lower() in (t or "").lower()),
            None
        )
        if match_index is None:
            raise Exception(f'No option contains "{needle}"')

        exact_label = option_texts[match_index].strip()
        exact_value = option_values[match_index]

        if exact_value:
            select.select_option(value=exact_value)
        else:
            select.select_option(label=exact_label)

        logger.info(f'Selected: label="{exact_label}", value="{exact_value}"')

        page.wait_for_timeout(delay)  # Explicit delay

        page.get_by_text("SELECT", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info(f"organization: {organization}")
        page.locator("region-search").get_by_text(organization).click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("region-search").get_by_text("Save").click()
        page.wait_for_timeout(delay)  # Explicit delay
        logger.info(f"region selected")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('input[name="storeId"]').fill(storeID)
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('input[name="enrollmentNumber"]').fill(EN)
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_role("spinbutton").fill("50")
        page.wait_for_timeout(delay)  # Explicit delay

        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
        logger.info(f"current date: {current_time}")
        # Locate by placeholder and fill
        page.get_by_placeholder("mm/dd/yyyy HH:mm").fill(current_time)
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('input[name="action"]').fill(f"reported cop")
        page.wait_for_timeout(delay)  # Explicit delay
        if page.get_by_text("SUBMIT REVIEW").is_visible():
            page.get_by_text("SUBMIT REVIEW").click()
        else:
            page.locator("//a[@ng-bind=\"'Save' | i18n\"]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        success_msg = page.locator('//*[contains(text(), "Success!")]')
        if success_msg.is_visible():
            logger.info(f'success message visible: {success_msg.is_visible()}')
        else:
            logger.info(f'success message visible: {success_msg.is_visible()}')
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        logger.info(f"Failed to enroll large image: {e}")


def delete_enrollment(page, delay):
    try:
        page.wait_for_timeout(delay)
        page.locator("//span[@ng-bind=\"::('Action' | i18n)\"]").click()
        page.wait_for_timeout(delay)
        page.get_by_text("Permanently DELETE Selected Enrollments", exact=True).click()
        page.wait_for_timeout(delay)
        page.locator("//button[@ng-click=\"delete()\"][1]").click()
        page.wait_for_timeout(delay)
        success_message = page.locator("//p[@ng-bind=\"deleteResponseMessage\"]")
        if success_message.is_visible():
            logger.info(f"{success_message.inner_text()}")
    except Exception as e:
        logger.info(f"Failed to click on delete button: {e}")


def edit_enrollment(page, delay):
    try:
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("//table//input[@name='storeId']").clear()
        page.locator("//table//input[@name='storeId']").fill(f"Kormangala Edited")
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator('//table//input[@name="enrollmentNumber"]').clear()
        page.locator('//table//input[@name="enrollmentNumber"]').fill("Edit Enrollment Edited")
        page.wait_for_timeout(delay)  # Explicit delay
        page.get_by_text("SUBMIT REVIEW").click()
        page.wait_for_timeout(10000)  # Explicit delay
    except Exception as e:
        logger.info(f"failed to edit enrollment: {e}")


def enable_disable_enrollment(page, status, option, delay):
    logger.info("Entered into enable disable function")
    try:
        if status == "disable":
            page.wait_for_timeout(delay)
            page.locator("//td[@ng-show=\"editingMode\"]//label//span[@ng-bind=\"'Disabled' | i18n\"]").click()
            page.wait_for_timeout(delay)
            page.locator("//div[@ng-controller=\"CustomFieldsCtrl\"]//select[@name=\"disabledReason\"]").select_option(option)
            page.wait_for_timeout(delay)
            page.locator("//a[@ng-bind=\"'Save' | i18n\"]").click()
            # page.locator("a").filter(has_text="Save").click()
            page.wait_for_timeout(delay)
        elif status == "enable":
            page.wait_for_timeout(delay)
            page.locator("//td[@ng-show=\"editingMode\"]//label//span[@ng-bind=\"'Enabled' | i18n\"]").click()
            page.wait_for_timeout(delay)
            page.locator("//a[@ng-bind=\"'Save' | i18n\"]").click()
            page.wait_for_timeout(delay)
        else:
            logger.info("no status displayed")
    except Exception as e:
        logger.info(f"failed to enable/disable enrollment: {e}")


def adding_note_details(page, location, enrollment_number):
    try:
        page.get_by_role("row", name="LOCATION/STORE").get_by_role("textbox").fill(location)
        # page.get_by_role("row", name="ENROLLMENT NUMBER").get_by_role("textbox").click()
        page.get_by_role("row", name="ENROLLMENT NUMBER").get_by_role("textbox").fill(enrollment_number)
        # page.get_by_role("spinbutton").click()
        page.get_by_role("spinbutton").fill("0")
        page.locator("select[name=\"enrollmentEventType\"]").select_option("Store threat")
        page.locator("select[name=\"activityType\"]").select_option("SCO fraud")
        page.locator("select[name=\"methodOffence\"]").select_option("Concealment")
        # page.locator("input[name=\"reportedBy\"]").click()
        page.locator("input[name=\"reportedBy\"]").fill("Renuka")
        # page.locator("textarea[name=\"narrativeDesc\"]").click()
        page.locator("textarea[name=\"narrativeDesc\"]").fill("test note")
        page.wait_for_timeout(delay)
        page.get_by_role("button", name="  Add Location").click()
        page.locator(".gm-style > div > div:nth-child(2)").click()
        page.locator(
            ".controller-panel-div.posrel.fltlft.disblk.xlrg-panel-width > .panel-heading-container > .close-button-large").click()
        page.locator("#note_details_5").get_by_text("Save", exact=True).click()
        page.wait_for_timeout(delay)
        logger.info("Note created successfully")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


def natural_key(s: str):
    """
    Split into chunks: digits as integers, non-digits as lowercased strings.
    Example: 'soe_case_10a' -> ['soe', '_case_', 10, 'a']
    Sorting will compare each chunk pairwise.
    """
    tokens = re.findall(r'\d+|\D+', s)
    key = []
    for tok in tokens:
        if tok.isdigit():
            key.append(int(tok))
        else:
            key.append(tok.lower())  # case-insensitive
    return key


def welcome(page, delay):
    try:
        logger.info("Welcome to the FaceFirst Platform.")
        page.get_by_role("button", name="Close").click()
        logger.info("Clicked the Close button.")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def dm_log_in(page, credentials, delay):
    page.get_by_role("textbox", name="Email (Username) *").fill(credentials["email"])
    logger.info("Filled out the Email field for login.")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Password *").fill(credentials["password"])
    logger.info("Filled out the Password field for login.")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("button", name="Login").click()
    logger.info("Clicked the Login button.")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info(f"login_user:{credentials['email']}")


def dm_log_out(page, delay):
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("xpath=/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[2]/a[1]").click()
    logger.info("Clicked the core link.")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("menuitem", name="Logout").click()
    logger.info("Clicked the Logout menu item.")
    page.wait_for_timeout(delay)  # Explicit delay


def login_to_portal_with_user_if_not_logged_in(page, credentials, delay):
    try:
        print(f'\ncredentials: {credentials}')
        logger.info(f'\ncredentials: {credentials}')
        if page.url != conftest.BASE_URL:
            print(f"\nloading page {conftest.BASE_URL}")
            page.goto(conftest.BASE_URL)
            page.wait_for_timeout(delay)
            username_textbox = page.locator('//input[@id="login-username"]')
            if username_textbox.is_visible():
                print(f"username_textbox displayed: {username_textbox.is_visible()}")
                # print(f'username: {credentials["username"]}')
                print(f"username: {credentials['username']}")
                username_textbox.fill(credentials['username'])
                page.wait_for_timeout(delay)
            else:
                print(f"username_textbox did not display: {username_textbox.is_visible()}")
            pass_textbox = page.locator('//input[@id="login-password"]')
            if pass_textbox.is_visible():
                print(f"pass_textbox displayed: {pass_textbox.is_visible()}")
                print(f"password: {credentials['password']}")
                pass_textbox.fill(credentials['password'])
                page.wait_for_timeout(delay)
            else:
                print(f"pass_textbox did not display: {pass_textbox.is_visible()}")
            login_button = page.locator('//div[@ng-click="login()"]')
            if login_button.is_visible():
                print(f"login button displayed: {login_button.is_visible()}")
                login_button.hover()
                login_button.click()
                # page.wait_for_timeout(5000)
            else:
                print(f"login button did not display: {login_button.is_visible()}")
            agree_to_term(page=page, delay=delay)
            # page.wait_for_timeout(delay)
        else:
            page.wait_for_selector('//input[@id="login-username"]', state='visible', timeout=delay_10_Second)
            print(f"current url is {page.url}")
            username_textbox = page.locator('//input[@id="login-username"]')
            if username_textbox.is_visible():
                print(f"username_textbox displayed: {username_textbox.is_visible()}")
                # print(f'username: {credentials["username"]}')
                print(f"username: {credentials['username']}")
                username_textbox.fill(credentials['username'])
                page.wait_for_timeout(delay)
            else:
                print(f"username_textbox did not display: {username_textbox.is_visible()}")
            pass_textbox = page.locator('//input[@id="login-password"]')
            if pass_textbox.is_visible():
                print(f"pass_textbox displayed: {pass_textbox.is_visible()}")
                print(f"password: {credentials['password']}")
                pass_textbox.fill(credentials['password'])
                page.wait_for_timeout(delay)
            else:
                print(f"pass_textbox did not display: {pass_textbox.is_visible()}")
            login_button = page.locator('//div[@ng-click="login()"]')
            if login_button.is_visible():
                print(f"login button displayed: {login_button.is_visible()}")
                login_button.hover()
                login_button.click()
                # page.wait_for_timeout(5000)
            else:
                print(f"login button did not display: {login_button.is_visible()}")
            agree_to_term(page=page, delay=delay)
    except Exception as e:
        logger.error(f"An Exception occurred: {type(e).__name__}")
        logger.error(f"Exception message: login_to_portal_with_user_if_not_logged_in")
        print(f"Exception@: login_to_portal_with_user_if_not_logged_in")
        print(f"Exception type: {type(e).__name__}")


# *****************************************


def login(page, username, password=PASSWORD):
    page.context.clear_cookies()
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("//input[@id='login-username']", timeout=60000)
    page.fill("//input[@id='login-username']", username)
    page.wait_for_selector("//input[@id='login-password']", timeout=60000)
    page.fill("//input[@id='login-password']", password)
    page.click('//div[@ng-click="login()"]')
    page.wait_for_selector("#dashboard-menu-container", timeout=10000)


def logout_if_logged_in(page, delay):
    try:
        logout_button = page.locator('//div[@ng-click="logout()"]')
        if logout_button.is_visible():
            logout_button.click()
            page.wait_for_timeout(delay)  # wait for logout to complete
            print("Logged out successfully")
        else:
            print("Logout button not visible, maybe already logged out")
    except Exception as ex:
        print(f"Exception during logout: {type(ex).__name__}, {ex}")


def setup_page(page):
    page.goto(BASE_URL)


def close_one_panel(page):
    try:
        print("Closing one panel.")
        close_button = page.locator('//div[@data-original-title="Close Panel"]').all()
        print(len(close_button))
        if len(close_button) > 0:
            if close_button[0].is_visible():
                print(f"Close button displayed: {close_button[0].is_visible()}")
                # close_button.hover()
                close_button[0].click()
            else:
                print(f"Close button did not display: {close_button[0].is_visible()}")

    except Exception as ex:
        print(f"Exception occurred: {type(ex).__name__}")
        print(f"Exception message: close_one_panel")


def close_all_panels_one_by_one(page):
    try:
        print("Closing all panels.")
        number_of_panels_displayed = page.locator('//div[@class="controller-panel-div posrel fltlft disblk lrg-panel-width"]').all()
        print(f'number of panels count: {len(number_of_panels_displayed)}')
        if len(number_of_panels_displayed) > 0:

            for i in range(len(number_of_panels_displayed)):
                close_one_panel(page)
                page.wait_for_timeout(delay_1_second)
        print("closed all panels.")
        page.wait_for_timeout(delay_1_second)
    except Exception as ex:
        print(f"Exception occurred: {type(ex).__name__}")
        print(f"Exception message: close_all_panels_one_by_one")


def perform_vsj_image_search(page, subject, index, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_11_vs_image_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay


def perform_image_meta_search(page, subject, index, organization, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    set_vsj_search_date_and_time(page, delay)
    select_organization(page, organization, delay)
    # page.get_by_role("combobox").select_option("string:5")
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.screenshot(path=f"screenshots/_12_vs_image_meta_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay


def perform_vsj_threshold_image_meta_search(page, subject, index, organization, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    set_vsj_search_date_and_time(page, delay)
    select_organization(page, organization, delay)
    slider = page.locator("#thresholdSlider")
    box = slider.bounding_box()
    start_x = box["x"] + box["width"] * 0.25  # current position
    end_x = box["x"] + box["width"] * 0.50  # target position
    y = box["y"] + box["height"] / 2
    page.wait_for_timeout(delay)
    page.mouse.move(start_x, y)
    page.mouse.down()
    page.mouse.move(end_x, y)
    page.mouse.up()

    page.get_by_role("combobox").select_option("string:5")
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.screenshot(path=f"screenshots/_12_vs_image_meta_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay


def set_vsj_search_date_and_time(page, delay):
    # Enable Start Date
    page.locator("#includeStartDateEl").check()
    page.wait_for_timeout(delay)

    # Open Date Picker
    page.locator("#startDateField").click()
    page.wait_for_timeout(delay)

    # Move to next month (as per your existing working logic)
    page.get_by_title("Next Month").click()
    page.wait_for_timeout(delay)

    print("Search date success")

    # -------- DATE SELECTION (FIXED) --------
    target_day = str(conftest.search_date.day)
    print(f"Selecting date: {target_day}")

    # Click ONLY current-month date (not old / new)
    page.locator(
        f"//td[not(contains(@class,'old')) and "
        f"not(contains(@class,'new')) and text()='{target_day}']"
    ).click()

    page.wait_for_timeout(delay)

    # -------- TIME SELECTION --------
    print("Search time success")

    page.get_by_title("Select Time").click()
    page.wait_for_timeout(delay)

    # Hour
    page.get_by_title("Pick Hour").click()
    page.wait_for_timeout(delay)
    page.get_by_role(
        "cell", name=conftest.search_time.strftime("%I")
    ).click()

    page.wait_for_timeout(delay)

    # Minute
    page.get_by_title("Pick Minute").click()
    page.wait_for_timeout(delay)
    page.get_by_role(
        "cell", name=conftest.search_time.strftime("%M")
    ).click()

    page.wait_for_timeout(delay)

    # AM / PM Toggle
    if conftest.search_time.strftime("%p") == "PM":
        page.get_by_title("Toggle Period").click()

    page.wait_for_timeout(delay)

    # Close Picker
    page.get_by_title("Close the picker").click()
    page.wait_for_timeout(delay)

    print("Search date & time selected successfully ✅")


def set_date_by_typing(page, checkbox_locator, input_locator, dt_string):
    page.locator(checkbox_locator).check()
    inp = page.locator(input_locator)
    inp.fill("")  # clear
    inp.type(dt_string)  # e.g., "11/11/2025 12:00 AM"
    page.keyboard.press("Enter")
    page.wait_for_timeout(delay)


def set_date_for_events(page, checkbox_locator, input_locator, dt_string):
    """Set date in Events page date picker."""
    page.locator(checkbox_locator).check()
    inp = page.locator(input_locator)
    inp.fill("")  # clear existing value
    inp.type(dt_string)  # e.g., "11/11/2025 12:00 AM"
    inp.press("Enter")
    page.wait_for_timeout(delay)


def select_start_date_with_checkbox_and_confirm1(page, target_date,):
    checkbox = page.locator("#includeStartDateEl")
    if not checkbox.is_checked():
        checkbox.check()

    page.locator("#startDateField").click()

    target = datetime.combine(target_date, datetime.min.time())

    target_month_year = target.strftime("%B %Y")
    target_data_day = target.strftime("%m/%d/%Y")

    month_year_locator = page.locator(
        ".bootstrap-datetimepicker-widget .datepicker-days th.picker-switch"
    )

    while True:
        current_month_year = month_year_locator.inner_text().strip()
        if current_month_year == target_month_year:
            break

        current_date = datetime.strptime(current_month_year, "%B %Y")
        if current_date < target:
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days th.next").click()
        else:
            page.locator(".bootstrap-datetimepicker-widget .datepicker-days th.prev").click()

        page.wait_for_timeout(delay)

    page.locator(
        f".bootstrap-datetimepicker-widget td[data-action='selectDay'][data-day='{target_data_day}']"
    ).click()

    page.locator(".bootstrap-datetimepicker-widget a[data-action='close']").click()



def select_start_date_with_checkbox_and_confirm(page, target_date, delay):
    checkbox = page.locator("#includeStartDateEl")

    if not checkbox.is_checked():
        checkbox.check()

    # tiny Angular settle time (important)
    page.wait_for_timeout(300)

    # click directly — Playwright retries internally
    page.locator("#startDateField").click()

    target = datetime.combine(target_date, datetime.min.time())
    target_month_year = target.strftime("%B %Y")
    target_data_day = target.strftime("%m/%d/%Y")

    month_year_locator = page.locator(
        ".bootstrap-datetimepicker-widget .datepicker-days th.picker-switch"
    )

    while month_year_locator.inner_text().strip() != target_month_year:
        current = datetime.strptime(
            month_year_locator.inner_text().strip(), "%B %Y"
        )

        if current < target:
            page.locator(
                ".bootstrap-datetimepicker-widget .datepicker-days th.next"
            ).click()
        else:
            page.locator(
                ".bootstrap-datetimepicker-widget .datepicker-days th.prev"
            ).click()

        page.wait_for_timeout(delay)

    page.locator(
        f".bootstrap-datetimepicker-widget "
        f"td[data-action='selectDay'][data-day='{target_data_day}']"
    ).click()

    page.locator(
        ".bootstrap-datetimepicker-widget a[data-action='close']"
    ).click()



def select_end_date_with_checkbox_and_confirm(page, delay):
    target_date = date.today()

    # 1️ Enable End Date checkbox
    checkbox = page.locator("#includeEndDateEl")
    if not checkbox.is_checked():
        checkbox.check()

    #  Let Angular settle
    page.wait_for_timeout(300)

    # 2️ Open End Date calendar (direct click)
    page.locator("#endDateField").click()

    # 3️ Prepare date formats
    target = datetime.combine(target_date, datetime.min.time())
    target_month_year = target.strftime("%B %Y")
    target_data_day = target.strftime("%m/%d/%Y")

    month_year_locator = page.locator(
        ".bootstrap-datetimepicker-widget .datepicker-days th.picker-switch"
    )

    # 4️ Navigate month/year
    while month_year_locator.inner_text().strip() != target_month_year:
        current_date = datetime.strptime(
            month_year_locator.inner_text().strip(), "%B %Y"
        )

        if current_date < target:
            page.locator(
                ".bootstrap-datetimepicker-widget .datepicker-days th.next"
            ).click()
        else:
            page.locator(
                ".bootstrap-datetimepicker-widget .datepicker-days th.prev"
            ).click()

        page.wait_for_timeout(delay)

    # 5️ Select day
    page.locator(
        f".bootstrap-datetimepicker-widget "
        f"td[data-action='selectDay'][data-day='{target_data_day}']"
    ).click()

    # 6️ Close calendar
    page.locator(
        ".bootstrap-datetimepicker-widget a[data-action='close']"
    ).click()

# def select_end_date_with_checkbox_and_confirm(page, date_input_locator="#endDateField"):
#
#
#     # 1️ Check checkbox if not already checked
#     checkbox = page.locator("#includeEndDateEl")
#     if not checkbox.is_checked():
#         checkbox.check()
#
#     # 2️ Open calendar
#     page.locator(date_input_locator).click()
#
#     # 3️ Convert target date
#     target = datetime.strptime(end_date, "%d/%m/%Y")  # string from conftest
#     target_month_year = target.strftime("%B %Y")
#     target_data_day = target.strftime("%m/%d/%Y")
#
#     # 4️ Navigate to correct month/year
#     month_year_locator = page.locator(".bootstrap-datetimepicker-widget .datepicker-days th.picker-switch")
#     while True:
#         current_month_year = month_year_locator.inner_text().strip()
#         if current_month_year == target_month_year:
#             break
#         current_date = datetime.strptime(current_month_year, "%B %Y")
#         if current_date < target:
#             page.locator(".bootstrap-datetimepicker-widget .datepicker-days th.next").click()
#         else:
#             page.locator(".bootstrap-datetimepicker-widget .datepicker-days th.prev").click()
#         page.wait_for_timeout(3000)
#
#     # 5️ Select the day
#     page.locator(
#         f".bootstrap-datetimepicker-widget td[data-action='selectDay'][data-day='{target_data_day}']"
#     ).click()
#
#     # 6️ Click ✓ tick mark to close calendar
#     page.locator(".bootstrap-datetimepicker-widget a[data-action='close']").click()


def select_groups_and_zones(page, groups, zones):
    # -------------------- SELECT GROUPS --------------------
    page.locator(".group-zone-bu").first.click()
    page.wait_for_timeout(delay)

    group_menu = page.locator("#group-selection-menu")
    group_menu.wait_for(state="visible", timeout=5000)

    for group in groups:
        item = group_menu.get_by_role("listitem").filter(has_text=group.strip())
        item.wait_for(state="visible", timeout=5000)
        item.click(force=True)
        page.wait_for_timeout(delay)

    page.locator(".save-group-bu").wait_for(state="visible", timeout=5000)
    page.locator(".save-group-bu").click(force=True)

    group_menu.wait_for(state="hidden", timeout=5000)

    # -------------------- SELECT ZONES --------------------
    if zones:
        dropdown = page.locator(':text-is("Select zone filter")')
        dropdown.wait_for(state="visible", timeout=5000)
        dropdown.click(force=True)

        zone_menu = page.locator("#zone-selection-menu")
        zone_menu.wait_for(state="visible", timeout=5000)

        for zone in zones:
            item = zone_menu.get_by_role("listitem").filter(has_text=zone.strip())
            item.wait_for(state="visible", timeout=5000)
            item.click(force=True)
            page.wait_for_timeout(delay)

        # ✅ CLICK SAVE ZONE BUTTON (THIS WAS MISSING)
        save_zone_btn = page.locator(".save-zone-bu")
        save_zone_btn.wait_for(state="visible", timeout=5000)
        save_zone_btn.click(force=True)

        # Wait until save button disappears (Angular update)
        save_zone_btn.wait_for(state="hidden", timeout=5000)

    # -------------------- GENERATE REPORT --------------------
    generate_btn = page.locator(
        '.group-zone-bu:has-text("Generate Report")'
    )
    generate_btn.wait_for(state="visible", timeout=10000)
    generate_btn.click(force=True)


def select_single_group(page, group, delay, timeout=10000):
    # Open group menu
    group_button = page.locator(".group-zone-bu").first
    group_button.wait_for(state="visible", timeout=timeout)
    group_button.click()
    page.wait_for_timeout(delay)
    # Wait for menu
    menu = page.locator("#group-selection-menu")
    menu.wait_for(state="visible", timeout=timeout)
    page.wait_for_timeout(delay)

    # Select group
    menu.get_by_role("listitem").filter(has_text=group).first.click()
    page.wait_for_timeout(delay)
    # Save
    save_button = page.locator(".save-group-bu")
    save_button.wait_for(state="visible", timeout=timeout)
    save_button.click()
    page.wait_for_timeout(delay)
    logger.info(f"Group '{group}' selected and saved.")
    # Generate Report
    generate_btn = page.locator("div.group-zone-bu:has-text('Generate Report')")
    generate_btn.wait_for(state="visible", timeout=timeout)
    generate_btn.click()
    page.wait_for_timeout(delay)
    logger.info("Clicked 'Generate Report'")


def click_start_date_checkbox(page):
    status = []
    try:
        start_date_checkbox = page.locator("#includeStartDateEl")

        if start_date_checkbox.is_visible() and start_date_checkbox.is_enabled():
            if not start_date_checkbox.is_checked():
                start_date_checkbox.check()
                logger.info("✅ Start Date checkbox checked")
            else:
                logger.info("ℹ️ Start Date checkbox already checked")
                page.wait_for_timeout(delay_2_second)
            status.append(True)
        else:
            logger.info("❌ Start Date checkbox not visible or not enabled")
            status.append(False)
    except Exception as e:
        logger.info(f"❌ Failed to click Start Date checkbox: {e}")
        status.append(False)

    return False not in status

def click_end_date_checkbox(page):
    status = []
    try:
        start_date_checkbox = page.locator("#includeEndDateEl")

        if start_date_checkbox.is_visible() and start_date_checkbox.is_enabled():
            if not start_date_checkbox.is_checked():
                start_date_checkbox.check()
                page.wait_for_timeout(delay_2_second)
                logger.info("✅ Start Date checkbox checked")
            else:
                logger.info("ℹ️ Start Date checkbox already checked")
            status.append(True)
        else:
            logger.info("❌ Start Date checkbox not visible or not enabled")
            status.append(False)
    except Exception as e:
        logger.info(f"❌ Failed to click Start Date checkbox: {e}")
        status.append(False)

    return False not in status

def select_one_group_and_all_zones_and_generate_report(page,group,delay,timeout=10000):
    # -------------------- SELECT ONLY ONE GROUP --------------------
    page.locator(".group-zone-bu").first.click()
    page.wait_for_timeout(delay)

    group_menu = page.locator("#group-selection-menu")
    group_menu.wait_for(state="visible", timeout=timeout)

    # Clear previous selections
    selected_items = group_menu.locator(
        'li.selected, li[aria-selected="true"]'
    )
    for i in range(selected_items.count()):
        selected_items.nth(i).click(force=True)
        page.wait_for_timeout(delay)

    # Select required group
    group_menu.get_by_role("listitem").filter(
        has_text=group
    ).first.click(force=True)

    page.locator(".save-group-bu").click(force=True)
    group_menu.wait_for(state="hidden", timeout=timeout)
    print(f"Selected group: {group}")

    # -------------------- SELECT ALL ZONES (STABLE) --------------------
    dropdown = page.locator(':text-is("Select zone filter")')
    dropdown.wait_for(state="visible", timeout=timeout)
    dropdown.click(force=True)
    page.wait_for_timeout(delay)

    zone_menu = page.locator("#zone-selection-menu")
    zone_menu.wait_for(state="visible", timeout=timeout)
    page.wait_for_timeout(delay)

    # 🔹 CRITICAL: wait until at least ONE zone is rendered
    zone_menu.get_by_role("listitem").first.wait_for(
        state="visible",
        timeout=timeout
    )

    # 🔹 Try Select All (best option)
    select_all = zone_menu.locator(
        'li:has-text("Select All")'
    )

    if select_all.count() > 0:
        select_all.first.click(force=True)
    else:
        # 🔹 Safe fallback: select visible zones only
        zone_items = zone_menu.get_by_role("listitem")
        zone_count = zone_items.count()

        for i in range(zone_count):
            page.wait_for_timeout(delay)
            zone = zone_items.nth(i)
            if zone.is_visible():
                zone.click(force=True)
                page.wait_for_timeout(delay)

    # Save zones
    save_zone_btn = page.locator(".save-zone-bu")
    save_zone_btn.wait_for(state="visible", timeout=timeout)
    save_zone_btn.click(force=True)
    save_zone_btn.wait_for(state="hidden", timeout=timeout)

    print("All zones selected")

    # -------------------- GENERATE REPORT --------------------
    generate_btn = page.locator(
        "div.group-zone-bu:has-text('Generate Report')"
    )
    generate_btn.wait_for(state="visible", timeout=timeout)
    generate_btn.click(force=True)

    page.locator(".panel-heading").first.wait_for(
        state="visible",
        timeout=timeout
    )
    print("Report generated successfully")


def get_group_by_index(index=0):
    if not Notifier_groups:
        raise ValueError("Notifier_groups is empty")

    if index < 0 or index >= len(Notifier_groups):
        raise IndexError("Invalid group index")

    selected_group = Notifier_groups[index]
    reordered_groups = [selected_group] + [
        g for i, g in enumerate(Notifier_groups) if i != index
    ]

    return selected_group, reordered_groups


def get_start_time():
    try:
        time = datetime.now()
        print(f"\nget_start_time: {time}")
        return time
    except Exception as ex:
        print(f"\nget_start_time: {type(ex).__name__}")
        pass


def get_end_time():
    try:
        time = datetime.now()
        print(f"\nget_start_time: {time}")
        return time
    except Exception as ex:
        print(f"\nget_start_time: {type(ex).__name__}")
        pass


# def select_groups(page, groups_to_select: list):
#     """
#     Select groups from group selection menu
#     """
#     group_items = page.locator("ul#group-selection-menu li.report-menu-list-item")
#     page.wait_for_timeout(delay)
#     count = group_items.count()
#     for i in range(count):
#         group_name = group_items.nth(i).locator("p").inner_text().strip()
#         if group_name in groups_to_select:
#             group_items.nth(i).click()
#             save_group_button = page.locator("//div[contains(@class,'save-group-bu')]//p[text()='Save group selection']")
#             save_group_button.click()
#             page.wait_for_timeout(1500)

def select_groups(page, groups):
    # 👉 Open main group selection menu (ONLY ONCE)
    page.locator(".group-zone-bu").first.click()
    page.wait_for_timeout(delay)
    for group in groups:
        # 👉 Select the group item
        page.locator("#group-selection-menu") \
            .get_by_role("listitem") \
            .filter(has_text=group.lower()) \
            .click()
        page.wait_for_timeout(delay)
        # 👉 Click SAVE button
        page.locator(".save-group-bu").click()
        page.wait_for_timeout(delay)
        # 👉 After saving, open the menu AGAIN (small reopen button)
        page.locator(".group-zone-bu.posrel.fltlft.disblk.tac-horizontal").click()
        page.wait_for_timeout(delay)
        # 👉 Click the second nested menu opener (your UI requires this)
        page.locator(".group-zone-bu.posrel").first.click()
        page.wait_for_timeout(delay)


#
# def select_zones(page, zones):
#     for zone in zones:
#         # Open the zone dropdown
#         page.locator(':text-is("Select zone filter")').click()
#         page.wait_for_timeout(delay)
#
#         # Select the desired zone from the menu
#         page.locator("#zone-selection-menu") \
#             .get_by_role("listitem") \
#             .filter(has_text=zone.lower()) \
#             .click()
#         page.wait_for_timeout(delay)

# def add_enrollment_to_eg(page, eg_name):
#     print(f"Linking enrollment to Enrollment Group: {eg_name}")
#     page.get_by_role("button", name="Enrollments").click()
#     page.locator("#people_2 a", has_text="Filter").click()
#     page.locator("a", has_text="UnlinkedEnrollments").click()
#     page.wait_for_timeout(delay)
#
#     enrollment_rows = page.locator("#people_2 li.non-linked-list-menu-item")
#     enrollment_rows.first.wait_for(state="visible", timeout=15000)
#     enrollment_rows.first.locator(".right-menu-checkbox-container .icheckbox_polaris ins").click(force=True)
#
#     page.locator("#people_2 a", has_text="Action").click()
#     page.locator("#people_2").get_by_text("Add Enrollment To Group(s)", exact=True).click()
#
#     page.locator("//p[@class='item-title']").first.wait_for(state="visible", timeout=15000)
#
#     eg_row = page.locator(f"//p[@class='item-title' and normalize-space()='{eg_name}']")
#     eg_row.wait_for(state="visible", timeout=20000)
#     eg_row.scroll_into_view_if_needed()
#     page.wait_for_timeout(delay)
#
#     eg_row.locator(
#         "xpath=ancestor::div[contains(@class,'list-item')]"
#         "//div[contains(@class,'right-menu-checkbox-container')]//div[contains(@class,'icheckbox_polaris')]//ins"
#     ).wait_for(state="visible", timeout=10000)
#     eg_row.locator(
#         "xpath=ancestor::div[contains(@class,'list-item')]"
#         "//div[contains(@class,'right-menu-checkbox-container')]//div[contains(@class,'icheckbox_polaris')]//ins"
#     ).click(force=True)
#
#     for btn_text in ["Add", "Save", "Apply"]:
#         btn = page.locator(f"//button[normalize-space()='{btn_text}']")
#         if btn.count() > 0:
#             btn.first.wait_for(state="visible", timeout=10000)
#             btn.first.click()
#             break
#     print("Linked enrollment to eg successfully added")
#     page.wait_for_timeout(delay)


def create_notification_group_1(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    # add_eg_to_notification_group(page, ng, delay)
    # page.wait_for_timeout(delay)  # Explicit delay
    # logger.info("Closing notification group creation panel")
    # page.wait_for_timeout(delay)  # Explicit delay
    # page.locator(
    #     "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_eg_to_notification_group(page, ng, delay):
    logger.info("Adding Enrollment Group to Notification Group")
    eg_name = ng["eg_name"]

    # ---------- OPEN ENROLLMENT GROUPS TAB ----------
    page.get_by_role("button", name="Enrollment Groups").click()
    page.wait_for_timeout(delay)

    # ---------- FILTER → UNLINKED ----------
    page.locator("#enrollment_groups_1 a", has_text="Filter").click()
    page.locator("a", has_text="Unlinked Enrollment Groups").click()
    page.wait_for_timeout(delay)
    # page.locator("ul.list-group").wait_for(state="visible", timeout=15000)

    page.locator("#enrollment_groups_1") \
        .get_by_role("listitem") \
        .filter(has_text=ng["eg_name"]) \
        .get_by_role("insertion") \
        .click()
    page.wait_for_timeout(delay)
    # ---------- ACTION → ADD ALERT TO GROUP ----------
    page.locator("#enrollment_groups_1 a", has_text="Action").click()
    page.get_by_text("Add Alert To Group(s)").click()
    page.wait_for_timeout(delay)

    # ---------- CLOSE PANEL ----------
    page.locator(".casegroups-index > div > .close-button-large").click()
    page.wait_for_timeout(delay)


def create_notification_group_2(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    add_users_to_notification_group(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing notification group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay
    # try:
    #     # Click Org/Hierarchy Selection
    #     zone_btn = page.locator("#notifier-settings-button").filter(has_text="Org/Hierarchy Selection").first
    #     zone_btn.wait_for(state="visible", timeout=10000)
    #     zone_btn.click()
    #
    #     # Fill search textbox and select zones
    #     search_box = page.locator("input[placeholder='Search']")
    #     zone_nodes = page.locator("div.tree-node-content")
    #     for zone in zones:
    #         search_box.fill(zone)
    #         page.wait_for_timeout(delay)
    #
    #         node = zone_nodes.filter(has=page.locator(f"span.textContents:has-text('{zone}')")).first
    #         checkbox = node.locator("i.fa-square-o, i.fa-minus-square-o")
    #         if checkbox.count() > 0:
    #             checkbox.first.click(force=True)
    #             page.wait_for_timeout(delay)
    #
    #     # Click Save
    #     save_btn = page.locator('[ng-click="saveSelectedRegionsCameras()"]').first
    #     save_btn.scroll_into_view_if_needed()
    #     save_btn.click(force=True)
    #     page.wait_for_timeout(delay)
    #
    #     return True


def add_users_to_notification_group_2(page, ng, delay):
    logger.info("Adding users to notification group")

    # Open Users tab within NG Details
    page.locator("//li[contains(@class,'panel-div')]//button[normalize-space()='Users']").click()
    page.wait_for_timeout(delay)

    # Filter to Unlinked Users
    page.locator("#UserView a", has_text="Filter").click()
    page.wait_for_timeout(delay)
    page.locator("#UserView a", has_text="Unlinked Users").click()
    page.wait_for_timeout(delay)
    user_rows = page.locator("#UserView li.non-linked-list-menu-item")
    user_rows.first.wait_for(state="visible", timeout=3000)
    first_user_checkbox = user_rows.first.locator(
        ".right-menu-checkbox-container .icheckbox_polaris ins.iCheck-helper"
    )
    first_user_checkbox.scroll_into_view_if_needed()
    first_user_checkbox.wait_for(state="visible", timeout=10000)
    first_user_checkbox.click(force=True)
    page.wait_for_timeout(delay)
    page.locator("#UserView a", has_text="Action").click()
    page.wait_for_timeout(delay)
    added = False
    for text in ["Add User(s) to Alert"]:
        item = page.locator(f"//a[normalize-space()='{text}']")
        if item.count() > 0:
            item.first.click()
            added = True
            break


def select_single_group_in_notifier(page, group):
    try:
        # Open the group selection dropdown
        page.locator(
            "div[ng-click='displayGroupSelection();']:has-text('Enrollment Group Selection')"
        ).click()

        # Wait for input box
        input_box = page.locator("#groupFilter")
        input_box.wait_for(state="visible", timeout=5000)

        # Type group name in search box
        input_box.fill(group)
        page.keyboard.press("Enter")
        page.wait_for_timeout(delay)  # small delay for filter to apply

        # Click the radio button corresponding to the group
        radio_btn = page.locator(f"li:has(p:text-is('{group}')) input[type='radio']")
        radio_btn.wait_for(state="visible", timeout=5000)
        radio_btn.click()

        # Click Save
        save_btn = page.locator("div[ng-click='saveGroupSelection(); $event.stopPropagation();']")
        save_btn.wait_for(state="visible", timeout=5000)
        save_btn.click()
        return True

    except Exception as e:
        print(f"Notifier group selection failed for '{group}': {e}")
        page.screenshot(
            path=f"notifier_group_selection_failure_{group}.png", full_page=True
        )
        return False


def configure_notifier_settings(page, number_of_events: int, photo_size: str, sound_option: str):
    try:
        # Click first visible Notifier Settings button
        page.locator("#notifier-settings-button", has_text="Notifier Settings").first.click()

        # Dictionary of dropdowns: label text -> (ng-model, option value)
        dropdowns = {
            "# Of Probable Match Events Displayed": ("currentNotifierSettingsObj.numberOfEventsToDisplay",
                                                     str(number_of_events)),
            "Photo Size": ("currentNotifierSettingsObj.photoSize", photo_size),
            "Sound Option": ("currentNotifierSettingsObj.soundOption", sound_option)
        }

        # Loop through each dropdown and select value if it exists
        for label_text, (ng_model, value) in dropdowns.items():
            page.locator("p", has_text=label_text).wait_for(state="visible", timeout=5000)
            dropdown = page.locator(f"select[ng-model='{ng_model}']")
            if dropdown.locator(f"option[label='{value}']").count() > 0:
                dropdown.select_option(label=value)

        # Click Save button
        save_button = page.locator("a", has_text="Save")
        save_button.wait_for(state="visible", timeout=5000)
        save_button.click()

    except Exception as e:
        print("Error configuring notifier settings:", e)
        # configure settings method completed


def is_group_displayed(page, group_name: str) -> bool:
    try:
        # Locate the container that specifically shows Selected Groups
        container = page.locator(
            "div.zone-filters-band-container:has(div.search-fields-heading:has-text('Selected Group(s)'))"
        )
        container.wait_for(state="visible", timeout=5000)

        # Look for the group inside the container
        group_elements = container.locator("div.search-field-pill-text")
        for i in range(group_elements.count()):
            if group_elements.nth(i).inner_text().strip().lower() == group_name.lower():
                print(f"Group '{group_name}' is displayed.")
                return True

        print(f"Group '{group_name}' is NOT displayed.")
        return False

    except Exception as e:
        print("Error checking selected group:", e)
        return False


def set_refresh_rate_and_save(page, refresh_value: str):
    try:
        # Open Notifier Settings (handles multiple buttons safely)
        page.locator("#notifier-settings-button", has_text="Notifier Settings").first.click()

        # Wait for Refresh Rate label
        page.locator("p", has_text="Refresh Rate").wait_for(state="visible", timeout=5000)

        # Select refresh rate if option exists
        dropdown = page.locator("select[ng-model='currentNotifierSettingsObj.refreshRate']")
        if dropdown.locator(f"option[label='{refresh_value}']").count() > 0:
            dropdown.select_option(label=refresh_value)

        # Click Save button
        save_button = page.locator("//a[@ng-click='saveSettings()']").click()
        save_button.wait_for(state="visible", timeout=5000)
        save_button.click()
    except Exception as e:
        print(f"Failed to set refresh rate '{refresh_value}':", e)

        # Ntifier methods coompleted#

    # if not added:
    #     page.locator("//a[contains(normalize-space(),'Add User') and contains(normalize-space(),'Group')]").first.click()
    #
    # page.wait_for_timeout(delay)
    # page.screenshot(path=f"screenshots/_5_NG_creation_success_{ng['name']}_linking_user.png")
    #
    # logger.info("Closing Users panel")
    # # Close Users panel via its header close button (per your HTML)
    # users_close = page.locator(
    #     "//div[contains(@class,'panel-heading-container')][.//p[normalize-space()='Users']]//div[contains(@class,'close-button-large')]"
    # )
    # users_close.wait_for(state="visible", timeout=10000)
    # users_close.click(force=True)
    #
    # # SPA hides the panel; do not wait for 'detached'
    # page.locator("#UserView").wait_for(state="hidden", timeout=10000)
    # page.wait_for_timeout(delay)


# Audit Log report #####################

from datetime import datetime
import os


def identify_and_enroll(page, image_path, basis_value, internal_group, region_keyword, store_id, enrollment_number, score, action_text, date_time=None):
    status = []

    # ---------- Identify & Enroll menu ----------
    ie_menu = page.locator(
        "//div[@id='dashboard-menu-container']//div[contains(@ng-click,'identify-and-enroll')]"
    )
    ie_menu.wait_for(state="visible", timeout=15000)
    ie_menu.scroll_into_view_if_needed()
    ie_menu.hover()
    ie_menu.click()
    status.append(True)

    # ---------- Resolve PROJECT_ROOT dynamically ----------
    CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(CURRENT_FILE_DIR, "datas")):
        parent = os.path.dirname(CURRENT_FILE_DIR)
        if parent == CURRENT_FILE_DIR:
            raise RuntimeError("Project root not found (datas folder missing)")
        CURRENT_FILE_DIR = parent

    PROJECT_ROOT = CURRENT_FILE_DIR

    # ---------- Resolve image path ----------
    # If user passes relative path, assume it's inside datas/Auditlog_images
    if not os.path.isabs(image_path):
        image_path = os.path.join(
            PROJECT_ROOT,
            "datas",
            "Auditlog_images",
            image_path
        )

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # ---------- Upload image ----------
    page.locator("input[type='file']").set_input_files(image_path)

    # ---------- Click Identify / Enroll ----------
    upload_button = page.locator(
        "div[ng-click='upload()'][ng-show*='identify-and-enroll']"
    )
    upload_button.wait_for(state="visible")
    upload_button.click()

    page.wait_for_timeout(5000)

    # ---------- Add Details panel ----------
    add_details_panel = page.locator('//*[text()="Add Details"]')
    status.append(add_details_panel.is_visible())

    # ---------- Dropdowns ----------
    page.locator('select[name="basis"]').select_option(basis_value)
    page.locator('select[name="internal_group"]').select_option(internal_group)
    page.wait_for_timeout(delay)

    # ---------- Region selection ----------
    region_select_btn = page.locator("//div[@ng-bind=\"'SELECT' | i18n\"]")
    if region_select_btn.is_visible():
        region_select_btn.click()
        status.append(True)
    else:
        status.append(False)

    regions = page.locator(
        '//region-search/div/div/div/div/ol/li/div/'
        'following-sibling::ol/li/following-sibling::li//li/div'
    ).all()

    for region in regions:
        if region_keyword.lower() in region.inner_text().lower():
            region.click()
            status.append(True)
            break

    save_btn = page.locator("//div[@ng-bind=\"'Save' | i18n\"]")
    if save_btn.is_visible():
        save_btn.click()
        status.append(True)
    else:
        status.append(False)

    # ---------- Fill details ----------
    page.locator('input[name="storeId"]').fill(store_id)
    page.locator('input[name="enrollmentNumber"]').fill(enrollment_number)
    page.get_by_role("spinbutton").fill(score)

    if not date_time:
        date_time = datetime.now().strftime("%Y-%m-%dT%H:%M")

    page.get_by_placeholder("mm/dd/yyyy HH:mm").fill(date_time)
    page.locator('input[name="action"]').fill(action_text)

    page.wait_for_timeout(delay)

    # ---------- Final Save ----------
    final_save_btn = page.locator('//a[text()="Save"]')
    if final_save_btn.is_visible() and final_save_btn.is_enabled():
        final_save_btn.click()
        status.append(True)
    else:
        status.append(False)

    page.wait_for_timeout(delay)

    # ---------- Success Message ----------
    success_msg = page.locator('//*[contains(text(), "Success!")]')
    status.append(success_msg.is_visible())

    return status


def create_notification_group_3(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    # page.wait_for_timeout(delay)  # Explicit delay
    # logger.info("Closing notification group creation panel")
    # page.wait_for_timeout(delay)  # Explicit delay
    # page.locator("li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def add_users_to_notification_group_3(page, ng, delay):
    logger.info("Adding users to notification group")

    # Open Users tab within NG Details
    # page.locator("//li[contains(@class,'panel-div')]//button[normalize-space()='Users']").click()
    page.get_by_role("button", name="Users").click()
    page.wait_for_timeout(delay)

    # Filter to Unlinked Users
    page.locator("#UserView a", has_text="Filter").click()
    page.wait_for_timeout(delay)
    page.locator("#UserView a", has_text="Unlinked Users").click()
    page.wait_for_timeout(delay)

    # Select first user checkbox
    user_rows = page.locator("#UserView li.non-linked-list-menu-item")
    user_rows.first.wait_for(state="visible", timeout=3000)
    first_user_checkbox = user_rows.first.locator(
        ".right-menu-checkbox-container .icheckbox_polaris ins.iCheck-helper"
    )
    first_user_checkbox.scroll_into_view_if_needed()
    first_user_checkbox.wait_for(state="visible", timeout=10000)
    first_user_checkbox.click(force=True)
    page.wait_for_timeout(delay)

    # Click Action → Add User(s) to Alert
    page.locator("#UserView a", has_text="Action").click()
    page.wait_for_timeout(delay)
    added = False
    for text in ["Add User(s) to Alert"]:
        item = page.locator(f"//a[normalize-space()='{text}']")
        if item.count() > 0:
            item.first.click()
            added = True
            break
    if not added:
        page.locator("//a[contains(normalize-space(),'Add User') and contains(normalize-space(),'Group')]").first.click()

    page.wait_for_timeout(delay)
    page.screenshot(path=f"screenshots/_5_NG_creation_success_{ng['name']}_linking_user.png")

    logger.info("Closing Users panel")
    # Close only the Users panel, keep NG Details panel open
    users_close = page.locator(
        "//div[contains(@class,'panel-heading-container')][.//p[normalize-space()='Users']]//div[contains(@class,'close-button-large')]"
    )
    users_close.wait_for(state="visible", timeout=10000)
    users_close.click(force=True)

    # Wait for Users panel to hide
    page.locator("#UserView").wait_for(state="hidden", timeout=10000)
    page.wait_for_timeout(delay)


def add_eg_to_notification_group_3(page, ng, delay):
    logger.info("Adding Enrollment Group to Notification Group")

    # Open Enrollment Groups tab inside NG Details
    page.get_by_role("button", name="Enrollment Groups").click()
    page.wait_for_timeout(delay)

    # Open Filter
    page.locator("#enrollment_groups_1 a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)

    # Select Unlinked Enrollment Groups
    page.locator("a").filter(has_text="Unlinked Enrollment Groups").click()
    page.wait_for_timeout(delay)

    # Select EG checkbox (iCheck)
    page.locator("#enrollment_groups_1") \
        .get_by_role("listitem") \
        .filter(has_text=ng["eg_name"]) \
        .get_by_role("insertion") \
        .click()
    page.wait_for_timeout(delay)

    # Click Action → Add Alert To Group(s)
    page.locator("#enrollment_groups_1 a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)
    page.get_by_text("Add Alert To Group(s)").click()
    page.wait_for_timeout(delay)

    page.screenshot(path=f"screenshots/_6_NG_{ng['name']}_linked_EG_{ng['eg_name']}.png")

    logger.info("Closing Enrollment Groups panel")
    # Close only Enrollment Groups panel, keep NG Details panel open
    page.locator(".casegroups-index > div > .close-button-large").click()
    page.wait_for_timeout(delay)


def create_notification_group_4(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing notification group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_notification_group_5(page, ng, delay):
    logger.info(f"Creating notification group: {ng['name']}")
    page.locator("a").filter(has_text="Action").click()
    logger.info("Clicked action dropdown")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Notification Group").click()
    logger.info("Creating notification group")
    page.wait_for_timeout(delay)  # Explicit delay
    fill_notification_group_details(page, ng, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing notification group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_enrollment_group_1(page, eg, delay):
    logger.info(f"Creating enrollment group: {eg['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Enrollment Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_enrollment_group_details_1(page, eg, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing enrollment group creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def fill_enrollment_group_details_1(page, eg, delay):
    logger.info("Filling in enrollment group details")
    page.get_by_role("textbox", name="Name").fill(eg["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Description").fill(eg["name"] + "_des")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"faceThreshold\"]").fill("0.84")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").clear()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"maskedFaceThreshold\"]").fill("0.85")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Save", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_enrollment_group_2(page, eg, delay):
    logger.info(f"Creating enrollment group: {eg['name']}")
    # Action → Create Enrollment Group
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)
    page.get_by_text("Create Enrollment Group").click()
    page.wait_for_timeout(delay)
    # Fill EG details and save
    fill_enrollment_group_details_1(page, eg, delay)
    page.wait_for_timeout(delay)


def add_ng_to_eg(page, ng_name, delay=3000):
    logger.info(f"Linking NG '{ng_name}' to EG")

    # Click Notification Groups button inside EG Details panel
    page.locator("//button[.//div[normalize-space()='Notification Groups']]"
    ).click()
    page.wait_for_timeout(delay)

    # Filter → Unlinked Notification Groups
    page.locator("#AlertGroupIndex a").filter(has_text="Filter").click()
    page.wait_for_timeout(delay)

    page.get_by_text("Unlinked Notification Groups").click()
    page.wait_for_timeout(delay)

    # Select the Notification Group
    page.locator("#AlertGroupIndex") \
        .get_by_role("listitem") \
        .filter(has_text=ng_name) \
        .get_by_role("insertion") \
        .click()
    page.wait_for_timeout(delay)

    # Action → Add To Enrollment Groups
    page.locator("#AlertGroupIndex a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)

    page.get_by_text("Add To Enrollment Groups").click()
    page.wait_for_timeout(delay)

    # Close Notification Groups panel
    page.locator(
        "#AlertGroupIndex > .panel-heading-container > .close-button-large"
    ).click()
    page.wait_for_timeout(delay)


def add_enrollment_to_eg(page, delay):
    logger.info("Linking Enrollment to Enrollment Group")

    # STEP 1: Click Enrollments inside EG-Details panel
    enrollments_btn = page.locator(
        "//button[.//div[normalize-space()='Enrollments']]"
    )
    enrollments_btn.wait_for(state="visible", timeout=10000)
    enrollments_btn.click()
    page.wait_for_timeout(delay)

    # STEP 2: Open Filter → Unlinked Enrollments
    page.locator("#people_2 a", has_text="Filter").click()
    # page.wait_for_timeout(delay)

    page.locator("a").filter(has_text="UnlinkedEnrollments").click()
    page.wait_for_timeout(delay)
    first_checkbox = page.locator(
        "//div[@id='people_2']//ins[contains(@class,'iCheck-helper')]"
    ).first

    first_checkbox.wait_for(state="visible", timeout=10000)
    first_checkbox.click(force=True)
    page.wait_for_timeout(delay)
    page.locator("#people_2 a").filter(has_text="Action").click()
    page.locator("#people_2").get_by_text("Add Enrollment To Group(s)").click()
    page.locator("#people_2 > .panel-heading-container > .close-button-large").click()
    page.locator(".controller-panel-div.posrel.fltlft.disblk.med-panel-width > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)


def add_enrollment_to_eg_1(page, delay=3000):
    logger.info("Linking Enrollment to Enrollment Group")

    # STEP 1: Click Enrollments inside EG Details panel
    enrollments_btn = page.locator(
        "//button[.//div[normalize-space()='Enrollments']]"
    )
    enrollments_btn.wait_for(state="visible", timeout=10000)
    enrollments_btn.click()
    page.wait_for_timeout(delay)

    # STEP 2: Filter → Unlinked Enrollments
    page.locator("#people_2 a", has_text="Filter").click()
    page.wait_for_timeout(delay)

    page.locator("a", has_text="UnlinkedEnrollments").click()
    page.wait_for_timeout(delay)

    # STEP 3: Select first enrollment checkbox
    first_checkbox = page.locator(
        "//div[@id='people_2']//ins[contains(@class,'iCheck-helper')]"
    ).first
    first_checkbox.wait_for(state="visible", timeout=10000)
    first_checkbox.click(force=True)
    page.wait_for_timeout(delay)

    # STEP 4: Action → Add Enrollment To Group(s)
    page.locator("#people_2 a", has_text="Action").click()
    page.wait_for_timeout(delay)

    page.locator(
        "#people_2 a",
        has_text="Add Enrollment To Group(s)"
    ).click()
    page.wait_for_timeout(delay)

    # STEP 5: Close ONLY Enrollments panel
    page.locator(
        "#people_2 > .panel-heading-container > .close-button-large"
    ).click()
    page.wait_for_timeout(delay)


def select_zones_in_notifier(page, zones):
    try:
        # Click Org/Hierarchy Selection
        zone_btn = page.locator("#notifier-settings-button").filter(has_text="Org/Hierarchy Selection").first
        zone_btn.wait_for(state="visible", timeout=10000)
        zone_btn.click()

        # Fill search textbox and select zones
        search_box = page.locator("input[placeholder='Search']")
        zone_nodes = page.locator("div.tree-node-content")

        for zone in zones:
            search_box.fill(zone)
            page.wait_for_timeout(delay)

            node = zone_nodes.filter(has=page.locator(f"span.textContents:has-text('{zone}')")).first
            checkbox = node.locator("i.fa-square-o, i.fa-minus-square-o")
            if checkbox.count() > 0:
                checkbox.first.click(force=True)
                page.wait_for_timeout(delay)

        # Click Save
        save_btn = page.locator('[ng-click="saveSelectedRegionsCameras()"]').first
        save_btn.scroll_into_view_if_needed()
        save_btn.click(force=True)
        page.wait_for_timeout(delay)

        return True

    except Exception as e:
        print("Failed in selecting zones:", e)
        page.screenshot(path="notifier_zone_selection_error.png", full_page=True)
        return False


def get_notifier_group_by_index(index=0):
    if not Notifier_groups:
        raise ValueError("Notifier_groups is empty")

    if index < 0 or index >= len(Notifier_groups):
        raise IndexError("Invalid group index")

    selected_group = Notifier_groups[index]
    reordered_groups = [selected_group] + [
        g for i, g in enumerate(Notifier_groups) if i != index
    ]

    return selected_group, reordered_groups


############## VSJ  ########################


def is_descending_order(values):
    def natural_key(value):
        return [
            int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', value.strip())
        ]

    keys = [natural_key(v) for v in values]
    return all(keys[i] >= keys[i + 1] for i in range(len(keys) - 1))


def is_descending_order_calendar_dates(values):
    dates = [
        datetime.strptime(v.strip(), "%b %d, %Y %I:%M %p")
        for v in values
    ]
    return dates == sorted(dates, reverse=True)


def _close_user_details_and_role_panels(page, notes_list=None):
    if notes_list is None:
        notes_list = []

    try:
        for _ in range(6):
            close_icons = page.locator("//i[contains(@class,'fa-times') and not(contains(@class,'ng-hide'))]")
            count = close_icons.count()
            if count == 0:
                break
            close_icons.nth(count - 1).click()
            page.wait_for_timeout(250)
    except Exception:
        pass

    try:
        closes = page.locator("//a[normalize-space()='Close']")
        count = closes.count()
        for i in range(count):
            try:
                closes.nth(i).click()
                page.wait_for_timeout(delay)
            except Exception:
                pass
    except Exception:
        pass

    try:
        for _ in range(2):
            page.keyboard.press("Escape")
            page.wait_for_timeout(delay)
    except Exception:
        pass

    notes_list.append("INFO: Closed user details & role panels")


def fill_user_details_for_useralertschedule(page, user, credentials, delay):
    logger.info("Filling in user details")

    page.get_by_role("textbox", name="Username", exact=True).fill(user["username"])
    logger.info("Filled Username")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="First Name").fill(user["username"] + "F")
    logger.info("Filled First Name")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="Last Name").fill(user["username"] + "L")
    logger.info("Filled Last Name")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"userRoleId\"]").select_option(user["role_id"])
    logger.info("Selected User Role")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="New Password").click()
    page.get_by_role("textbox", name="New Password").fill("Right_1r1s")
    page.wait_for_timeout(delay)
    page.get_by_role("textbox", name="Confirm Password").click()
    page.get_by_role("textbox", name="Confirm Password").fill("Right_1r1s")

    page.get_by_text("Region Selection").click()
    logger.info("Clicked Region Selection")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_text(user["region"]).click()
    logger.info("Selected Region")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("region-search").get_by_text("Save").click()
    logger.info("Clicked Save in Region Search")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name='storeGroupId']").select_option("sg01")
    logger.info("Selected first Store Group by value")
    page.wait_for_timeout(delay)

    page.get_by_role("textbox", name="User Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled User Email")
    page.wait_for_timeout(delay)  # Explicit delay

    page.get_by_role("textbox", name="Alert Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled Alert Email")
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        page.locator("select[name=\"timezoneId\"]").select_option(user["timezone"])
    except Exception as e:
        logger.info(f"{e}")
        page.locator("select[name=\"timezoneID\"]").select_option(user["timezone"])

    logger.info("Selected Timezone")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("a").filter(has_text="Save").click()
    logger.info("Clicked Save")
    page.wait_for_timeout(delay)  # Explicit delay


def create_user_for_useralertschedule(page, user, credentials, delay):
    logger.info(f"Creating user: {user['username']}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create User", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_user_details_for_useralertschedule(page, user, credentials, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Verifying user creation")
    page.wait_for_timeout(delay)  # Explicit delay
    assert page.get_by_text("Success! A user has been created.").is_visible()
    page.wait_for_timeout(delay)  # Explicit delay
    page.screenshot(path=f"screenshots/_2_user_creation_success_{user['username']}.png")
    page.wait_for_timeout(delay)  # Explicit delay
    logger.info("Closing user creation panel")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > .panel-heading-container > .close-button-large"
    ).first.click()
    page.wait_for_timeout(delay)  # Explicit delay


def select_start_date_previous_month(page, delay):
    # ---------------- SELECT START DATE CHECKBOX ----------------
    start_checkbox = page.locator("//input[@id='userSelectedStartDateEl']")
    if not start_checkbox.is_checked():
        start_checkbox.check()
        page.wait_for_timeout(delay)

    # ---------------- CLICK START DATE FIELD TO OPEN DATEPICKER ----------------
    page.click("//input[@id='startDateField']")
    page.wait_for_timeout(delay)

    # ---------------- CLICK PREVIOUS MONTH BUTTON ----------------
    page.get_by_title("Previous Month").click()  # Adjust selector if necessary
    page.wait_for_timeout(delay)
    # ---------------- SELECT DATE (FROM CONFTEST) ----------------
    day = conftest.search_date.day

    try:
        page.locator(
            f"//td[not(contains(@class,'old')) "
            f"and not(contains(@class,'new')) "
            f"and normalize-space()='{day}']"
        ).first.click()
    except Exception as e:
        logger.info(f"{e}")
        page.get_by_role("cell", name=str(day)).first.click()

    page.wait_for_timeout(delay)
    # day = 1
    # page.locator(
    #     f"//td[not(contains(@class,'old')) and not(contains(@class,'new')) and normalize-space()='{day}']"
    # ).first.click()
    # page.wait_for_timeout(delay)

    # Set the time
    page.get_by_title("Select Time").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Pick Hour").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("cell", name=conftest.search_time.strftime("%I")).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Pick Minute").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("cell", name=conftest.search_time.strftime("%M")).click()
    page.wait_for_timeout(delay)  # Explicit delay
    # page.get_by_role("button", name=conftest.search_time.strftime("%p")+" Toggle AM/PM").click()
    # toggle_am_pm = conftest.search_time.strftime("%p")
    if conftest.search_time.strftime("%p") == "AM":
        page.get_by_title("Toggle Period").click()
        page.get_by_title("Toggle Period").click()
    else:
        page.get_by_title("Toggle Period").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_title("Close the picker").click()
    page.wait_for_timeout(delay)  # Explicit delay


def create_user_with_all_details(page, USERS_WITH_ALL_DETAILS, delay=500):
    user = USERS_WITH_ALL_DETAILS[1]
    logger.info(f"Creating user: {user['username']}")

    page.wait_for_timeout(delay)
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)
    page.get_by_text("Create User", exact=True).click()
    page.wait_for_timeout(delay)

    page.fill("//input[@name='usersusername']", user["username"])
    page.get_by_role("textbox", name="First Name").fill(user["username"] + "F")
    logger.info("Filled First Name")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Last Name").fill(user["username"] + "L")
    logger.info("Filled Last Name")
    page.wait_for_timeout(delay)  # Explicit delay
    page.fill("//input[@name='newpassword']", PASSWORD)
    logger.info("Filled new pwd")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='confirmpassword']", PASSWORD)
    logger.info("Filled confirm pwd")
    page.wait_for_timeout(delay)
    page.select_option("//select[@name='userRoleId']", label=user["userRole"])
    logger.info("Selected user role")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='company']", user["company"])
    logger.info("Filled company name")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='title']", user["title"])
    logger.info("Filled title")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='department']", user["department"])
    logger.info("Filled department")
    page.wait_for_timeout(delay)
    page.click("//div[contains(@class,'selectRegion') and normalize-space()='Region Selection']")
    logger.info("Selecting region")
    page.wait_for_timeout(delay)
    page.click(f"(//div[contains(@class,'tree-node-content')])[{user['region_index']}]")
    page.wait_for_timeout(delay)
    page.click("//div[contains(@class,'toolbar-btn') and normalize-space()='Save']")
    logger.info("Selected and saved region")
    page.wait_for_timeout(delay)
    page.get_by_role("textbox", name="User Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled User Email")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Alert Email").fill(user["username"] + "@facefirst.com")
    logger.info("Filled Alert Email")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='alertPhone']", user["alertphone"])
    logger.info("Filled alert phone")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='address1']", user["address1"])
    logger.info("Filled address 1")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='address2']", user["address2"])
    logger.info("Filled address 2")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='city']", user["city"])
    logger.info("Filled city")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='state']", user["state"])
    logger.info("Filled state")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='postalcode']", user["postalcode"])
    logger.info("Filled postal code")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='homephone']", user["homephone"])
    logger.info("Filled home phone number")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='workphone']", user["workphone"])
    logger.info("Filled work phone number")
    page.wait_for_timeout(delay)
    page.fill("//input[@name='faxphone']", user["faxphone"])
    logger.info("Filled fax phone")
    page.wait_for_timeout(delay)
    page.select_option("//select[@ng-model='user.prefs.phoneType']", label=user["phonetype"])
    logger.info("Selected photo type")
    page.wait_for_timeout(delay)
    page.select_option("//select[@ng-model='user.prefs.provider']", label=user["phoneprovider"])
    logger.info("Selected phone provider")
    page.wait_for_timeout(delay)
    page.select_option("//select[@name='timezoneId']", value=user["timezone"])
    logger.info("Selected timezone")
    page.wait_for_timeout(delay)
    page.wait_for_selector("//a[contains(@ng-click,'saveUserEditClicked') and not(@disabled)]")
    logger.info("Saved user details")
    page.wait_for_timeout(delay)
    page.locator("//a[contains(@ng-click,'saveUserEditClicked')]").click(force=True)
    page.wait_for_timeout(delay)
    assert page.get_by_text("Success! A user has been created.").is_visible()
    page.screenshot(path=f"screenshots/user_created_{user['username']}.png")
    page.locator(
        "li:nth-child(2) > .panel-div > .controller-panel-div > "
        ".panel-heading-container > .close-button-large"
    ).first.click()


def save_screenshot(page, name, screenshot_path):
    try:
        path_obj = screenshot_path if isinstance(screenshot_path, Path) else Path(screenshot_path)
        path_obj.mkdir(parents=True, exist_ok=True)

        file_path = path_obj / f"{name}.png"
        print(f'file_path: {file_path}')
        page.screenshot(path=file_path)
        print(f"Screenshot saved at: {file_path}")

    except Exception as ex:
        print(f"save_screenshot error: {type(ex).__name__} - {ex}")


def date_days_back(days):
    return (datetime.now() - timedelta(days=days)).strftime("%d/%m/%Y")


def loginuser(page, username, password=PASSWORD):
    page.context.clear_cookies()
    page.goto(BASE_URL, wait_until="load")
    page.wait_for_selector("//input[@id='login-username']", timeout=60000)
    page.fill("//input[@id='login-username']", username)
    page.wait_for_selector("//input[@id='login-password']", timeout=60000)
    page.fill("//input[@id='login-password']", password)
    page.click('//div[@ng-click="login()"]')
    # agree_to_term(page, delay)
    # page.wait_for_selector("#dashboard-menu-container", timeout=10000)


def enroll_disabled_subject(page, subject, group, organization, index, delay):
    import os
    from datetime import datetime

    status = []
    subject_name = os.path.splitext(os.path.basename(subject))[0]
    logger.info(f"Enrolling disabled subject: {subject_name}")

    page.get_by_text("Identify & Enroll").click()
    page.wait_for_timeout(delay)

    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)

    page.locator(
        "(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]"
    ).click()
    page.wait_for_timeout(delay)

    try:
        page.inner_text("//div/p[contains(text(), 'Add Details')]")
    except Exception:
        page.locator(
            "div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)"
        ).click()
        page.wait_for_timeout(delay)

    page.locator("select[name='basis']").select_option("number:3")
    page.wait_for_timeout(delay)

    internal_group, spinbutton_value = group
    page.locator("select[name='internal_group']").select_option(internal_group)
    page.wait_for_timeout(delay)

    page.get_by_text("SELECT", exact=True).click()
    page.wait_for_timeout(delay)
    page.get_by_text(organization).click()
    page.wait_for_timeout(delay)
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)

    page.locator("input[name='storeId']").fill(f"store_{subject_name}")
    page.locator("input[name='enrollmentNumber']").fill(f"enroll_{subject_name}")
    page.get_by_role("spinbutton").fill(spinbutton_value)

    input_box = page.get_by_placeholder("mm/dd/yyyy HH:mm")
    fill_value = datetime.now().strftime("%Y-%m-%dT%H:%M")
    input_box.fill(fill_value)

    page.locator("input[name='action']").fill(f"action_{subject_name}")

    page.locator("a.btn.toolbar-btn.nav-pills-small.tac[ng-click^='save(']").click()
    page.wait_for_timeout(10000)

    # ---------- Review Enrollment Details ----------
    page.locator(
        "//button[.//span[normalize-space()='Review Enrollment Details']]"
    ).click()
    page.wait_for_timeout(delay)

    # ---------- Action → Edit ----------
    page.locator(
        "//span[@class='dropdown-btn-label' and normalize-space()='Action']"
    ).click()
    page.wait_for_timeout(delay)

    page.locator("//a[normalize-space()='Edit']").click()
    page.wait_for_timeout(delay)

    # ---------- Disable Enrollment ----------
    page.locator(
        "//label[.//span[normalize-space()='Disabled']]"
    ).click()
    page.wait_for_timeout(delay)

    # ---------- Select Disabled Reason ----------
    disabled_reasons = [
        "Opt-out",
        "Poor Image Quality",
        "Duplicate Enrollment",
        "Enrollment Criteria"
    ]

    selected_reason = disabled_reasons[index % len(disabled_reasons)]

    page.locator(
        "//select[@name='disabledReason']"
    ).select_option(label=selected_reason)

    page.wait_for_timeout(delay)

    logger.info(
        f"Enrollment {subject_name} disabled with reason: {selected_reason}"
    )
    # ---------- Save Disabled Enrollment ----------
    page.locator(
        "//a[normalize-space()='Save' and contains(@class,'toolbar-btn')]"
    ).click()
    page.wait_for_timeout(delay)

    details_panel = page.locator(
        "//p[normalize-space()='Enrollment - Details']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
    )
    disabled_label = details_panel.locator(
        "xpath=.//span[contains(@class,'disabled-label-large') and not(contains(@class,'ng-hide'))]"
        "//span[normalize-space()='Disabled']"
    )
    if disabled_label.is_visible():
        status.append(True)
    else:
        status.append(False)

    # ---------- Close Enrollment Details Panel ----------
    page.locator(
        "//p[normalize-space()='Enrollment - Details']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
        "//div[contains(@class,'close-button-large')]"
    ).click()
    page.wait_for_timeout(delay)

    logger.info(
        f"Enrollment disabled, saved, and closed for subject: {subject_name}"
    )

    page.locator(
        "//p[normalize-space()='Identify & Enroll']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
        "//div[contains(@class,'close-button-large')]"
    ).click()
    page.wait_for_timeout(delay)
    logger.info(
        f"Disabled enrollment completed: "
        f"store_{subject_name}, enroll_{subject_name}, action_{subject_name}"
    )


def verify_disabled_opt_out_status_appears_in_search_criteria_on_top(page, delay):
    result = []

    disabled_reason_criteria = page.locator(
        "//div[@ng-bind=\"('Disabled Reason' | i18n)+': '+(disabledReasonKey)\"]"
    )

    # Visibility check
    if disabled_reason_criteria.is_visible():
        result.append(True)
        logger.info("Disabled Reason criteria visible at top")
    else:
        result.append(False)
        logger.info("Disabled Reason criteria not visible at top")

    # Text validation
    if "Opt-out" in disabled_reason_criteria.inner_text():
        result.append(True)
        logger.info(
            f"Disabled Reason value visible at top: {disabled_reason_criteria.inner_text()}"
        )
    else:
        result.append(False)
        logger.info("Disabled Reason value not matching Opt-out")

    page.wait_for_timeout(delay)

    # Remove criteria button
    remove_disabled_reason_button = page.locator(
        "//div[@ng-click=\"removeDisabledReasonFromSearch( )\"]"
    )

    if remove_disabled_reason_button.is_visible():
        result.append(True)
        logger.info("Remove Disabled Reason criteria button is visible")
    else:
        result.append(False)
        logger.info("Remove Disabled Reason criteria button is not visible")

    page.wait_for_timeout(delay)
    return result


def verify_disabled_opt_out_status_of_enrollments_in_enrollment_list(page, delay):
    result = []

    # -------- LOAD ALL ENROLLMENTS --------
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay_1_second)

    page.wait_for_timeout(delay_5_second)

    # -------- OPEN DETAILS FROM EXTEND MENU --------
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]'
    )

    count = menus.count()

    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        details_button.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        # -------- VERIFY DISABLED STATUS --------
        disabled_status = page.locator(
            '//span[@ng-show="enrollment.status===0" and contains(@class,"disabled-label-large")]'
        )

        # -------- VERIFY DISABLED REASON = OPT-OUT --------
        disabled_reason = page.locator('//td[normalize-space()="Opt-out"]')

        if disabled_status.is_visible() and "Opt-out" in disabled_reason.inner_text():
            result.append(True)
            logger.info("Enrollment is Disabled with reason: Opt-out")
        else:
            result.append(False)
            logger.warning(
                f"Verification failed | Status visible: {disabled_status.is_visible()} | "
                f"Reason text: {disabled_reason.inner_text()}"
            )

        page.wait_for_timeout(delay_2_second)

        # -------- CLOSE DETAILS PANEL --------
        page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()

        page.wait_for_timeout(delay_2_second)

    return result


def verify_disabled_poor_image_quality_status_appears_in_search_criteria_on_top(page, delay):
    result = []

    disabled_reason_criteria = page.locator(
        "//div[@ng-bind=\"('Disabled Reason' | i18n)+': '+(disabledReasonKey)\"]"
    )

    # Visibility check
    if disabled_reason_criteria.is_visible():
        result.append(True)
        logger.info("Disabled Reason criteria visible at top")
    else:
        result.append(False)
        logger.info("Disabled Reason criteria not visible at top")

    # Text validation
    if "Poor Image Quality" in disabled_reason_criteria.inner_text():
        result.append(True)
        logger.info(
            f"Disabled Reason value visible at top: {disabled_reason_criteria.inner_text()}"
        )
    else:
        result.append(False)
        logger.info("Disabled Reason value not matching Poor Image Quality")

    page.wait_for_timeout(delay)

    # Remove criteria button
    remove_disabled_reason_button = page.locator(
        "//div[@ng-click=\"removeDisabledReasonFromSearch( )\"]"
    )

    if remove_disabled_reason_button.is_visible():
        result.append(True)
        logger.info("Remove Disabled Reason criteria button is visible")
    else:
        result.append(False)
        logger.info("Remove Disabled Reason criteria button is not visible")

    page.wait_for_timeout(delay)
    return result


def verify_disabled_poor_image_quality_status_of_enrollments_in_enrollment_list(page, delay):
    result = []

    # -------- LOAD ALL ENROLLMENTS --------
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay_1_second)

    page.wait_for_timeout(delay_5_second)

    # -------- OPEN DETAILS FROM EXTEND MENU --------
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]'
    )

    count = menus.count()

    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        details_button.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        # -------- VERIFY DISABLED STATUS --------
        disabled_status = page.locator(
            '//span[@ng-show="enrollment.status===0" and contains(@class,"disabled-label-large")]'
        )

        # -------- VERIFY DISABLED REASON = OPT-OUT --------
        disabled_reason = page.locator('//td[normalize-space()="Poor Image Quality"]')

        if disabled_status.is_visible() and "Poor Image Quality" in disabled_reason.inner_text():
            result.append(True)
            logger.info("Enrollment is Disabled with reason: Poor Image Quality")
        else:
            result.append(False)
            logger.warning(
                f"Verification failed | Status visible: {disabled_status.is_visible()} | "
                f"Reason text: {disabled_reason.inner_text()}"
            )

        page.wait_for_timeout(delay_2_second)

        # -------- CLOSE DETAILS PANEL --------
        page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()

        page.wait_for_timeout(delay_2_second)

    return result


def verify_disabled_duplicate_enrollment_status_appears_in_search_criteria_on_top(page, delay):
    result = []

    disabled_reason_criteria = page.locator(
        "//div[@ng-bind=\"('Disabled Reason' | i18n)+': '+(disabledReasonKey)\"]"
    )

    # Visibility check
    if disabled_reason_criteria.is_visible():
        result.append(True)
        logger.info("Disabled Reason criteria visible at top")
    else:
        result.append(False)
        logger.info("Disabled Reason criteria not visible at top")

    # Text validation
    if "Duplicate Enrollment" in disabled_reason_criteria.inner_text():
        result.append(True)
        logger.info(
            f"Disabled Reason value visible at top: {disabled_reason_criteria.inner_text()}"
        )
    else:
        result.append(False)
        logger.info("Disabled Reason value not matching Duplicate Enrollment")

    page.wait_for_timeout(delay)

    # Remove criteria button
    remove_disabled_reason_button = page.locator(
        "//div[@ng-click=\"removeDisabledReasonFromSearch( )\"]"
    )

    if remove_disabled_reason_button.is_visible():
        result.append(True)
        logger.info("Remove Disabled Reason criteria button is visible")
    else:
        result.append(False)
        logger.info("Remove Disabled Reason criteria button is not visible")

    page.wait_for_timeout(delay)
    return result


def verify_disabled_duplicate_enrollment_status_of_enrollments_in_enrollment_list(page, delay):
    result = []

    # -------- LOAD ALL ENROLLMENTS --------
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay_1_second)

    page.wait_for_timeout(delay_5_second)

    # -------- OPEN DETAILS FROM EXTEND MENU --------
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]'
    )

    count = menus.count()

    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        details_button.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        # -------- VERIFY DISABLED STATUS --------
        disabled_status = page.locator(
            '//span[@ng-show="enrollment.status===0" and contains(@class,"disabled-label-large")]'
        )

        # -------- VERIFY DISABLED REASON = OPT-OUT --------
        disabled_reason = page.locator('//td[normalize-space()="Duplicate Enrollment"]')

        if disabled_status.is_visible() and "Duplicate Enrollment" in disabled_reason.inner_text():
            result.append(True)
            logger.info("Enrollment is Disabled with reason: Duplicate Enrollment")
        else:
            result.append(False)
            logger.warning(
                f"Verification failed | Status visible: {disabled_status.is_visible()} | "
                f"Reason text: {disabled_reason.inner_text()}"
            )

        page.wait_for_timeout(delay_2_second)

        # -------- CLOSE DETAILS PANEL --------
        page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()

        page.wait_for_timeout(delay_2_second)

    return result


def verify_disabled_enrollment_criteria_status_appears_in_search_criteria_on_top(page, delay):
    result = []

    disabled_reason_criteria = page.locator(
        "//div[@ng-bind=\"('Disabled Reason' | i18n)+': '+(disabledReasonKey)\"]"
    )

    # Visibility check
    if disabled_reason_criteria.is_visible():
        result.append(True)
        logger.info("Disabled Reason criteria visible at top")
    else:
        result.append(False)
        logger.info("Disabled Reason criteria not visible at top")

    # Text validation
    if "Enrollment Criteria" in disabled_reason_criteria.inner_text():
        result.append(True)
        logger.info(
            f"Disabled Reason value visible at top: {disabled_reason_criteria.inner_text()}"
        )
    else:
        result.append(False)
        logger.info("Disabled Reason value not matching Enrollment Criteria")

    page.wait_for_timeout(delay)

    # Remove criteria button
    remove_disabled_reason_button = page.locator(
        "//div[@ng-click=\"removeDisabledReasonFromSearch( )\"]"
    )

    if remove_disabled_reason_button.is_visible():
        result.append(True)
        logger.info("Remove Disabled Reason criteria button is visible")
    else:
        result.append(False)
        logger.info("Remove Disabled Reason criteria button is not visible")

    page.wait_for_timeout(delay)
    return result


def verify_disabled_enrollment_criteria_status_of_enrollments_in_enrollment_list(page, delay):
    result = []

    # -------- LOAD ALL ENROLLMENTS --------
    load_more = page.locator('//button[@ng-click="loadMore()"]')
    while load_more.is_visible():
        load_more.click()
        page.wait_for_timeout(delay_1_second)

    page.wait_for_timeout(delay_5_second)

    # -------- OPEN DETAILS FROM EXTEND MENU --------
    menus = page.locator('//div[@data-original-title="Extend Menu"]')
    details_button = page.locator(
        '//div[@ng-repeat="menuItem in buttonMenuArray" and @data-original-title="Details"]'
    )

    count = menus.count()

    for i in range(count):
        menus.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        details_button.nth(i).click()
        page.wait_for_timeout(delay_2_second)

        # -------- VERIFY DISABLED STATUS --------
        disabled_status = page.locator(
            '//span[@ng-show="enrollment.status===0" and contains(@class,"disabled-label-large")]'
        )

        # -------- VERIFY DISABLED REASON = OPT-OUT --------
        disabled_reason = page.locator('//td[normalize-space()="Enrollment Criteria"]')

        if disabled_status.is_visible() and "Enrollment Criteria" in disabled_reason.inner_text():
            result.append(True)
            logger.info("Enrollment is Disabled with reason: Enrollment Criteria")
        else:
            result.append(False)
            logger.warning(
                f"Verification failed | Status visible: {disabled_status.is_visible()} | "
                f"Reason text: {disabled_reason.inner_text()}"
            )

        page.wait_for_timeout(delay_2_second)

        # -------- CLOSE DETAILS PANEL --------
        page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()

        page.wait_for_timeout(delay_2_second)

    return result


def enroll_subject_with_expiration_date_and_disabled_reason(
    page,
    users,
    organization,
    delay,
    screenshot_path
):
    from datetime import datetime, timedelta
    import os

    status = []
    try:
        logger.info(
            "Starting enroll_subject_with_expiration_date_and_disabled_reason"
        )

        # ---------------- LOGIN ----------------
        login(page, username=users[0]["username"])
        agree_to_term(page, delay)

        page.wait_for_selector(
            "#dashboard-menu-container",
            state="visible",
            timeout=20000
        )

        # ---------------- TEST DATA ----------------
        subject_image = "datas/enrollSubjectWithExpirationDateRangeanddisabledReason/s1.png"
        subject_name = os.path.splitext(os.path.basename(subject_image))[0]

        logger.info(f"Enrolling subject: {subject_name}")

        # ---------------- IDENTIFY & ENROLL ----------------
        page.get_by_text("Identify & Enroll").click()
        page.wait_for_timeout(delay)

        file_input = page.locator("input[type='file']")
        file_input.wait_for(state="attached", timeout=15000)
        file_input.set_input_files(subject_image)
        page.wait_for_timeout(delay)

        page.locator(
            "(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]"
        ).click()
        page.wait_for_timeout(delay)

        try:
            page.inner_text("//div/p[contains(text(), 'Add Details')]")
        except Exception:
            page.locator(
                "div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)"
            ).click()
            page.wait_for_timeout(delay)

        # ---------------- ENROLLMENT DETAILS ----------------
        page.locator("select[name='basis']").select_option("number:3")
        page.wait_for_timeout(delay)

        page.locator("select[name='internal_group']").select_option(
            "abe (Serious Offender - Medium)"
        )
        page.wait_for_timeout(delay)

        page.get_by_text("SELECT", exact=True).click()
        page.wait_for_timeout(delay)

        page.get_by_text(organization).click()
        page.wait_for_timeout(delay)

        page.locator("region-search").get_by_text("Save").click()
        page.wait_for_timeout(delay)

        page.locator("input[name='storeId']").fill(f"store_{subject_name}")
        page.locator("input[name='enrollmentNumber']").fill(
            f"enroll_{subject_name}"
        )
        page.get_by_role("spinbutton").fill("300")

        # ---------------- ENROLLMENT DATE ----------------
        page.get_by_placeholder("mm/dd/yyyy HH:mm").fill(
            datetime.now().strftime("%Y-%m-%dT%H:%M")
        )

        page.locator("input[name='action']").fill(
            f"action_{subject_name}"
        )

        # ==================================================
        # ========== EXPIRATION DATE (1 WEEK) ===============
        # ==================================================
        page.locator("#EXPIRATION_DATE_WAS_SET").check()
        page.wait_for_timeout(delay)

        expiry_date = datetime.now() + timedelta(weeks=1)
        expiry_value = expiry_date.strftime("%m/%d/%Y %I:%M %p")

        expiration_input = page.locator("#expirationDateInputEl")
        expiration_input.click()
        page.wait_for_timeout(delay)
        expiration_input.fill(expiry_value)
        expiration_input.press("Tab")
        page.wait_for_timeout(delay)

        logger.info(f"Expiration date set to: {expiry_value}")

        # ---------------- SAVE ENROLLMENT ----------------
        page.locator("a.btn.toolbar-btn.nav-pills-small.tac[ng-click^='save(']").click()
        page.wait_for_timeout(10000)

        page.locator(
            "//button[.//span[normalize-space()='Review Enrollment Details']]"
        ).click()
        page.wait_for_timeout(delay)

        page.locator(
            "//span[@class='dropdown-btn-label' and normalize-space()='Action']"
        ).click()
        page.wait_for_timeout(delay)

        page.locator("//a[normalize-space()='Edit']").click()
        page.wait_for_timeout(delay)

        page.locator(
            "//label[.//span[normalize-space()='Disabled']]"
        ).click()
        page.wait_for_timeout(delay)

        disabled_reason_dropdown = page.locator("select[name='disabledReason']")
        disabled_reason_dropdown.wait_for(state="visible", timeout=5000)
        disabled_reason_dropdown.select_option("number:1")  # opt out
        page.wait_for_timeout(delay)
        page.wait_for_timeout(delay)

        logger.info("Enrollment disabled with reason: Opt out")

        # ---------------- SAVE DISABLED ----------------
        page.locator(
            "//a[normalize-space()='Save' and contains(@class,'toolbar-btn')]"
        ).click()
        page.wait_for_timeout(delay)

        details_panel = page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
        )
        disabled_label = details_panel.locator(
            "xpath=.//span[contains(@class,'disabled-label-large') and not(contains(@class,'ng-hide'))]"
            "//span[normalize-space()='Disabled']"
        )
        if disabled_label.is_visible():
            status.append(True)
        else:
            status.append(False)

        # ---------------- CLOSE PANELS ----------------
        page.locator(
            "//p[normalize-space()='Enrollment - Details']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()
        page.wait_for_timeout(delay)

        page.locator(
            "//p[normalize-space()='Identify & Enroll']"
            "/ancestor::div[contains(@class,'panel-heading-container')]"
            "//div[contains(@class,'close-button-large')]"
        ).click()
        page.wait_for_timeout(delay)

        logger.info(
            f"Enrollment completed: store_{subject_name}, "
            f"enroll_{subject_name}, action_{subject_name}"
        )
        logger.info(f"Status: {status}")
        if False in status:
            save_screenshot(page, "enroll_subject_with_expiration_date_and_disabled_reason", screenshot_path)
            logger.error('enroll_subject_with_expiration_date_and_disabled_reason')
            return False
        else:
            return True

    except Exception as e:
        logger.error(
            "enroll_subject_with_expiration_date_and_disabled_reason failed: "
            f"{e}"
        )
        save_screenshot(page, "enroll_subject_with_expiration_date_and_disabled_reason", screenshot_path)
        return False
    finally:
        logout_if_logged_in(page, delay)


def enroll_photo_origin_subject(page, subject, group, organization, index, delay, action_for_enrollment):
    status = []
    logger.info("Navigating to Identify & Enroll page")
    logger.info(f"Enrolling subject: {subject}")
    page.get_by_text("Identify & Enroll").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay

    # Verify photo origin verbiage
    photo_origin_verbiage = page.locator(
        "//label/span[contains(normalize-space(),"
        "'I have confirmed that the selected photo is not from an Illinois or Portland, Oregon source')]"
    )
    if photo_origin_verbiage.is_visible():
        logger.info("Photo origin verbiage is displayed")
        status.append(True)

    # CHECK the checkbox
    checkbox = page.locator("//input[@id='nonIllinoisPortland']")
    checkbox.check()
    logger.info("Photo origin checkbox checked")
    page.wait_for_timeout(delay)

    identify_enroll_locator = page.locator("xpath=(//div[@class='ff-mobile-button posrel fltlft disblk tac'])[2]")
    identify_enroll_locator.click()
    page.wait_for_timeout(delay)  # Explicit delay

    try:
        text = page.inner_text("//div/p[contains(text(), 'Add Details')]")
        print(text)
        logger.info(f"Add Details text is visible")
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.info(f"Add Details text is not visible")
        identify_enroll_locator = page.locator("div:nth-child(3) > .ff-mobile-bu-container > div:nth-child(2)")
        identify_enroll_locator.click()
        page.wait_for_timeout(delay)  # Explicit delay

    page.screenshot(path=f"screenshots/_8_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"basis\"]").select_option("number:3")
    page.wait_for_timeout(delay)  # Explicit delay

    internal_group, spinbutton_value = group
    page.wait_for_timeout(delay)  # Explicit delay

    page.locator("select[name=\"internal_group\"]").select_option(internal_group)
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("SELECT", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text(ORGANIZATION).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("region-search").get_by_text("Save").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"storeId\"]").fill(f"store_photoOrigin_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[name=\"enrollmentNumber\"]").fill(f"enroll_photoOrigin_{internal_group.split(' ')[0].lower()}_{index + 1}")
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("spinbutton").fill(spinbutton_value)
    page.wait_for_timeout(delay)  # Explicit delay
    input_box = page.get_by_placeholder("mm/dd/yyyy HH:mm")
    current_iso = datetime.now().strftime("%Y-%m-%dT%H:%M")
    max_attr = input_box.get_attribute("max")
    fill_value = current_iso if not max_attr or current_iso <= max_attr else max_attr
    input_box.click()
    input_box.press("Control+A")
    input_box.press("Delete")
    input_box.fill(fill_value)
    assert input_box.input_value() == fill_value
    page.wait_for_timeout(delay)  # Explicit delay
    action_dropdown = page.locator("select[name='action']")
    action_dropdown.select_option(action_for_enrollment)
    logger.info(f"Action selected: {action_for_enrollment}")
    page.wait_for_timeout(delay)  # Explicit delay
    try:
        page.get_by_text("SUBMIT REVIEW").click()
    except:
        page.get_by_text("Save").click()
    page.wait_for_timeout(10000)  # Explicit delay

    page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    page.wait_for_timeout(delay)  # Explicit delay


def perform_visitor_image_meta_search_for_photo_origin(page, subject, index, organization, delay):
    logger.info(f"Visitor Image Subject: {subject}")
    page.get_by_text("Visitor Search", exact=True).click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.locator("input[type='file']").set_input_files(subject)
    page.wait_for_timeout(delay)  # Explicit delay
    set_search_date_and_time(page, delay)
    select_organization(page, organization, delay)
    page.get_by_role("combobox").select_option("string:15")
    page.wait_for_timeout(delay)  # Explicit delay
    submit_search(page, delay)
    page.screenshot(path=f"screenshots/_12_vs_image_meta_subject_{index + 1}_uploaded.png")
    page.wait_for_timeout(delay)  # Explicit delay
    # page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
    # page.wait_for_timeout(delay)  # Explicit delay
    # page.locator("xpath=(//div[@class='close-button-large posabs tac'])[1]").click()
    # page.wait_for_timeout(delay)  # Explicit delay


def update_csv(input_csv, output_csv):
    # Read the CSV
    df = pd.read_csv(input_csv, dtype=str)
    # Update only these two columns
    df["Region"] = conftest.ORGANIZATION
    df["timeIncident"] = datetime.now().strftime("%Y-%m-%dT%H:%M")
    # Save updated CSV
    df.to_csv(output_csv, index=False)


def disable_configuration_rights_of_admin_user(page, delay):
    status = []
    logger.info(f"Navigating to Users panel..")
    page.locator("//div[contains(@class,'dashboard-menu-item')][.//p[normalize-space()='Users']]").click()
    page.wait_for_timeout(delay)

    logger.info(f"Searching for {USERS[0]} user")
    search_box = page.locator("//input[@placeholder='Filter by name, username or email']")
    search_box.fill(USERS[0]['username'])
    logger.info(f"Admin user found")
    page.wait_for_timeout(delay)

    logger.info(f"Clicking Details button")
    details_btn = page.locator("//i[@class='fa fa-pencil-square-o icon-medium']")
    details_btn.first.click()
    logger.info(f"Clicked on Details button of Admin user")
    page.wait_for_timeout(delay)

    logger.info(f"Clicking on user role on user details panel")
    page.locator("//span[contains(@ng-click,'viewUserRole') and contains(normalize-space(),'it system admin')]").click()
    logger.info(f"Clicked on user role on user details panel")
    page.wait_for_timeout(delay)

    logger.info(f"Clicking Action dropdown on User Role panel")
    action_dropdown = page.locator(
        "//p[normalize-space()='User Role']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
        "/following-sibling::div[contains(@class,'panel-toolbar')]"
        "//a[contains(@class,'dropdown-toggle')]"
    )
    action_dropdown.wait_for(state="visible")
    action_dropdown.click()
    logger.info(f"Clicked on Action dropdown on User Role panel")
    page.wait_for_timeout(delay)

    logger.info(f"Selecting Edit User Role from Action dropdown")
    edit_user_role = page.locator(
        "//ul[contains(@class,'dropdown-menu')]"
        "//a[normalize-space()='Edit User Role']"
    )
    edit_user_role.wait_for(state="visible", timeout=15000)
    edit_user_role.click()
    logger.info(f"Selected Edit User Role from Action dropdown")
    page.wait_for_timeout(delay)

    logger.info(f"Unchecking the Configuration rights checkbox")
    config_checkbox = page.locator("//span[normalize-space()='Configuration']/ancestor::td//input[@type='checkbox']")
    config_checkbox.wait_for(state="visible")
    if config_checkbox.is_checked():
        config_checkbox.uncheck()
    logger.info(f"Unchecked the Configuration rights checkbox")
    page.wait_for_timeout(delay)

    logger.info(f"Saving User Role details")
    save_btn = page.locator("//a[contains(@ng-click,'saveUserRoleEditClicked')]")
    save_btn.wait_for(state="visible")
    save_btn.click()
    logger.info(f"Saved User Role details")
    page.wait_for_timeout(delay)

    config_row = page.locator("//tr[.//span[normalize-space()='Configuration']]")
    checked_icons = config_row.locator("xpath=.//i[contains(@class,'fa-check') and not(contains(@class,'ng-hide'))]")
    count = checked_icons.count()
    logger.info(f"Number of enabled Configuration rights found: {count}")

    if count == 0:
        status.append(True)
        logger.info("All Configuration rights are disabled")
    else:
        status.append(False)
        logger.error("Some Configuration rights are still enabled")

    logger.info(f"Closing User role panel")
    close_user_role_panel = page.locator(
        "//p[normalize-space()='User Role']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
        "//div[contains(@class,'close-button-large')]"
    )
    close_user_role_panel.wait_for(state="visible")
    close_user_role_panel.click()
    logger.info(f"Closed User role panel")
    page.wait_for_timeout(delay)
    return status

def enable_configuration_rights_of_admin_user(page, delay):
    status = []
    logger.info(f"Login to portal to enable the configuration rights of admin user")
    login(page, username=USERS[0]["username"])
    page.wait_for_timeout(delay)

    logger.info(f"Navigating to Users panel..")
    page.locator("//div[contains(@class,'dashboard-menu-item')][.//p[normalize-space()='Users']]").click()
    logger.info(f"Navigated to Users panel..")
    page.wait_for_timeout(delay)

    logger.info(f"Searching for {USERS[0]['username']} user")
    search_box = page.locator("//input[@placeholder='Filter by name, username or email']")
    search_box.fill(USERS[0]["username"])
    logger.info(f"{USERS[0]['username']} user found")
    page.wait_for_timeout(delay)

    logger.info(f"Click Details button")
    details_btn = page.locator("//i[@class='fa fa-pencil-square-o icon-medium']")
    details_btn.first.click()
    logger.info(f"Clicked details button")
    page.wait_for_timeout(delay)

    logger.info(f"Click on user role on user details panel")
    page.locator("//span[contains(@ng-click,'viewUserRole') and contains(normalize-space(),'it system admin')]").click()
    logger.info(f"Clicked on user role on user details panel")
    page.wait_for_timeout(delay)

    logger.info(f"Click Action dropdown on User Role panel")
    action_dropdown = page.locator(
        "//p[normalize-space()='User Role']"
        "/ancestor::div[contains(@class,'panel-heading-container')]"
        "/following-sibling::div[contains(@class,'panel-toolbar')]"
        "//a[contains(@class,'dropdown-toggle')]"
    )
    action_dropdown.wait_for(state="visible")
    action_dropdown.click()
    logger.info(f"Clicked on Action dropdown on User Role panel")
    page.wait_for_timeout(delay)

    logger.info(f"Selecting Edit User Role from Action dropdown")
    edit_user_role = page.locator(
        "//ul[contains(@class,'dropdown-menu')]"
        "//a[normalize-space()='Edit User Role']"
    )
    edit_user_role.wait_for(state="visible", timeout=15000)
    edit_user_role.click()
    logger.info(f"Selected Edit User Role from Action dropdown")
    page.wait_for_timeout(delay)

    logger.info(f"Check the Configuration rights checkbox")
    configuration_checkboxes = page.locator(
        "//span[normalize-space()='Configuration']"
        "/ancestor::tr"
        "//input[@type='checkbox' and not(@disabled)]"
    )
    for i in range(configuration_checkboxes.count()):
        cb = configuration_checkboxes.nth(i)
        if not cb.is_checked():
            cb.check(force=True)
    logger.info(f"Enabled Configuration rights of {USERS[0]['username']}")
    page.wait_for_timeout(delay)

    save_btn = page.locator("//a[contains(@ng-click,'saveUserRoleEditClicked')]")
    save_btn.wait_for(state="visible")
    save_btn.click()
    logger.info(f"Saved User Role details")
    page.wait_for_timeout(delay)

    config_row = page.locator(
        "//tr[.//span[normalize-space()='Configuration']]"
    )
    enabled_icons = config_row.locator("xpath=.//i[contains(@class,'fa-check') and not(contains(@class,'ng-hide'))]")
    count = enabled_icons.count()
    logger.info(f"Enabled Configuration rights count: {count}")
    if count == 4:
        status.append(True)
        logger.info("All Configuration rights are enabled")
    else:
        status.append(False)
        logger.error("All Configuration rights are NOT enabled")
    return status


def verify_collapse_all_functionality_in_region_hierarchy(page, delay):
    status = []
    try:
        logger.info(f"VERIFYING COLLAPSE ALL FUNCTIONALITY")
        collapse_all = page.locator("//a[normalize-space()='Collapse all']")
        collapse_all.click()
        page.wait_for_timeout(delay)
        visible_lists = page.locator("ol[ui-tree-nodes]:visible")
        count = visible_lists.count()
        if count == 1:
            status.append(True)
            logger.info(f"Collapse all functionality is working as expected")
        else:
            status.append(False)
            logger.info(f"Collapse all functionality is not working as expected")
    except Exception as e:
        logger.error(f"verify_collapse_all_functionality_in_region_hierarchy: {e}")
        save_screenshot(page, "collapse_all_functionality", screenshot_path)
        raise
    return status

def verify_expand_all_functionality_in_region_hierarchy(page, delay):
    status = []
    try:
        logger.info(f"VERIFYING EXPAND ALL FUNCTIONALITY")
        expand_all = page.locator("//a[normalize-space()='Expand all']")
        expand_all.click()
        page.wait_for_timeout(delay)
        collapsed_nodes = page.locator("//ol[@ui-tree-nodes and contains(@class,'hidden')]")
        collapsed_count = collapsed_nodes.count()
        if collapsed_count == 0:
            logger.info("Expand all functionality is working as expected...All nodes are expanded")
            status.append(True)
        else:
            logger.error(f"Expand all failed. Collapsed node count: {collapsed_count}")
            status.append(False)
        # Fetch and print all visible regions
        region_names = page.locator(
            "//span[contains(@class,'textContents') and not(ancestor::ol[contains(@class,'hidden')])]")
        region_count = region_names.count()
        logger.info(f"Total visible regions after expand all: {region_count}")
        all_regions = region_names.all_inner_texts()
        logger.info("Regions visible after Expand all:")
        for region in all_regions:
            logger.info(region.strip())
    except Exception as e:
        logger.error(f"verify_expand_all_functionality_in_region_hierarchy: {e}")
        save_screenshot(page, "expand_all_functionality", screenshot_path)
        raise
    return status

def verify_select_all_functionality_in_region_hierarchy(page, delay):
    status = []
    try:
        logger.info(f"VERIFYING SELECT ALL FUNCTIONALITY")
        select_all = page.locator("//a[normalize-space()='Select all']")
        select_all.click()
        page.wait_for_timeout(delay)
        checked_boxes = page.locator("//i[contains(@class,'fa-check-square-o')]")
        checked_count = checked_boxes.count()
        logger.info(f"Total checkboxes checked: {checked_count}")
        if checked_count > 0:
            logger.info("Select all worked as expected: only one checkbox is selected")
            status.append(True)
        else:
            logger.error(f"Select all failed: expected only 1 selected, but got {checked_count}")
            status.append(False)
        page.wait_for_timeout(delay)
        selected_regions = page.locator(
            "//i[contains(@class,'fa-check-square-o')]/following-sibling::span[@class='textContents']")
        for name in selected_regions.all_inner_texts():
            logger.info(f"Selected region: {name.strip()}")
    except Exception as e:
        logger.error(f"verify_select_all_functionality_in_region_hierarchy: {e}")
        save_screenshot(page, "select_all_functionality", screenshot_path)
        raise
    return status

def verify_unselect_all_functionality_in_region_hierarchy(page, delay):
    status = []
    try:
        logger.info(f"VERIFYING UNSELECT ALL FUNCTIONALITY")
        unselect_all = page.locator("//a[normalize-space()='Unselect all']")
        unselect_all.click()
        page.wait_for_timeout(delay)
        checked_boxes_after_unselect = page.locator("//i[contains(@class,'fa-check-square-o')]")
        checked_count_after_unselect = checked_boxes_after_unselect.count()
        logger.info(f"Total checkboxes checked after Unselect all: {checked_count_after_unselect}")
        if checked_count_after_unselect == 0:
            logger.info("Unselect all worked as expected: no checkboxes are selected")
            status.append(True)
        else:
            logger.error(f"Unselect all failed: expected 0 selected, but got {checked_count_after_unselect}")
            status.append(False)
    except Exception as e:
        logger.error(f"verify_unselect_all_functionality_in_region_hierarchy: {e}")
        save_screenshot(page, "unselect_all_functionality", screenshot_path)
        raise
    return status

def create_enrollment_group_p2(page, eg, delay):
    logger.info(f"Creating enrollment group: {eg['name']}")
    page.locator("a").filter(has_text="Action").click()
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_text("Create Enrollment Group").click()
    page.wait_for_timeout(delay)  # Explicit delay
    fill_enrollment_group_details_1(page, eg, delay)
    page.wait_for_timeout(delay)  # Explicit delay
    # logger.info("Closing enrollment group creation panel")
    # page.wait_for_timeout(delay)  # Explicit delay
    # page.locator(".panel-div > .controller-panel-div > .panel-heading-container > .close-button-large").click()
    # page.wait_for_timeout(delay)  # Explicit delay


def fill_enrollment_group_details_p2(page, eg, delay):
    status = []
    logger.info("Filling in enrollment group details")
    page.get_by_role("textbox", name="Name").fill(eg["name"])
    page.wait_for_timeout(delay)  # Explicit delay
    page.get_by_role("textbox", name="Description").fill(eg["name"] + "_des")
    page.wait_for_timeout(delay)
    alert_color_dropdown = page.locator(
        "xpath=//p[normalize-space()='Masked Face Threshold']"
        "/following::p[normalize-space()='Alert Color']"
        "/following::select[1]"
    )
    alert_color_dropdown.wait_for(state="visible", timeout=5000)
    for color_value in ["#E0301E"]:
        alert_color_dropdown.select_option(color_value)
    page.get_by_text("Save", exact=True).click()
    page.wait_for_timeout(delay)
    success_message = page.locator("//div[@ng-show='messageToUser']")
    success_message.wait_for(state="visible", timeout=5000)  # wait until visible
    message_text = success_message.inner_text().strip()
    if "Success, the group below has been created." in message_text:
        status.append(True)
        logger.info(f"Success message is visible")
    else:
        status.append(False)
        logger.info(f"Success message is NOT visible")
    return status