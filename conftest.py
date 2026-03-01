import os
from pathlib import Path

import pytest
import logging
from datetime import datetime, timedelta
from datetime import date
from playwright.sync_api import sync_playwright
from natsort import natsorted

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define global variables
REGISTER_URL = "https://localhost:5000/register"
REGISTER_LOGIN_URL = "https://localhost:5000/login"
BASE_URL = "https://ftecore1a-vm.qa.facefirst.dev/"
WEBAPI_VERSION = "8.4.0.19"
SERVER_VERSION = "8.4.0.6"
EMAIL = "ritesh.kagale777@facefirst.com"
DOMAIN_Status = 1  # 1 letsencrypt, 2 ip, 3 go daddy
LICENSE = "ad078857-1f20-477a-83fa-0434311f057e"
LICENSE_URL = "https://license.facefirst.dev/"
TIMEZONE = "(UTC+05:30) Chennai, Kolkata"
JSONUrl = "https://localhost/swagger/index.html"
JSONFile = "datas/jsonFiles/Kroger_International.json"
SELECTRegion = "Kroger San Fransisco - KSF"
RTSPPort = "8551/v2"
GEOLocation = "Bengaluru"
USERNAME = "core"
PASSWORD = "Right_1r1s"
INVALID_PASSWORD = "Right_1"
INVALID_USERNAME = "USER"
BLOCKED_USER = "approve"
USERNAME1 = "admin"
SEARCH_TEXT = "ASSAULT"
USERROLE = "5. it system admin"
SUBJECTS_PATH = "datas/original_video1"  # Update this path to the actual path of your enroll subject images
SUBJECTS_PATH_ROC = "datas/rocEnrollments"  # for ROC algo
SUBJECTS_PATH_2 = "datas/visitorSearches"  # Update this path to the actual path of your visitor subject images
SUBJECTS_PATH_3 = "datas/vsEnrollments"  # Update this path to the actual path of your visitor subject images for enrollment
SUBJECTS_PATH_4 = "datas/expirationEnrollments"  # Update this path to the actual path of your expiration subject images for enrollment
enrolled_img = "datas/original_video1"
NUM_SUBJECTS = 25
NUM_SUBJECTS_ROC = 10
CORE_NAME = "ftecore1"
ORGANIZATION = "fteedge1-vm"
organization1 = "fteedge1-vm"
OFFLINE_EDGE = "fteedge1-vm"
ONLINE_EDGE = "fteedge1-vm"
region_name = CORE_NAME + "-vm - KCORP"
# region_name = "Kroger International - KCORP"
DELAY = 3000
search_date = datetime(2026, 1, 23)
search_time = datetime.strptime("05:50 PM", "%I:%M %p")
MASK = "datas/maskImages/MASK1.jpg"
FACE = "datas/maskImages/FACE.png"
NOTE = "datas/noteImages/NOTE.png"
DETECT = "datas/detectImages/DETECTIMAGE.PNG"
EDITED_NAME = CORE_NAME.capitalize()
EDITED_EDGE_NAME = ORGANIZATION.capitalize()
TIMEOUT_LONG = 300000  # 5 minutes
delay_1_second = 3000
delay_2_second = 3000
delay_3_second = 3000
delay_4_second = 4000
delay_5_second = 5000
delay_10_Second = 10000
disabled_images_path = "datas/disabledEnrollments"

# Photo Origin
photo_origin_enrollments = "datas/photoOriginImages"
Num_Subjects = 5

######## Reporting ##############


reporting_end_date = date.today()
reporting_start_date = reporting_end_date - timedelta(days=2)


start_date = "05/12/2025"
end_date = "05/12/2025"

####### Notifier #########
Notifier_groups = ["soe", "abe", "pte", "fraude", "vipe"]

####### ALR ###########
threshold_group = "abe"

