## Before Configuring core and edges, make sure to update the respective parameters in conftest.py-

#### STEP 1:
##### REGISTER_URL = "https://localhost:5000/register"
##### REGISTER_LOGIN_URL = "https://localhost:5000/login"
##### BASE_URL = "https://scecore2-vm.qa.facefirst.dev/"
##### WEBAPI_VERSION = "8.3.0.66"
##### SERVER_VERSION = "8.3.0.24"
##### EMAIL = "ritesh.kagale777@facefirst.com"
##### RTSPPort = "8551/v2"
##### CORE_NAME = "scecore2"
##### ORGANIZATION = "sceedge2-vm"

#### STEP 2: Execute the below commands-
pytest -v -s .\test_suite_core_0.py --html="Results/test_suite_core_0.html"

#### STEP 3: Once the core is configured, make sure to download the client installer on edge and then execute the below command to configure edge-
pytest -v -s .\test_suite_edge_0.py --html="Results/test_suite_edge_0.html"

#### STEP 4: Once core and edges are configured, execute below commands to populate data on the environment-
##### 1. To create Users, Store Groups, Enrollment Groups, Notification Group, Enroll subjects, Approve subjects:
   pytest -v -s .\test_suite_portal_1.py --html="\test_suite_portal_1.html"

##### 2. Next, run the video stream on edge environment, then execute the below command to Tag Events, perform Visitor Search, verify Insights Dashboard, Audit Log Reports:
   pytest -v -s .\test_suite_portal_2.py --html="\test_suite_portal_2.html"

#### STEP 5: To verify DM test cases, execute below command-
 pytest -v -s .\test_suite_other_dm_3.py --html="\test_suite_other_dm_3.html"

#### Once basic smoke test execution is completed, execute below p1 automation scripts-
pytest -v -s .\P1_Module_wise\Test_P1_Set_1.py --html="Results/Test_P1_Set_1_5Dec.html"


## Modules:

### Portal Login:
Requirements:
1. URL
2. Username
3. Password



#############  Reporting Module ########################
Make sure to change reporting start date and end date in confest.py under Reporting section
reporting_start_date = date(2026, 1, 2)
reporting_end_date = date(2026, 1, 2)

Make sure to change group fixture according to your groups 
@pytest.fixture
def groups():
    return ["soe", "abe", "pte", "fraude", "vipe"]

Make sure to change Zone_list  fixture according to your edges 
@pytest.fixture
def zones_list():
    return ["All Devices", "scecore2-vm", "sceedge2-vm"]

Make sure to change single_Zone fixture according to your edge
@pytest.fixture
def single_zone():
    return ["sceedge2-vm"]

################ Notifier changes #####################
Make sure to change notifier groups according to your groups under Notifier section in confest.py
Notifier_groups = ["soe", "abe", "pte", "fraude", "vipe"]

Make sure to change root_region fixture according to your root region
@pytest.fixture
def root_region():
    return ["scecore2-vm"]

############ Audit_Log_reports #################
Please verify "DefaultEnrollmentGroup (Serious Offender - None)" is exists or not. If Not please create.using default enrollment group to enroll subjects for audit_Log reports.


