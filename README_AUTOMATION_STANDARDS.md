# Automation Standards – Tests, POM, Fixtures, and Utilities

---

## 1) Test Case Standard (Current Style – Mandatory)

**Pattern**:

- Tests use `if/else + assert True/False`
- Each test calls **exactly one** POM/validation method
- **No** loggers, **no** try/except, **no** extra logic in tests
- Test name must match the **test case ID**

### ✅ Canonical Example (Use As-Is)
``` python
def test_tc_df_03(page, credentials, screenshot_path, delay):
    if click_on_close_panel_button_and_verify_detect_faces_panel_is_closing(
        page, credentials, screenshot_path, delay
    ):
        assert True
    else:
        assert False
```

### ✅ Reviewer Checklist (Tests)
- [ ] Uses `if/else` with `assert True/False`
- [ ] Calls exactly one POM method
- [ ] No logging or try/except
- [ ] No extra logic (loops/conditions beyond the if/else)
- [ ] Test name maps to the test case ID

---

## 2) POM Standard (Mandatory)

**Contract:**

- **Return** only `True` or `False` (no asserts inside POM)
- Use `status = []` and **append boolean validations** (`status.append(True/False)`)
- **Final decision:** `if False in status: return False else: return True`
- Always use **`try / except / finally`**
- On **failure/exception:** capture screenshot as `<test_id>_failed.png`
- Perform **cleanup** (e.g., logout) in `finally`
- After **every locator acquisition or action**, call **`page.wait_for_timeout(3000)`**  
  (You may pass `delay` fixture but the default enforced wait is 3000ms)

### ✅ Canonical Example (Use As-Is)
```python
def click_on_close_panel_button_and_verify_detect_faces_panel_is_closing(page, credentials, screenshot_path, delay):
    test_id = "test_tc_df_03"
    status = []
    try:
        # logging in to portal (if required)
        login_to_portal_with_user_if_not_logged_in(page, credentials, delay)

        page.wait_for_timeout(delay)
        page.get_by_text("Detect Faces").click()
        page.wait_for_timeout(delay)

        # panels locator
        number_of_panels_displayed = page.locator('//div[@class="controller-panel-div posrel ftlft disblk lrg=panel-width"]').all()
        page.wait_for_timeout(3000)

        if len(number_of_panels_displayed) > 0:
            for _ in range(len(number_of_panels_displayed)):
                close_one_panel(page)
                page.wait_for_timeout(3000)

        number_of_panels_displayed = page.locator('//div[@class="controller-panel-div posrel ftlft disblk lrg=panel-width"]').all()
        page.wait_for_timeout(3000)

        if len(number_of_panels_displayed) > 0:
            status.append(False)
        else:
            status.append(True)

        if False in status:
            save_screenshot(page, test_id, screenshot_path, filename=f"{test_id}_failed.png")
            return False
        else:
            return True

    except Exception:
        save_screenshot(page, test_id, screenshot_path, filename=f"{test_id}_failed.png")
        return False
    finally:
        logout_if_logged_in(page)
```

### ✅ Reviewer Checklist (POM)
- [ ] Returns **bool** only (`True/False`)
- [ ] Uses `status.append(...)` for validations
- [ ] Final decision uses `if False in status` pattern
- [ ] `try/except/finally` present
- [ ] Screenshot saved on failure as `<test_id>_failed.png`
- [ ] **3000ms wait** after each locator/action
- [ ] Single responsibility (one action flow + one validation group)
- [ ] No hardcoded constants in POM (values come from fixtures/utilities)

---

## 3) Hardcoded Values → `conftest.py` (Mandatory)

All **hardcoded values** must be defined in `conftest.py` and exposed via fixtures:

- Timeouts (e.g., default 3000 ms)
- Paths (e.g., `screenshots` directory)
- Base URLs
- Credentials (prefer environment variables in CI)
- Feature flags / toggles


### ✅ Reviewer Checklist (conftest)
- [ ] All magic numbers/strings are defined here (or sourced from env)
- [ ] Fixtures provided for `delay`, `screenshot_path`, `credentials`, etc.
- [ ] Tests/POMs **do not** embed hardcoded constants

---

## 4) Reusable Functions → `utilities.py` (Mandatory)

All **reusable** actions/helpers must live in `utils/utilities.py`:

- Screenshot capture
- Login/logout
- Common UI actions, parsing, file IO, transformations, etc.

**Rules:**

- Utilities **should not assert**
- Prefer returning values/booleans and let POM decide pass/fail

### ✅ Reviewer Checklist (utilities)
- [ ] Shared logic resides in `utils/utilities.py`
- [ ] Utilities have no assertions
- [ ] POMs import and use these helpers


## 5) Quick Reference – Do & Don’t

**Tests (Do)**

- ✅ Exactly one POM call  
- ✅ `if/else + assert True/False`  

**Tests (Don’t)**

- ❌ No direct `assert function_call()`  
- ❌ No logger/try/except/extra logic  

**POM (Do)**

- ✅ Return `True/False`  
- ✅ Use `status.append(...)`  
- ✅ `if False in status` final decision  
- ✅ `try/except/finally`  
- ✅ Screenshot on failure  
- ✅ 3000 ms wait after each locator/action  

**POM (Don’t)**

- ❌ No assertions  
- ❌ No hardcoded constants  

**Fixtures/Utilities**

- ✅ Constants → `conftest.py` fixtures  
- ✅ Reusable code → `utilities.py`  

---