###### Audit_Log_report ############
report_options = ['Aged Enrollments w/No Events','Approver Enrollments','User Enrollments','Log-in / Log-out','Threshold Changes','System Users Log']
expected_date_options = [
    "Custom Date Range",
    "Last 7 days",
    "Last 14 days",
    "Last 30 days",
    "Month-to-date",
    "Last 90 days",
    "Quarter-to-date",
    "Year-to-date"
]
deleted_username = "audit_user8"
expected_name = "audit, audit"
USERS = [
    {
        "username": "admin",
        "role_id": "5. it system admin",
        "timezone": "Asia/Kolkata",
        "region": CORE_NAME+"-vm - KCORP"
        # "region": "Kroger International - KCORP"
    },
    {
        "username": "executive",
        "role_id": "1. executive",
        "timezone": "Asia/Kolkata",
        "region": CORE_NAME+"-vm - KCORP"
        # "region": "Kroger International - KCORP"
    },
    {
        "username": "operator",
        "role_id": "3. operator",
        "timezone": "Asia/Kolkata",
        "region": "Kroger San Fransisco - KSF"
    },
    {
        "username": "responder",
        "role_id": "4. responder",
        "timezone": "Asia/Kolkata",
        "region": "Kroger San Fransisco - KSF"
    },
    {
        "username": "approver",
        "role_id": "2. approver/supervisor",
        "timezone": "Asia/Kolkata",
        "region": "Kroger US West - USWEST"
    },
    {
        "username": "p1user1",
        "role_id": "5. it system admin",
        "timezone": "Asia/Kolkata",
        "region": CORE_NAME+"-vm - KCORP"
        # "region": "Kroger International - KCORP"
    },
    {
        "username": "p1user2",
        "role_id": "5. it system admin",
        "timezone": "Asia/Kolkata",
        "region": CORE_NAME+"-vm - KCORP",
        # "region": "Kroger International - KCORP",
        "store_group": "sg1"
    }
]
USERCREATION = [{"created_username": "AUPUSER99"}]

USERS_WITH_ALL_DETAILS = [
    {
        "username": "p1User11",
        "userRole": "5. it system admin",
        "company": "TestCompany",
        "title": "Manager",
        "department": "IT",
        "region_index": 1,
        "alertphone": "1234567890",
        "address1": "123 Main St",
        "address2": "Apt 101",
        "city": "Bangalore",
        "state": "Karnataka",
        "postalcode": "560034",
        "homephone": "9876543210",
        "workphone": "9876543211",
        "faxphone": "9876543212",
        "phonetype": "iPhone",
        "phoneprovider": "Verizon",
        "timezone": "Asia/Kolkata"
    },
    {
        "username": "p1User12",
        "userRole": "5. it system admin",
        "company": "TestCompany",
        "title": "Manager",
        "department": "IT",
        "region_index": 1,
        "alertphone": "1234567890",
        "address1": "123 Main St",
        "address2": "Apt 101",
        "city": "Bangalore",
        "state": "Karnataka",
        "postalcode": "560034",
        "homephone": "9876543210",
        "workphone": "9876543211",
        "faxphone": "9876543212",
        "phonetype": "iPhone",
        "phoneprovider": "Verizon",
        "timezone": "Asia/Kolkata"
    }
]


STORE_GROUPS = [
    {
        "name": "sg01",
        "org": ORGANIZATION
    },
    {
        "name": "sgP1",
        "org": ORGANIZATION
    }
    # Add more store groups as needed
]

NOTIFICATION_GROUPS = [
    {
        "name": "ng01",
        "user_ng": "responder responderF"
    },
    {
        "name": "ngP1"
    }
    # Add more notification groups as needed
]

ENROLLMENT_GROUPS = [
    {
        "name": "abe",
        "color": "#EB8C00",
        "priority": "Medium",
        "eg_ng": "ng01 ng01_des Linked Unlinked 1"
    },
    {
        "name": "fraude",
        "color": "#00AEF0",
        "priority": "None",
        "eg_ng": "ng01 ng01_des Linked Unlinked 1"
    },
    {
        "name": "pte",
        "color": "#FFFC00",
        "priority": "Low",
        "eg_ng": "ng01 ng01_des Linked Unlinked 1"
    },
    {
        "name": "soe",
        "color": "#E0301E",
        "priority": "High",
        "eg_ng": "ng01 ng01_des Linked Unlinked 1"
    },
    {
        "name": "vipe",
        "color": "#FFFFFF",
        "priority": "None",
        "eg_ng": "ng01 ng01_des Linked Unlinked 1"
    },
    {
        "name": "egP1",
        "color": "#E0301E",
        "priority": "High"
    },
    {
        "name": "egP2Enrollments",
        "color": "#E0301E",
        "priority": "High"
    },
    {
        "name": "egP2NotificationGroup",
        "color": "#E0301E",
        "priority": "High"
    },
    {
        "name": "egP2pme",
        "color": "#E0301E",
        "priority": "High"
    },
    {
        "name": "egP2alertcolor",
        "color": "#E0301E",
        "priority": "High"
    }
]

TAGS = [
    {
        "name": "ASSAULT",
        "serious_event": True
    },
    {
        "name": "THREAT",
        "serious_event": True
    },
    {
        "name": "PUSH CART",
        "serious_event": True
    },
    {
        "name": "FRAUD",
        "serious_event": False
    }
    # Add more tags as needed
]

