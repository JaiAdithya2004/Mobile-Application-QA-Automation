"""
BasePage - Base class for all page objects
Contains common utilities and methods used across all pages
"""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
from datetime import datetime


class BasePage:
    """
    Base class containing common methods for all page objects.
    Implements explicit waits and utility functions.
    """
    
    def __init__(self, driver):
        """
        Initialize the BasePage with the Appium driver.
        
        Args:
            driver: Appium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.short_wait = WebDriverWait(driver, 5)
    
    # --- Wait Methods (Explicit Waits - No Hard Sleeps) ---
    
    def wait_for_element_visible(self, locator, timeout=15):
        """
        Wait for an element to be visible on the screen.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement if found
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=15):
        """
        Wait for an element to be clickable.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement if found and clickable
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_element_present(self, locator, timeout=15):
        """
        Wait for an element to be present in the DOM.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement if found
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    # --- Element Interaction Methods ---
    
    def click_element(self, locator):
        """
        Click on an element after waiting for it to be clickable.
        
        Args:
            locator: Tuple of (By strategy, locator string)
        """
        element = self.wait_for_element_clickable(locator)
        element.click()
    
    def enter_text(self, locator, text):
        """
        Enter text into an input field after clearing it.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            text: Text to enter
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    def get_element_text(self, locator):
        """
        Get the text content of an element.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            
        Returns:
            String text of the element
        """
        element = self.wait_for_element_visible(locator)
        return element.text
    
    def is_element_displayed(self, locator, timeout=5):
        """
        Check if an element is displayed on screen.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            timeout: Maximum wait time
            
        Returns:
            Boolean - True if displayed, False otherwise
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def is_element_present(self, locator, timeout=5):
        """
        Check if an element is present in the DOM.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            timeout: Maximum wait time
            
        Returns:
            Boolean - True if present, False otherwise
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    # --- Screenshot Methods ---
    
    def take_screenshot(self, name=None):
        """
        Take a screenshot and save it to the screenshots directory.
        
        Args:
            name: Optional name for the screenshot file
            
        Returns:
            Path to the saved screenshot
        """
        # Create screenshots directory if it doesn't exist
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        if name:
            filename = f"{name}_{timestamp}.png"
        else:
            filename = f"screenshot_{timestamp}.png"
        
        filepath = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(filepath)
        
        return filepath
    
    def take_failure_screenshot(self, test_name):
        """
        Take a screenshot specifically for test failures.
        
        Args:
            test_name: Name of the failed test
            
        Returns:
            Path to the saved screenshot
        """
        return self.take_screenshot(f"FAILURE_{test_name}")
    
    # --- Navigation Methods ---
    
    def go_back(self):
        """Navigate back using device back button."""
        self.driver.back()
    
    def get_page_source(self):
        """
        Get the current page source for debugging.
        
        Returns:
            String containing the page source XML
        """
        return self.driver.page_source
    
    # --- Attribute Methods ---
    
    def get_element_attribute(self, locator, attribute):
        """
        Get a specific attribute value of an element.
        
        Args:
            locator: Tuple of (By strategy, locator string)
            attribute: Name of the attribute
            
        Returns:
            Attribute value as string
        """
        element = self.wait_for_element_visible(locator)
        return element.get_attribute(attribute)
