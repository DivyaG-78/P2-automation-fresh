from utilities import *


def test_add_tags_to_events_10_(page, credentials, users, enrollment_groups, delay):
    try:
        logger.info("Starting test: test_add_tags_to_events_10_")

        first_user = users[3]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Probable Match Events page")
        page.get_by_text("Probable Match Events", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay

        for i, eg in enumerate(enrollment_groups[:5]):
            logger.info(f"Searching for enrollment group: {eg['name']}")
            search_enrollment_group(page, eg, delay)
            logger.info(f"Adding tags to events for enrollment group: {eg['name']}")
            add_tags_to_events(page, eg, delay)
            page.screenshot(path=f"screenshots/_10_add_tag_to_events_success_{eg['name']}.png")
            logger.info(f"Tags added successfully to events for enrollment group: {eg['name']}")

        logger.info("Closing the Probable Match Events page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during add tag to events: {e}")
        page.screenshot(path=f"screenshots/_10_add_tag_to_events_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_add_tags_to_events_10_")


def test_visitor_image_search_11_(page, credentials, users, image_files_2, delay):
    try:
        logger.info("Starting test: test_visitor_image_search_11_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        for i, subject in enumerate(image_files_2):
            perform_visitor_image_search(page, subject, i, delay)

    except Exception as e:
        logger.error(f"An error occurred during visitor image search: {e}")
        page.screenshot(path=f"screenshots/_11_visitor_image_search_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_visitor_image_search_11_")


def test_visitor_image_meta_search_12_(page, credentials, users, image_files_2, organization, delay):
    try:
        logger.info("Starting test: test_visitor_image_meta_search_12_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        for i, subject in enumerate(image_files_2):
            perform_visitor_image_meta_search(page, subject, i, organization, delay)

    except Exception as e:
        logger.error(f"An error occurred during visitor image meta search: {e}")
        page.screenshot(path=f"screenshots/_12_visitor_image_meta_search_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_visitor_image_meta_search_12_")


def test_visitor_meta_search_13_(page, credentials, users, image_files_2, organization, delay):
    try:
        logger.info("Starting test: test_visitor_meta_search_13_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Visitor Search")
        page.get_by_text("Visitor Search", exact=True).click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Setting search date and time")
        set_search_date_and_time(page, delay)

        logger.info(f"Selecting organization: {organization}")
        select_organization(page, organization, delay)

        logger.info("Submitting search")
        submit_search(page, delay)

        logger.info("Taking screenshot after subject upload")
        page.screenshot(path=f"screenshots/_13_visitor_meta_subject_uploaded.png")

        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//div[@class='close-button-large posabs tac'])[2]").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page.locator("xpath=(//div[@class='close-button-large posabs tac'])[1]").click()
        page.wait_for_timeout(delay)  # Explicit delay
    except Exception as e:
        logger.error(f"An error occurred during visitor meta search: {e}")
        page.screenshot(path=f"screenshots/_13_visitor_meta_search_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_visitor_meta_search_13_")


def test_enroll_approve_mask_add_face_note_to_subject_14_(page, credentials, users, organization, delay):
    try:
        logger.info("Starting test: test_enroll_approve_mask_add_face_note_to_subject_14_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        groups = [
            ("soe (Serious Offender - High)", "500")
        ]

        logger.info("Enrolling mask subject")
        enroll_mask_subject(page, conftest.MASK, groups[0], organization, delay)
        logger.info("Mask subject enrolled successfully")
    except Exception as e:
        logger.error(f"An error occurred during mask enrollment: {e}")
        page.screenshot(path=f"screenshots/_14_enroll_mask_subjects_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)

    try:
        logger.info("Logging in with user: {users[4]['username']}")
        first_user = users[4]
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
    except Exception as e:
        logger.error(f"An error occurred during approve mask enrollment: {e}")
        page.screenshot(path=f"screenshots/_14_approve_enroll_mask_subjects_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)

    try:
        logger.info("Logging in with user: {users[1]['username']}")
        first_user = users[1]
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Adding face and note to subject")
        add_face_and_note_to_subject(page, delay)
        logger.info("Face and note added successfully to subject")
    except Exception as e:
        logger.error(f"An error occurred during executive add face subjects: {e}")
        page.screenshot(path=f"screenshots/_14_executive_add_face_note_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_enroll_approve_mask_add_face_note_to_subject_14_")


def test_detect_image_15_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_detect_image_15_")

        first_user = users[2]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Detecting face")
        detect_face(page, conftest.DETECT, delay)
        logger.info("Face detection successful")
    except Exception as e:
        logger.error(f"An error occurred during face detection: {e}")
        page.screenshot(path=f"screenshots/_15_detect_face_subject_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_detect_image_15_")


def test_notifier_16_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_notifier_16_")

        first_user = users[1]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Configuring notifier")
        configure_notifier(page, delay)
        logger.info("Notifier configured successfully")
    except Exception as e:
        logger.error(f"An error occurred during notifier configuration: {e}")
        page.screenshot(path=f"screenshots/_16_notifier_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_notifier_16_")


def test_reporting_17_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_reporting_17_")

        first_user = users[1]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Reporting page")
        page.get_by_text("Reporting").click()
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Generating report")
        generate_report(page, delay)

        logger.info("Closing the Reporting page")
        page.locator(".close-button-large").click()
        page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        logger.error(f"An error occurred during reporting: {e}")
        page.screenshot(path=f"screenshots/_17_reporting_error.png")
        page.wait_for_timeout(delay)  # Explicit delay
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_reporting_17_")


def test_audit_log_report_18_(page, credentials, users, delay):
    try:
        logger.info("Starting test: test_audit_log_report_18_")
        logger.info("Starting enrollment group audit log report")

        first_user = users[0]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Updating enrollment group")
        update_enrollment_group(page, delay)
        logger.info("Enrollment group updated successfully")
    except Exception as e:
        logger.error(f"An error occurred during enrollment group audit log report: {e}")
        page.screenshot(path=f"screenshots/_18_enrollment_group_audit_log_report_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)

    try:
        logger.info("Starting audit log report generation")

        first_user = users[1]
        logger.info(f"Logging in with user: {first_user['username']}")
        log_in(page, first_user["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Audit Log Reports page")
        with page.expect_popup() as page1_info:
            page.get_by_text("Audit Log Reports").click()
        page1 = page1_info.value
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: Approver Enrollments")
        page1.locator("div").filter(has_text=re.compile(r"^Report type:Select$")).locator("#drop-down-button").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="Approver Enrollments").click()
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting date range: Last 7 days")
        page1.get_by_role("button", name="Custom Date Range").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="Last 7 days").click()
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting all users")
        page1.get_by_role("button", name="Select").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_text("All Users").click()
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Submitting report")
        page1.locator("div").filter(has_text=(re.compile(r"^SUBMIT REPORT$"))).click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("button", name="SUBMIT REPORT").click()
        page1.wait_for_timeout(delay)  # Explicit delay

        page1.screenshot(path=f"screenshots/_18_audit_log_approve_enrollments_report.png")

        logger.info("Downloading report: Approver Enrollments")
        with page1.expect_download() as download1_info:
            page1.locator("div > .MuiSvgIcon-root").click()
        download1 = download1_info.value
        download1.save_as(f'screenshots/alr_downloads/{download1.suggested_filename}')
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: User Enrollments")
        page1.get_by_role("button", name="Approver Enrollments").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="User Enrollments").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.screenshot(path=f"screenshots/_18_audit_log_user_enrollments_report.png")
        page1.wait_for_timeout(delay)  # Explicit delay
        with page1.expect_download() as download2_info:
            page1.locator("div > .MuiSvgIcon-root").click()
        download2 = download2_info.value
        download2.save_as(f'screenshots/alr_downloads/{download2.suggested_filename}')
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: Log-in / Log-out")
        page1.get_by_role("button", name="User Enrollments").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="Log-in / Log-out").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.screenshot(path=f"screenshots/_18_audit_log_log_in_log_out_report.png")
        page1.wait_for_timeout(delay)  # Explicit delay
        with page1.expect_download() as download3_info:
            page1.locator("div > .MuiSvgIcon-root").click()
        download3 = download3_info.value
        download3.save_as(f'screenshots/alr_downloads/{download3.suggested_filename}')
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: Threshold Changes")
        page1.get_by_role("button", name="Log-in / Log-out").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="Threshold Changes").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.screenshot(path=f"screenshots/_18_audit_log_threshold_change_report.png")
        page1.wait_for_timeout(delay)  # Explicit delay
        with page1.expect_download() as download4_info:
            page1.locator("div > .MuiSvgIcon-root").click()
        download4 = download4_info.value
        download4.save_as(f'screenshots/alr_downloads/{download4.suggested_filename}')
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: System Users Log")
        page1.get_by_role("button", name="Threshold Changes").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="System Users Log").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.screenshot(path=f"screenshots/_18_audit_log_system_users_log_report.png")
        page1.wait_for_timeout(delay)  # Explicit delay
        with page1.expect_download() as download5_info:
            page1.locator("div > .MuiSvgIcon-root").click()
        download5 = download5_info.value
        download5.save_as(f'screenshots/alr_downloads/{download5.suggested_filename}')
        page.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting report type: Aged Enrollments w/No Events")
        page1.get_by_role("button", name="System Users Log").click()
        page.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="Aged Enrollments w/No Events").click()
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Selecting date range: > Or = 3 months")
        page1.get_by_role("button", name="> Or =").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("menuitem", name="3 months", exact=True).click()
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Submitting report")
        page1.locator("div").filter(has_text=(re.compile(r"^SUBMIT REPORT$"))).click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.get_by_role("button", name="SUBMIT REPORT").click()
        page1.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path=f"screenshots/_18_audit_log_aged_enrollment_w_No_events_report.png")
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Downloading report: Aged Enrollments w/No Events")
        with page1.expect_download() as download6_info:
            page1.locator(
                "xpath=/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[3]/div[1]/*[name()='svg'][1]").click()
        download6 = download6_info.value
        download6.save_as(f'screenshots/alr_downloads/{download6.suggested_filename}')
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.wait_for_timeout(delay)  # Explicit delay

        try:
            logger.info("Closing the Audit Log Reports page")
            page1.close()
            page.wait_for_timeout(delay)  # Explicit delay
            page.wait_for_timeout(delay)  # Explicit delay
        except Exception as e:
            logger.error(f"An error occurred during audit log report: {e}")
            page.wait_for_timeout(delay)  # Explicit delay
            page.wait_for_timeout(delay)  # Explicit delay
            page.screenshot(path=f"screenshots/_18_audit_log_report_closing_error.png")
            page.wait_for_timeout(delay)  # Explicit delay

    except Exception as e:
        logger.error(f"An error occurred during audit log report: {e}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path="screenshots/_18_audit_log_report_error.png")
        page.wait_for_timeout(delay)  # Explicit delay
        raise
    finally:
        log_out(page, delay)
        logger.info("Test completed: test_audit_log_report_18_")


def test_insight_dashboard_overview_19_(page, credentials, delay):
    try:
        logger.info("Starting test: test_insight_dashboard_overview_19_")

        logger.info("Logging in with provided credentials")
        log_in(page, credentials["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Insights Dashboard")
        with page.expect_popup() as page1_info:
            page.get_by_text("Insights Dashboard").click()
        page1 = page1_info.value
        page1.wait_for_timeout(delay)  # Explicit delay
        page1.wait_for_timeout(delay)
        page1.wait_for_timeout(delay)
        logger.info("Verifying dashboard metrics")
        verify_dashboard_metrics(page1, delay)
        page1.wait_for_timeout(delay)
        page1.wait_for_timeout(delay)

        logger.info("Closing the Insights Dashboard page")
        try:
            page1.wait_for_timeout(delay)
            page1.wait_for_timeout(delay)
            page1.close()
        except Exception as e:
            logger.error(f"An error occurred during Insight dashboard overview report: {e}")
            page1.screenshot(path=f"screenshots/_19_insight_dashboard_closing_error.png")
            page1.wait_for_timeout(delay)
            page1.wait_for_timeout(delay)

    except Exception as e:
        logger.error(f"An error occurred during insight dashboard overview: {e}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)  # Explicit delay
        page.wait_for_timeout(delay)
        page.screenshot(path=f"screenshots/_19_insight_dashboard_overview_error.png")
        page.wait_for_timeout(delay)  # Explicit delay
        raise
    finally:
        logger.info("Logging out")
        page.wait_for_timeout(delay)
        page.wait_for_timeout(delay)
        log_out(page, delay)
        logger.info("Test completed: test_insight_dashboard_overview_19_")


def test_insight_dashboard_events_20_(page, credentials, delay):
    try:
        logger.info("Starting test: test_insight_dashboard_events_20_")

        logger.info("Logging in with provided credentials")
        log_in(page, credentials["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Insights Dashboard")
        with page.expect_popup() as page1_info:
            page.get_by_text("Insights Dashboard").click()
        page1 = page1_info.value
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Verifying event dashboard matrices")
        verify_event_dashboard_matrices(page1, delay)

    except Exception as e:
        logger.error(f"An error occurred during insight dashboard events: {e}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path=f"screenshots/_20_insight_dashboard_events_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_insight_dashboard_events_20_")


def test_insight_dashboard_enrollment_21_(page, credentials, delay):
    try:
        logger.info("Starting test: test_insight_dashboard_enrollment_21_")

        logger.info("Logging in with provided credentials")
        log_in(page, credentials["username"], credentials["password"], delay)
        agree_to_term(page, delay)

        logger.info("Navigating to Insights Dashboard")
        with page.expect_popup() as page1_info:
            page.get_by_text("Insights Dashboard").click()
        page1 = page1_info.value
        page1.wait_for_timeout(delay)  # Explicit delay

        logger.info("Verifying enrollment dashboard metrics")
        verify_enrollment_dashboard_metrics(page1, delay)
    except Exception as e:
        logger.error(f"An error occurred during insight dashboard enrollment: {e}")
        page.wait_for_timeout(delay)  # Explicit delay
        page.screenshot(path=f"screenshots/_21_insight_dashboard_enrollment_error.png")
        raise
    finally:
        logger.info("Logging out")
        log_out(page, delay)
        logger.info("Test completed: test_insight_dashboard_enrollment_21_")
        