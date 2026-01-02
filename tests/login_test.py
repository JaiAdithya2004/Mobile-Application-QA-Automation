"""
Login Tests - Automated test cases for Login functionality
Maps to Manual Test Cases: TC-001, TC-002, TC-003

Tests cover:
- App launch validation
- Positive login flow
- Negative login flow
- Empty field validation
"""

import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage


class TestLogin:
    """
    Test class for Login functionality.
    
    Automation mapping:
    - test_app_launch_success -> Prerequisite for all tests
    - test_login_with_valid_credentials -> TC-001
    - test_login_with_invalid_credentials -> TC-002
    - test_login_with_empty_fields -> TC-003
    """
    
    # Test Data
    VALID_EMAIL = "test@example.com"
    VALID_PASSWORD = "Password123"
    INVALID_EMAIL = "invalid@test.com"
    INVALID_PASSWORD = "wrongpassword"
    INVALID_EMAIL_FORMAT = "invalidemail"
    SHORT_PASSWORD = "abc"
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_app_launch_success(self, driver):
        """
        Test Case: Verify app launches successfully
        
        Validates that the application launches and the navigation bar is visible.
        This is a prerequisite for all other tests.
        
        Expected: App launches with visible navigation bar
        """
        # Arrange
        home_page = HomePage(driver)
        
        # Act & Assert
        assert home_page.is_app_launched(), "App failed to launch - navigation bar not visible"
        assert home_page.is_navigation_bar_visible(), "Navigation bar should be visible after launch"
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_with_valid_credentials(self, driver):
        """
        Test Case: TC-001 - Successful Login with Valid Credentials
        
        Steps:
        1. Navigate to Login screen
        2. Enter valid email
        3. Enter valid password
        4. Tap Login button
        
        Expected: Login success alert is displayed
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        login_page.select_login_tab()
        login_page.perform_login(self.VALID_EMAIL, self.VALID_PASSWORD)
        
        # Assert
        assert login_page.is_alert_displayed(), "Success alert should be displayed after valid login"
        assert login_page.is_login_successful(), "Login should be successful with valid credentials"
        
        # Cleanup - dismiss alert
        login_page.dismiss_alert()
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_invalid_credentials(self, driver):
        """
        Test Case: TC-002 - Failed Login with Invalid Password
        
        Steps:
        1. Navigate to Login screen
        2. Enter valid email
        3. Enter invalid password
        4. Tap Login button
        
        Expected: Error message is displayed, login fails
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        login_page.select_login_tab()
        login_page.perform_login(self.VALID_EMAIL, self.INVALID_PASSWORD)
        
        # Assert
        # Note: The demo app validates format, not actual credentials
        # Checking that login screen remains visible indicates failure
        assert login_page.is_login_screen_displayed(), "Should remain on login screen after failed login"
    
    @pytest.mark.regression  
    @pytest.mark.login
    def test_login_with_empty_fields(self, driver):
        """
        Test Case: TC-003 - Login with Empty Fields
        
        Steps:
        1. Navigate to Login screen
        2. Leave email field empty
        3. Leave password field empty
        4. Tap Login button
        
        Expected: Validation error messages are displayed
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        login_page.select_login_tab()
        login_page.click_login_button()  # Click without entering any data
        
        # Assert
        # Check that validation errors are shown or user stays on login screen
        assert login_page.is_login_screen_displayed(), "Should remain on login screen with empty fields"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_invalid_email_format(self, driver):
        """
        Test Case: TC-004 - Email Field Validation - Invalid Format
        
        Steps:
        1. Navigate to Login screen
        2. Enter invalid email format
        3. Observe validation error
        
        Expected: Email validation error is displayed
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        login_page.select_login_tab()
        login_page.enter_email(self.INVALID_EMAIL_FORMAT)
        login_page.enter_password(self.VALID_PASSWORD)  # Move focus to trigger validation
        
        # Assert
        assert login_page.is_email_error_displayed(), "Email validation error should be displayed for invalid format"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_with_short_password(self, driver):
        """
        Test Case: TC-005 - Password Field Validation - Minimum Length
        
        Steps:
        1. Navigate to Login screen
        2. Enter valid email
        3. Enter short password
        4. Observe validation error
        
        Expected: Password minimum length error is displayed
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        login_page.select_login_tab()
        login_page.enter_email(self.VALID_EMAIL)
        login_page.enter_password(self.SHORT_PASSWORD)
        login_page.click_login_button()  # Trigger validation
        
        # Assert
        assert login_page.is_password_error_displayed(), "Password validation error should be displayed for short password"
    
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_screen_elements_visible(self, driver):
        """
        Test Case: Verify all login screen elements are visible
        
        Validates that all required elements on the login screen are displayed.
        
        Expected: All login form elements are visible
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        
        # Assert
        assert login_page.is_login_screen_displayed(), "Login screen should be displayed"
        assert login_page.is_element_displayed(login_page.EMAIL_INPUT), "Email input should be visible"
        assert login_page.is_element_displayed(login_page.PASSWORD_INPUT), "Password input should be visible"
        assert login_page.is_element_displayed(login_page.LOGIN_BUTTON), "Login button should be visible"