USER_LINKED_TO_EDGE = [
    {
        "username": "p1user1linkedtoedge1",
        "role_id": "5. it system admin",
        "timezone": "Asia/Kolkata",
        "region": ORGANIZATION
    }
]


# ----------------- HTML Report Path -----------------
def pytest_configure(config):
    if not config.option.htmlpath:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        config.option.htmlpath = f"{Path(__file__).parent}\\Reports\\report_{now}.html"


def get_image_files(directory):
    return natsorted([os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.png', '.jpg', '.jpeg'))])


def get_image_files_vs(directory):
    return natsorted([os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.png', '.jpg', '.jpeg'))])


def get_image_files_vsEnrollment(directory):
    return natsorted([os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(('.png', '.jpg', '.jpeg'))])


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright):
    logger.info("Launching browser")
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    yield browser
    logger.info("Closing browser")
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    logger.info("Creating new browser context")
    context = browser.new_context(no_viewport=True, ignore_https_errors=True)
    yield context
    logger.info("Closing browser context")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    logger.info("Creating new page")
    page = context.new_page()
    yield page
    logger.info("Closing page")
    page.close()


@pytest.fixture(scope="session")
def credentials():
    return {"username": USERNAME, "password": PASSWORD, "email": EMAIL}


@pytest.fixture(scope="session")
def users():
    return USERS


@pytest.fixture(scope="session")
def store_groups():
    return STORE_GROUPS


@pytest.fixture(scope="session")
def notification_groups():
    return NOTIFICATION_GROUPS


@pytest.fixture(scope="session")
def enrollment_groups():
    return ENROLLMENT_GROUPS


@pytest.fixture(scope="session")
def tags():
    return TAGS


@pytest.fixture(scope="session")
def subjects_path():
    return SUBJECTS_PATH


@pytest.fixture(scope="session")
def get_enrolled_img():
    return enrolled_img


@pytest.fixture(scope="session")
def get_enrolled_img_files(get_enrolled_img):
    return get_image_files(get_enrolled_img)


@pytest.fixture(scope="session")
def num_subjects():
    return NUM_SUBJECTS


@pytest.fixture(scope="session")
def organization():
    return ORGANIZATION


@pytest.fixture(scope="session")
def delay():
    return DELAY


@pytest.fixture(scope="session")
def image_files(subjects_path):
    return get_image_files(subjects_path)


@pytest.fixture(scope="session")
def subjects_path_2():
    return SUBJECTS_PATH_2


@pytest.fixture(scope="session")
def image_files_2(subjects_path_2):
    return get_image_files_vs(subjects_path_2)


@pytest.fixture(scope="session")
def subjects_path_3():
    return SUBJECTS_PATH_3


@pytest.fixture(scope="session")
def image_files_3(subjects_path_3):
    return get_image_files_vsEnrollment(subjects_path_3)


@pytest.fixture(scope="session")
def subjects_path_4():
    return SUBJECTS_PATH_4


@pytest.fixture(scope="session")
def image_files_4(subjects_path_4):
    return get_image_files_vsEnrollment(subjects_path_4)


#******** Reporting Fixtures************
# @pytest.fixture
# def start_date():
#     return {
#         "month_year": "December 2025",
#         "day": "11"
#     }
#
# @pytest.fixture
# def end_date():
#     return {
#         "month_year": "December 2025",
#         "day": "11"
#     }


@pytest.fixture
def groups():
    return ["soe", "abe", "pte", "fraude", "vipe"]

# @pytest.fixture
# def start_dt_str():
#     return "12/05/2025 12:00 AM"
#
# @pytest.fixture
# def end_dt_str():
#     return "12/05/2025 11:59 PM"


@pytest.fixture
def zones_list():
    return ["All Devices", CORE_NAME, ORGANIZATION] # add more zones as needed


@pytest.fixture
def single_zone():
    return [ORGANIZATION]


# Notifier ##################
@pytest.fixture
def root_region():
    return [CORE_NAME]


# screenshot path for storing all screenshots for failed tests
@pytest.fixture(scope="session")
def screenshot_path():
    return f"{Path(__file__).parent}\\Screenshots"


# roc

@pytest.fixture(scope="session")
def subjects_path_roc():
    return SUBJECTS_PATH_ROC


@pytest.fixture(scope="session")
def image_files_roc(subjects_path_roc):
    return get_image_files(subjects_path_roc)


@pytest.fixture(scope="session")
def num_subjects_roc():
    return NUM_SUBJECTS_ROC


@pytest.fixture(scope="session")
def disabled_images_path():
    base_dir = os.getcwd()
    path = os.path.join(base_dir, "datas", "disabledEnrollments")

    return [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
