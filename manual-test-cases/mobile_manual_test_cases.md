# Mobile Application Manual Test Cases

## Application Under Test
**App**: Android NativeDemoApp (WebdriverIO Demo App)  
**Version**: Latest  
**Platform**: Android 10+

---

## Test Case Categories
1. [Login Functionality](#1-login-functionality)
2. [Form Input Validation](#2-form-input-validation)
3. [Screen Navigation](#3-screen-navigation)
4. [Error Message Display](#4-error-message-display)

---

## 1. Login Functionality

### TC-001: Successful Login with Valid Credentials

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-001 |
| **Priority** | High |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Login screen<br>3. Valid test credentials are available |
| **Steps** | 1. Tap on the "Login" tab in the navigation bar<br>2. Enter valid email: `test@example.com`<br>3. Enter valid password: `Password123`<br>4. Tap the "Login" button |
| **Expected Result** | - Login successful popup/alert is displayed<br>- User credentials are validated<br>- Success message confirms login |

---

### TC-002: Failed Login with Invalid Password

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-002 |
| **Priority** | High |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Login screen |
| **Steps** | 1. Tap on the "Login" tab in the navigation bar<br>2. Enter valid email: `test@example.com`<br>3. Enter invalid password: `wrongpass`<br>4. Tap the "Login" button |
| **Expected Result** | - Error message is displayed<br>- Login is not successful<br>- User remains on Login screen |

---

### TC-003: Login with Empty Fields

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-003 |
| **Priority** | High |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Login screen |
| **Steps** | 1. Tap on the "Login" tab in the navigation bar<br>2. Leave email field empty<br>3. Leave password field empty<br>4. Tap the "Login" button |
| **Expected Result** | - Validation error messages are displayed for both fields<br>- Login button action is blocked<br>- User remains on Login screen |

---

## 2. Form Input Validation

### TC-004: Email Field Validation - Invalid Format

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-004 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Login screen |
| **Steps** | 1. Tap on the "Login" tab<br>2. Enter invalid email format: `invalidemail`<br>3. Tap on password field or elsewhere to trigger validation |
| **Expected Result** | - Error message displayed: "Please enter a valid email address"<br>- Email field highlighted with error indicator |

---

### TC-005: Password Field Validation - Minimum Length

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-005 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Login screen |
| **Steps** | 1. Tap on the "Login" tab<br>2. Enter valid email: `test@example.com`<br>3. Enter short password: `abc`<br>4. Tap elsewhere to trigger validation |
| **Expected Result** | - Error message displayed indicating minimum password length requirement<br>- Password field highlighted with error indicator |

---

### TC-006: Sign Up Form - Password Mismatch

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-006 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Sign Up tab of Login screen |
| **Steps** | 1. Navigate to Login screen and tap "Sign up" tab<br>2. Enter email: `newuser@example.com`<br>3. Enter password: `Password123`<br>4. Enter confirm password: `DifferentPass`<br>5. Tap "Sign up" button |
| **Expected Result** | - Error message displayed: "Passwords do not match"<br>- Sign up is blocked<br>- Confirm password field shows error indicator |

---

## 3. Screen Navigation

### TC-007: Navigate from Home to Login Screen

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-007 |
| **Priority** | High |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Home screen |
| **Steps** | 1. Locate the bottom navigation bar<br>2. Tap on "Login" icon/tab |
| **Expected Result** | - Login screen is displayed<br>- Login form with email and password fields is visible<br>- Login and Sign up tabs are visible |

---

### TC-008: Navigate from Home to Forms Screen

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-008 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Home screen |
| **Steps** | 1. Locate the bottom navigation bar<br>2. Tap on "Forms" icon/tab |
| **Expected Result** | - Forms screen is displayed<br>- Form elements (input fields, switches, dropdowns) are visible |

---

### TC-009: Navigate to Webview Screen

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-009 |
| **Priority** | Low |
| **Preconditions** | 1. App is installed and launched<br>2. User is on the Home screen |
| **Steps** | 1. Locate the bottom navigation bar<br>2. Tap on "Webview" icon/tab |
| **Expected Result** | - Webview screen is displayed<br>- URL input field is visible<br>- Web content area is present |

---

## 4. Error Message Display

### TC-010: Error Message for Network Failure (Simulated)

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-010 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. Device network is disabled (Airplane mode) |
| **Steps** | 1. Enable Airplane mode on device<br>2. Navigate to Login screen<br>3. Enter valid credentials<br>4. Tap Login button |
| **Expected Result** | - Appropriate error message for network unavailability<br>- App handles the error gracefully without crashing |

---

### TC-011: Error Pop-up Dismissal

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-011 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. An error message is displayed |
| **Steps** | 1. Trigger any error (e.g., invalid login)<br>2. Observe the error message/popup<br>3. Tap "OK" or dismiss button on the popup |
| **Expected Result** | - Error popup is dismissed<br>- User can continue interacting with the app<br>- Previous screen state is maintained |

---

### TC-012: Validation Error Visibility

| Field | Details |
|-------|---------|
| **Test Case ID** | TC-012 |
| **Priority** | Medium |
| **Preconditions** | 1. App is installed and launched<br>2. User is on Login screen |
| **Steps** | 1. Enter invalid data in email field<br>2. Observe error message<br>3. Scroll if needed to view the error |
| **Expected Result** | - Error message text is clearly visible<br>- Error message is displayed near the relevant field<br>- Text is readable (appropriate font size and color) |

---

## Test Coverage Summary

| Category | Total Tests | Priority Breakdown |
|----------|-------------|-------------------|
| Login Functionality | 3 | High: 3 |
| Form Input Validation | 3 | Medium: 3 |
| Screen Navigation | 3 | High: 1, Medium: 1, Low: 1 |
| Error Message Display | 3 | Medium: 3 |
| **Total** | **12** | High: 4, Medium: 7, Low: 1 |

---

## Automation Mapping

| Manual Test ID | Automated Test | File |
|----------------|----------------|------|
| TC-001 | test_login_with_valid_credentials | login_test.py |
| TC-002 | test_login_with_invalid_credentials | login_test.py |
| TC-003 | test_login_with_empty_fields | login_test.py |
| TC-007 | test_navigate_to_login_screen | navigation_test.py |
| TC-008 | test_navigate_to_forms_screen | navigation_test.py |
