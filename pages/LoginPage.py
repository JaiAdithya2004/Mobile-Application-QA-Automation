"""
LoginPage - Page Object for Login Screen
Contains locators and methods for login functionality
"""

from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class LoginPage(BasePage):
    """
    Page Object representing the Login screen of the NativeDemoApp.
    Handles login, sign up, and validation error interactions.
    """
    
    # --- Locators ---
    # Navigation
    LOGIN_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login")
    
    # Tab selectors
    LOGIN_TAB = (AppiumBy.ACCESSIBILITY_ID, "button-login-container")
    SIGNUP_TAB = (AppiumBy.ACCESSIBILITY_ID, "button-sign-up-container")
    
    # Login form fields
    EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input-email")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input-password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "button-LOGIN")
    
    # Sign up form fields
    SIGNUP_EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input-email")
    SIGNUP_PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input-password")
    SIGNUP_CONFIRM_PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "input-repeat-password")
    SIGNUP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "button-SIGN UP")
    
    # Error/Validation messages
    EMAIL_ERROR_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Please enter a valid email')]")
    PASSWORD_ERROR_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Please enter at least 8 characters')]")
    
    # Success/Error popup
    SUCCESS_ALERT_TITLE = (AppiumBy.ID, "android:id/alertTitle")
    ALERT_MESSAGE = (AppiumBy.ID, "android:id/message")
    ALERT_OK_BUTTON = (AppiumBy.ID, "android:id/button1")
    
    # --- Navigation Methods ---
    
    def navigate_to_login(self):
        """Navigate to the Login screen from the bottom navigation bar."""
        self.click_element(self.LOGIN_NAV_BUTTON)
        return self
    
    def select_login_tab(self):
        """Select the Login tab on the Login screen."""
        self.click_element(self.LOGIN_TAB)
        return self
    
    def select_signup_tab(self):
        """Select the Sign Up tab on the Login screen."""
        self.click_element(self.SIGNUP_TAB)
        return self
    
    # --- Login Actions ---
    
    def enter_email(self, email):
        """
        Enter email address in the email field.
        
        Args:
            email: Email address to enter
        """
        self.enter_text(self.EMAIL_INPUT, email)
        return self
    
    def enter_password(self, password):
        """
        Enter password in the password field.
        
        Args:
            password: Password to enter
        """
        self.enter_text(self.PASSWORD_INPUT, password)
        return self
    
    def click_login_button(self):
        """Click the Login button."""
        self.click_element(self.LOGIN_BUTTON)
        return self
    
    def perform_login(self, email, password):
        """
        Perform complete login flow.
        
        Args:
            email: Email address
            password: Password
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        return self
    
    # --- Sign Up Actions ---
    
    def enter_signup_email(self, email):
        """Enter email in sign up form."""
        self.enter_text(self.SIGNUP_EMAIL_INPUT, email)
        return self
    
    def enter_signup_password(self, password):
        """Enter password in sign up form."""
        self.enter_text(self.SIGNUP_PASSWORD_INPUT, password)
        return self
    
    def enter_confirm_password(self, password):
        """Enter confirm password in sign up form."""
        self.enter_text(self.SIGNUP_CONFIRM_PASSWORD_INPUT, password)
        return self
    
    def click_signup_button(self):
        """Click the Sign Up button."""
        self.click_element(self.SIGNUP_BUTTON)
        return self
    
    # --- Validation Methods ---
    
    def is_login_screen_displayed(self):
        """
        Check if the login screen is displayed.
        
        Returns:
            Boolean - True if login screen is visible
        """
        return self.is_element_displayed(self.EMAIL_INPUT)
    
    def is_email_error_displayed(self):
        """
        Check if email validation error is displayed.
        
        Returns:
            Boolean - True if email error is visible
        """
        return self.is_element_displayed(self.EMAIL_ERROR_TEXT, timeout=3)
    
    def is_password_error_displayed(self):
        """
        Check if password validation error is displayed.
        
        Returns:
            Boolean - True if password error is visible
        """
        return self.is_element_displayed(self.PASSWORD_ERROR_TEXT, timeout=3)
    
    def get_email_error_message(self):
        """
        Get the email validation error message text.
        
        Returns:
            String - Error message text
        """
        return self.get_element_text(self.EMAIL_ERROR_TEXT)
    
    def get_password_error_message(self):
        """
        Get the password validation error message text.
        
        Returns:
            String - Error message text
        """
        return self.get_element_text(self.PASSWORD_ERROR_TEXT)
    
    # --- Alert/Popup Methods ---
    
    def is_alert_displayed(self):
        """
        Check if an alert/popup is displayed.
        
        Returns:
            Boolean - True if alert is visible
        """
        return self.is_element_displayed(self.SUCCESS_ALERT_TITLE, timeout=5)
    
    def get_alert_title(self):
        """
        Get the alert title text.
        
        Returns:
            String - Alert title
        """
        return self.get_element_text(self.SUCCESS_ALERT_TITLE)
    
    def get_alert_message(self):
        """
        Get the alert message text.
        
        Returns:
            String - Alert message
        """
        return self.get_element_text(self.ALERT_MESSAGE)
    
    def dismiss_alert(self):
        """Dismiss the alert by clicking OK button."""
        self.click_element(self.ALERT_OK_BUTTON)
        return self
    
    def is_login_successful(self):
        """
        Check if login was successful by verifying success alert.
        
        Returns:
            Boolean - True if success alert is displayed
        """
        if self.is_alert_displayed():
            title = self.get_alert_title()
            return "Success" in title
        return False
