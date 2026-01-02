"""
Navigation Tests - Automated test cases for Screen Navigation
Maps to Manual Test Cases: TC-007, TC-008, TC-009

Tests cover:
- Navigation to Login screen
- Navigation to Forms screen
- Navigation to Webview screen
- Back navigation
"""

import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class TestNavigation:
    """
    Test class for Navigation functionality.
    
    Automation mapping:
    - test_navigate_to_login_screen -> TC-007
    - test_navigate_to_forms_screen -> TC-008
    - test_navigate_to_webview_screen -> TC-009
    """
    
    @pytest.mark.smoke
    @pytest.mark.navigation
    def test_navigate_to_login_screen(self, driver):
        """
        Test Case: TC-007 - Navigate from Home to Login Screen
        
        Steps:
        1. Ensure app is on home screen
        2. Tap on Login icon in navigation bar
        
        Expected: Login screen is displayed with email and password fields
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act
        home_page.navigate_to_login()
        
        # Assert
        assert login_page.is_login_screen_displayed(), "Login screen should be displayed after navigation"
        assert login_page.is_element_displayed(login_page.EMAIL_INPUT), "Email input should be visible on login screen"
        assert login_page.is_element_displayed(login_page.PASSWORD_INPUT), "Password input should be visible on login screen"
    
    @pytest.mark.smoke
    @pytest.mark.navigation
    def test_navigate_to_forms_screen(self, driver):
        """
        Test Case: TC-008 - Navigate from Home to Forms Screen
        
        Steps:
        1. Ensure app is on home screen
        2. Tap on Forms icon in navigation bar
        
        Expected: Forms screen is displayed with form elements
        """
        # Arrange
        home_page = HomePage(driver)
        
        # Act
        home_page.navigate_to_forms()
        
        # Assert
        assert home_page.is_forms_screen_displayed(), "Forms screen should be displayed after navigation"
        assert home_page.is_element_displayed(home_page.FORMS_INPUT_FIELD), "Forms input field should be visible"
    
    @pytest.mark.regression
    @pytest.mark.navigation
    def test_navigate_to_webview_screen(self, driver):
        """
        Test Case: TC-009 - Navigate to Webview Screen
        
        Steps:
        1. Ensure app is on home screen
        2. Tap on Webview icon in navigation bar
        
        Expected: Webview screen is displayed with URL input field
        """
        # Arrange
        home_page = HomePage(driver)
        
        # Act
        home_page.navigate_to_webview()
        
        # Assert
        assert home_page.is_webview_screen_displayed(), "Webview screen should be displayed after navigation"
    
    @pytest.mark.regression
    @pytest.mark.navigation
    def test_navigate_back_to_home(self, driver):
        """
        Test Case: Navigate back to Home screen
        
        Steps:
        1. Navigate to Login screen
        2. Navigate back to Home screen
        
        Expected: Home screen is displayed
        """
        # Arrange
        home_page = HomePage(driver)
        
        # Act
        home_page.navigate_to_login()  # Go away from home
        home_page.navigate_to_home()   # Navigate back
        
        # Assert
        assert home_page.is_home_screen_displayed(), "Home screen should be displayed after navigating back"
    
    @pytest.mark.regression
    @pytest.mark.navigation
    def test_navigation_bar_always_visible(self, driver):
        """
        Test Case: Navigation bar remains visible across screens
        
        Steps:
        1. Navigate to multiple screens
        2. Verify navigation bar is visible on each
        
        Expected: Navigation bar is visible on all screens
        """
        # Arrange
        home_page = HomePage(driver)
        
        # Act & Assert - Check on Home
        assert home_page.is_navigation_bar_visible(), "Navigation bar should be visible on Home screen"
        
        # Navigate to Login and verify
        home_page.navigate_to_login()
        assert home_page.is_navigation_bar_visible(), "Navigation bar should be visible on Login screen"
        
        # Navigate to Forms and verify
        home_page.navigate_to_forms()
        assert home_page.is_navigation_bar_visible(), "Navigation bar should be visible on Forms screen"
    
    @pytest.mark.regression
    @pytest.mark.navigation
    def test_sequential_navigation(self, driver):
        """
        Test Case: Navigate through multiple screens sequentially
        
        Steps:
        1. Navigate Home -> Login -> Forms -> Webview -> Home
        
        Expected: Each screen is displayed correctly
        """
        # Arrange
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Act & Assert
        # Step 1: Home to Login
        home_page.navigate_to_login()
        assert login_page.is_login_screen_displayed(), "Login screen should be displayed"
        
        # Step 2: Login to Forms
        home_page.navigate_to_forms()
        assert home_page.is_forms_screen_displayed(), "Forms screen should be displayed"
        
        # Step 3: Forms to Webview
        home_page.navigate_to_webview()
        assert home_page.is_webview_screen_displayed(), "Webview screen should be displayed"
        
        # Step 4: Back to Home
        home_page.navigate_to_home()
        assert home_page.is_home_screen_displayed(), "Home screen should be displayed"
    
    @pytest.mark.regression
    @pytest.mark.navigation
    def test_forms_input_interaction(self, driver):
        """
        Test Case: Verify forms screen input interaction
        
        Steps:
        1. Navigate to Forms screen
        2. Enter text in input field
        3. Verify text is entered
        
        Expected: Text is successfully entered in the forms field
        """
        # Arrange
        home_page = HomePage(driver)
        test_text = "Test Input"
        
        # Act
        home_page.navigate_to_forms()
        home_page.enter_text_in_forms_field(test_text)
        
        # Assert
        assert home_page.is_forms_screen_displayed(), "Should remain on Forms screen after input"
