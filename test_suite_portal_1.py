from utilities import *


def test_login_1_(page, credentials, delay):
    try:
        logger.info("Starting test: test_login_1_")

        logger.info("Logging in with provided credentials")
        log_in(page, credentials["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Taking screenshot after successful login")
        page.screenshot(path=f"screenshots/_1_login_success.png")
    except Exception as e:
        logger.error(f"An error occurred during login: {e}")
        page.screenshot(path=f"screenshots/_1_login_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_login_1_")


def test_core_user_creates_two_users_2_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_core_user_creates_two_users_2_")

        logger.info("Logging in with provided credentials")
        log_in(page, credentials["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to users page")
        page.get_by_text("Users").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing users")
        existing_users = verify_duplicates(page, "xpath=//div[@class='ff-hide scroll-panel']//li/div/div")
        logger.info(f"Existing users: {existing_users}")

        # Create users if they don't already exist
        for user in users[:2]:
            if user["username"] not in existing_users:
                logger.info(f"Creating user: {user['username']}")
                create_user(page, user, credentials, delay)
                page.screenshot(path=f"screenshots/_2_user_creation_success_{user['username']}.png")
                logger.info(f"User created successfully: {user['username']}")
            else:
                logger.info(f"Duplicate user found: {user['username']}")

        logger.info("Closing the users page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during user creation: {e}")
        page.screenshot(path=f"screenshots/_2_user_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_core_user_creates_two_users_2_")


def test_create_store_groups_3_(page, credentials, store_groups, users, delay):
    try:
        logger.info("Starting test: test_create_store_groups_3_")

        first_user = users[0]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to store group page")
        page.locator("#dashboard-menu-container div").filter(has_text="Store Groups").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing store groups")
        existing_store_group = verify_duplicates(page,
                                                 "(//div[@class='list-item-details posrel fltlft disblk w100p'])//div")
        logger.info(f"Existing store groups: {existing_store_group}")

        for store_group in store_groups[:1]:
            if store_group['name'] not in existing_store_group:
                logger.info(f"Creating store group: {store_group['name']}")
                create_store_group(page, store_group, delay, screenshot_path)
                page.screenshot(path=f"screenshots/_3_store_group_creation_success_{store_group['name']}.png")
                logger.info(f"Store group created successfully: {store_group['name']}")
            else:
                logger.info(f"Duplicate store group found: {store_group['name']}")

        logger.info("Closing the store group page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        logger.error(f"An error occurred during store group creation: {e}")
        page.screenshot(path=f"screenshots/_3_store_group_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_create_store_groups_3_")


def test_create_additional_users_4_(page, credentials, store_groups, users, delay):
    try:
        logger.info("Starting test: test_create_additional_users_4_")

        first_user = users[0]
        additional_users = users[2:5]  # Assuming you want to create the next three users in the list
        first_store_group = store_groups[0]

        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to users page")
        page.get_by_text("Users").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing users")
        existing_users = verify_duplicates(page, "xpath=//div[@class='ff-hide scroll-panel']//li/div/div")
        logger.info(f"Existing users: {existing_users}")

        for user in additional_users:
            if user["username"] not in existing_users:
                logger.info(f"Creating additional user: {user['username']}")
                create_additional_user(page, user, credentials, first_store_group, delay)
                page.screenshot(path=f"screenshots/_4_additional_user_creation_success_{user['username']}.png")
                logger.info(f"Additional user created successfully: {user['username']}")
            else:
                logger.info(f"Duplicate user found: {user['username']}")

        logger.info("Closing the users page")
        page.locator(".close-button-large").click()
    except Exception as e:
        logger.error(f"An error occurred during user creation: {e}")
        page.screenshot(path=f"screenshots/_4_additional_user_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_create_additional_users_4_")


def test_create_notification_groups_5_(page, credentials, users, notification_groups, delay):
    try:
        logger.info("Starting test: test_create_notification_groups_5_")

        first_user = users[0]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to notification groups page")
        page.get_by_text("Notification Groups").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing notification groups")
        existing_ngs = verify_duplicates(page, "//div[@class='scroll-panel']//li/div/p[1]")
        logger.info(f"Existing notification groups: {existing_ngs}")

        for ng in notification_groups[:1]:
            if ng['name'] not in existing_ngs:
                logger.info(f"Creating notification group: {ng['name']}")
                create_notification_group(page, ng, delay)
                # timestamp = time.strftime("%Y%m%d-%H%M%S")
                page.screenshot(path=f"screenshots/_5_notification_group_creation_success_{ng['name']}.png")
                logger.info(f"Notification group created successfully: {ng['name']}")
            else:
                logger.info(f"Duplicate notification group found: {ng['name']}")

        logger.info("Closing the notification groups page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during notification group creation: {e}")
        page.screenshot(path=f"screenshots/_5_notification_group_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_create_notification_groups_5_")


def test_create_enrollment_groups_6_(page, credentials, users, enrollment_groups, delay):
    try:
        logger.info("Starting test: test_create_enrollment_groups_6_")

        first_user = users[0]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to enrollment groups page")
        page.get_by_text("Enrollment Groups").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing enrollment groups")
        existing_egs = verify_duplicates(page, "//div[@class='scroll-panel']//li/div/p[1]")
        logger.info(f"Existing enrollment groups: {existing_egs}")

        for eg in enrollment_groups[:5]:
            if eg['name'] not in existing_egs:
                logger.info(f"Creating enrollment group: {eg['name']}")
                create_enrollment_group(page, eg, delay)
                page.screenshot(path=f"screenshots/_6_enrollment_group_creation_success_{eg['name']}.png")
                logger.info(f"Enrollment group created successfully: {eg['name']}")
            else:
                logger.info(f"Duplicate enrollment group found: {eg['name']}")

        logger.info("Closing the enrollment groups page")
        page.locator("#panel-container").click()
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during enrollment group creation: {e}")
        page.screenshot(path=f"screenshots/_6_enrollment_group_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_create_enrollment_groups_6_")


def test_create_tags_7_(page, credentials, users, tags, delay):
    try:
        logger.info("Starting test: test_create_tags_7_")

        first_user = users[0]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        # agree_to_term(page, delay)

        logger.info("Navigating to tags page")
        page.get_by_text("Tags").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Fetching the list of existing tags")
        existing_tags = verify_duplicates(page, "//div[@class='scroll-panel']//li/p[1]")
        logger.info(f"Existing tags: {existing_tags}")

        for tag in tags:
            if tag['name'] not in existing_tags:
                logger.info(f"Creating tag: {tag['name']}")
                create_tag(page, tag, delay)
                page.screenshot(path=f"screenshots/_7_tag_creation_success_{tag['name']}.png")
                logger.info(f"Tag created successfully: {tag['name']}")
            else:
                logger.info(f"Duplicate tag found: {tag['name']}")

        logger.info("Closing the tags page")
        page.locator("#tags_1 div").filter(has_text="Tags Probable Match Event Tags").locator("div").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during tag creation: {e}")
        page.screenshot(path=f"screenshots/_7_tag_creation_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_create_tags_7_")


def test_enroll_subjects_8_(page, credentials, users, image_files, num_subjects, organization, delay):
    try:
        logger.info("Starting test: test_enroll_subjects_8_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        subjects = image_files[:num_subjects]  # Get the list of image files from the directory
        logger.info(f"Subjects to enroll: {subjects}")

        groups = [
            ("abe (Serious Offender - Medium)", "300"),
            ("fraude (Serious Offender - None)", "50"),
            ("pte (Serious Offender - Low)", "150"),
            ("soe (Serious Offender - High)", "500"),
            ("vipe (Serious Offender - None)", "0")
        ]

        group_size = num_subjects // len(groups)
        page.wait_for_timeout(delay)  # Explicit delay

        for i, subject in enumerate(subjects):
            group_index = i // group_size
            if group_index >= len(groups):
                group_index = len(groups) - 1

            # print(subject)
            # print(os.path.splitext(os.path.basename(subject))[0])

            enroll_subject(page, subject, groups[group_index], organization, i, delay)

    except Exception as e:
        logger.error(f"An error occurred during identity & enroll: {e}")
        page.screenshot(path=f"screenshots/_8_enroll_subjects_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_enroll_subjects_8_")


def test_approve_subjects_9_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_approve_subjects_9_")

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
        page.screenshot(path=f"screenshots/_9_approve_enroll_subjects_success.png")
    except Exception as e:
        logger.error(f"An error occurred during approve enrollment: {e}")
        page.screenshot(path=f"screenshots/_9_approve_enroll_subjects_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_approve_subjects_9_")
