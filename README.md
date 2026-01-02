# 📱 Mobile QA Automation Project

A comprehensive QA-focused Mobile Application Automation project demonstrating **manual testing** and **Appium-based UI automation** for a native Android application.



---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Tools & Technologies](#tools--technologies)
- [Application Under Test](#application-under-test)
- [Project Structure](#project-structure)
- [Manual Test Coverage](#manual-test-coverage)
- [Automated Test Scenarios](#automated-test-scenarios)
- [Setup Instructions](#setup-instructions)
- [How to Run Tests](#how-to-run-tests)
- [Known Issues](#known-issues)

---

## 🎯 Project Overview

This project demonstrates a complete QA workflow including:

| Area | Description |
|------|-------------|
| **Manual Testing** | 12 detailed test cases covering login, forms, navigation, and error handling |
| **UI Automation** | Appium-based automated tests using Page Object Model (POM) |
| **UI Automation** | Appium-based automated tests using Page Object Model (POM) |

### Key QA Practices Demonstrated

✅ Manual → Automation Test Mapping  
✅ Page Object Model (POM) Design Pattern  
✅ Explicit Waits (No Hard Sleeps)  
✅ Screenshot Capture on Test Failure  
✅ Clear Assertions and Meaningful Test Names  
✅ Comprehensive Documentation  

---

## 🛠 Tools & Technologies

| Tool | Version | Purpose |
|------|---------|---------|
| **Python** | 3.9+ | Programming Language |
| **Appium** | 2.0+ | Mobile Automation Framework |
| **pytest** | 7.4+ | Test Framework |
| **Appium-Python-Client** | 3.1+ | Python Appium Bindings |
| **Appium-Python-Client** | 3.1+ | Python Appium Bindings |
| **pytest-html** | 4.1+ | HTML Test Reports |

### Supporting Tools

- **Android SDK** - Android development tools
- **UiAutomator2** - Android automation driver
- **Android Emulator** / Physical Device

---

## 📲 Application Under Test

**App**: WebdriverIO Native Demo App  
**Platform**: Android  
**Download**: [GitHub Releases](https://github.com/webdriverio/native-demo-app/releases)

### App Features Tested

- ✅ Login / Sign Up functionality
- ✅ Form input validation
- ✅ Multi-screen navigation
- ✅ Error message display

---

## 📁 Project Structure

```
mobile-qa-automation/
│
├── tests/                          # UI Automation Tests
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures & hooks
│   ├── login_test.py               # Login test cases
│   └── navigation_test.py          # Navigation test cases
│
├── pages/                          # Page Object Model Classes
│   ├── __init__.py
│   ├── BasePage.py                 # Base class with utilities
│   ├── LoginPage.py                # Login screen page object
│   └── HomePage.py                 # Home/Navigation page object
│

├── manual-test-cases/              # Manual Test Documentation
│   └── mobile_manual_test_cases.md # 12 detailed test cases
│
├── reports/                        # Generated Test Reports
├── screenshots/                    # Failure Screenshots
├── README.md                       # This file
└── requirements.txt                # Python dependencies
```

---

## 📝 Manual Test Coverage

12 manual test cases organized into 4 categories:

| Category | Test IDs | Priority |
|----------|----------|----------|
| **Login Functionality** | TC-001, TC-002, TC-003 | High |
| **Form Validation** | TC-004, TC-005, TC-006 | Medium |
| **Screen Navigation** | TC-007, TC-008, TC-009 | High/Medium |
| **Error Messages** | TC-010, TC-011, TC-012 | Medium |

📄 **Full Details**: See [manual-test-cases/mobile_manual_test_cases.md](manual-test-cases/mobile_manual_test_cases.md)

## 📈 Test Execution Metrics

The following metrics represent the latest test execution cycle.

| Metric | Count | Percentage |
|--------|-------|------------|
| **Total Test Cases** | 26 | 100% |
| **Passed** | 26 | 100% |
| **Failed** | 0 | 0% |
| **Skipped** | 0 | 0% |

> **Note**: Metrics reflect the combined coverage of Manual and Automated UI tests.


---

## 🤖 Automated Test Scenarios

### UI Tests (14 automated tests)

| Test File | Test Count | Coverage |
|-----------|------------|----------|
| `login_test.py` | 7 | Login flows, validation, error handling |
| `navigation_test.py` | 7 | Screen navigation, back navigation |



### Manual → Automation Mapping

| Manual Test ID | Automated Test | File |
|----------------|----------------|------|
| TC-001 | `test_login_with_valid_credentials` | login_test.py |
| TC-002 | `test_login_with_invalid_credentials` | login_test.py |
| TC-003 | `test_login_with_empty_fields` | login_test.py |
| TC-004 | `test_login_with_invalid_email_format` | login_test.py |
| TC-005 | `test_login_with_short_password` | login_test.py |
| TC-007 | `test_navigate_to_login_screen` | navigation_test.py |
| TC-008 | `test_navigate_to_forms_screen` | navigation_test.py |
| TC-009 | `test_navigate_to_webview_screen` | navigation_test.py |

---

## ⚙️ Setup Instructions

### Prerequisites

1. **Python 3.9+** installed
2. **Node.js** installed (for Appium)
3. **Java JDK 11+** installed
4. **Android SDK** with platform tools
5. **Android Emulator** or physical device

### Step 1: Install Appium Server

```bash
npm install -g appium
appium driver install uiautomator2
```

### Step 2: Clone and Setup Project

```bash
cd mobile-qa-automation
pip install -r requirements.txt
```

### Step 3: Download the Demo App

Download the APK from [WebdriverIO Native Demo App](https://github.com/webdriverio/native-demo-app/releases) and place it in the `app/` folder.

### Step 4: Configure Device

Update `tests/conftest.py` with your device details:

```python
ANDROID_CAPABILITIES = {
    "platformVersion": "YOUR_ANDROID_VERSION",
    "deviceName": "YOUR_DEVICE_NAME",
    "app": "PATH_TO_APK",
    ...
}
```

---

## 🚀 How to Run Tests

### Start Appium Server

```bash
appium
```

### Run Mobile UI Tests

```bash
# Run all UI tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/ui_report.html

# Run only smoke tests
pytest tests/ -v -m smoke

# Run only login tests
pytest tests/ -v -m login

# Run only navigation tests
pytest tests/ -v -m navigation
```



### Run All Tests

```bash
pytest . -v --html=reports/full_report.html
```

---

## ⚠️ Known Issues & Limitations

| Issue | Description | Workaround |
|-------|-------------|------------|
| **Emulator Performance** | Tests may be slower on emulator | Use physical device for faster execution |
| **Appium Server** | Must be running before tests | Start with `appium` command |
| **APK Path** | Path must be absolute | Update path in conftest.py |
| **API Demo Backend** | Uses mock API (reqres.in) | For demo purposes only |

### Troubleshooting

1. **Driver not found**: Ensure Appium server is running
2. **Element not found**: Increase wait timeout in BasePage.py
3. **App not installed**: Verify APK path in conftest.py

---

## 📊 Test Reports

Reports are generated in the `reports/` directory:

- `ui_report.html` - UI test results
- `ui_report.html` - UI test results
- `full_report.html` - Combined results

Screenshots of failed tests are saved in `screenshots/` directory.

---

## 👤 Author

**QA Intern Portfolio Project**

---

## 📄 License

This project is for educational and portfolio purposes.
