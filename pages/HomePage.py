"""
HomePage - Page Object for Home Screen
Contains locators and methods for home/navigation functionality
"""

from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class HomePage(BasePage):
    """
    Page Object representing the Home screen of the NativeDemoApp.
    Handles navigation to different sections of the app.
    """
    
    # --- Locators ---
    # Bottom Navigation Bar Items
    HOME_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Home")
    WEBVIEW_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Webview")
    LOGIN_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login")
    FORMS_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Forms")
    SWIPE_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Swipe")
    DRAG_NAV_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Drag")
    
    # Home Screen Elements
    HOME_SCREEN_LOGO = (AppiumBy.ACCESSIBILITY_ID, "Home-screen")
    WEBDRIVERIO_LOGO = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='WEBDRIVER']")
    
    # Forms Screen Elements
    FORMS_INPUT_FIELD = (AppiumBy.ACCESSIBILITY_ID, "text-input")
    FORMS_SWITCH = (AppiumBy.ACCESSIBILITY_ID, "switch")
    FORMS_DROPDOWN = (AppiumBy.ACCESSIBILITY_ID, "Dropdown")
    
    # Webview Screen Elements
    WEBVIEW_URL_INPUT = (AppiumBy.ACCESSIBILITY_ID, "URL input field")
    
    # --- Navigation Methods ---
    
    def navigate_to_home(self):
        """Navigate to the Home screen."""
        self.click_element(self.HOME_NAV_BUTTON)
        return self
    
    def navigate_to_login(self):
        """Navigate to the Login screen from navigation bar."""
        self.click_element(self.LOGIN_NAV_BUTTON)
        return self
    
    def navigate_to_forms(self):
        """Navigate to the Forms screen."""
        self.click_element(self.FORMS_NAV_BUTTON)
        return self
    
    def navigate_to_webview(self):
        """Navigate to the Webview screen."""
        self.click_element(self.WEBVIEW_NAV_BUTTON)
        return self
    
    def navigate_to_swipe(self):
        """Navigate to the Swipe screen."""
        self.click_element(self.SWIPE_NAV_BUTTON)
        return self
    
    def navigate_to_drag(self):
        """Navigate to the Drag screen."""
        self.click_element(self.DRAG_NAV_BUTTON)
        return self
    
    # --- Verification Methods ---
    
    def is_home_screen_displayed(self):
        """
        Check if the home screen is displayed.
        
        Returns:
            Boolean - True if home screen is visible
        """
        return self.is_element_displayed(self.HOME_NAV_BUTTON)
    
    def is_forms_screen_displayed(self):
        """
        Check if the forms screen is displayed.
        
        Returns:
            Boolean - True if forms screen is visible
        """
        return self.is_element_displayed(self.FORMS_INPUT_FIELD)
    
    def is_webview_screen_displayed(self):
        """
        Check if the webview screen is displayed.
        
        Returns:
            Boolean - True if webview screen is visible
        """
        return self.is_element_displayed(self.WEBVIEW_URL_INPUT)
    
    def is_navigation_bar_visible(self):
        """
        Check if the bottom navigation bar is visible.
        
        Returns:
            Boolean - True if navigation bar is visible
        """
        return (self.is_element_displayed(self.HOME_NAV_BUTTON) and 
                self.is_element_displayed(self.LOGIN_NAV_BUTTON))
    
    # --- Forms Screen Actions ---
    
    def enter_text_in_forms_field(self, text):
        """
        Enter text in the forms input field.
        
        Args:
            text: Text to enter
        """
        self.enter_text(self.FORMS_INPUT_FIELD, text)
        return self
    
    def toggle_switch(self):
        """Toggle the switch on forms screen."""
        self.click_element(self.FORMS_SWITCH)
        return self
    
    def get_forms_input_text(self):
        """
        Get the text from forms input field.
        
        Returns:
            String - Current text in the input field
        """
        return self.get_element_text(self.FORMS_INPUT_FIELD)
    
    # --- App State Methods ---
    
    def is_app_launched(self):
        """
        Verify the app has launched successfully.
        
        Returns:
            Boolean - True if app is launched and home screen visible
        """
        return self.is_navigation_bar_visible()
    
    def get_current_screen(self):
        """
        Determine which screen is currently displayed.
        
        Returns:
            String - Name of the current screen
        """
        if self.is_element_displayed(self.HOME_SCREEN_LOGO, timeout=2):
            return "Home"
        elif self.is_element_displayed(self.FORMS_INPUT_FIELD, timeout=2):
            return "Forms"
        elif self.is_element_displayed(self.WEBVIEW_URL_INPUT, timeout=2):
            return "Webview"
        else:
            return "Unknown"
