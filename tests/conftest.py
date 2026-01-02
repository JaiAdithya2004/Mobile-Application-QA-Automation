"""
Pytest Configuration and Fixtures for Mobile Automation Tests
Contains Appium driver setup, configuration, and test hooks
"""

import pytest
import os
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options


# --- Configuration ---
# Appium Server Configuration
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# Android Device Capabilities
ANDROID_CAPABILITIES = {
    "platformName": "Android",
    "platformVersion": "13",  # Updated for connected device
    "deviceName": "4hnfq4uozlmfxsba",  # Connected device ID
    "automationName": "UiAutomator2",
    "app": os.path.join(os.path.dirname(os.path.dirname(__file__)), "app", "android.wdio.native.app.v2.0.0.apk"),
    "appPackage": "com.wdiodemoapp",
    "appActivity": "com.wdiodemoapp.MainActivity",
    "noReset": False,
    "fullReset": False,
    "newCommandTimeout": 300,
    "autoGrantPermissions": True
}


# --- Fixtures ---

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that provides an Appium driver instance.
    
    Scope: function - creates a new driver for each test
    
    Yields:
        Appium WebDriver instance
    """
    # Set up Appium options
    options = UiAutomator2Options()
    options.load_capabilities(ANDROID_CAPABILITIES)
    
    # Initialize the driver
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown - quit driver after test
    driver.quit()


@pytest.fixture(scope="session")
def driver_session():
    """
    Session-scoped driver fixture for tests that need to share state.
    Use sparingly - prefer function-scoped driver for test isolation.
    
    Yields:
        Appium WebDriver instance
    """
    options = UiAutomator2Options()
    options.load_capabilities(ANDROID_CAPABILITIES)
    
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


# --- Hooks ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshots on test failure.
    
    This hook runs after each test phase (setup, call, teardown)
    and captures a screenshot if the test fails.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get the driver from the test's fixtures
        driver = item.funcargs.get("driver") or item.funcargs.get("driver_session")
        
        if driver:
            # Create screenshots directory
            screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            # Generate screenshot filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            test_name = item.name.replace("[", "_").replace("]", "_")
            filename = f"FAILURE_{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)
            
            # Capture screenshot
            try:
                driver.save_screenshot(filepath)
                print(f"\nScreenshot saved: {filepath}")
            except Exception as e:
                print(f"\nFailed to capture screenshot: {e}")


def pytest_configure(config):
    """
    Pytest configuration hook.
    Sets up custom markers and reporting.
    """
    config.addinivalue_line("markers", "smoke: mark test as smoke test")
    config.addinivalue_line("markers", "regression: mark test as regression test")
    config.addinivalue_line("markers", "login: mark test as login related")
    config.addinivalue_line("markers", "navigation: mark test as navigation related")


def pytest_html_report_title(report):
    """Custom title for HTML report."""
    report.title = "Mobile QA Automation Test Report"


# --- Helper Functions ---

def get_screenshot_path(test_name):
    """
    Generate a path for saving screenshots.
    
    Args:
        test_name: Name of the test
        
    Returns:
        Full path for the screenshot file
    """
    screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{test_name}_{timestamp}.png"
    
    return os.path.join(screenshot_dir, filename)
