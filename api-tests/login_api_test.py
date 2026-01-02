"""
API Tests - Backend API Validation
Demonstrates basic API testing for mobile app backend validation

Tests cover:
- Valid API requests
- Invalid request handling
- Response structure validation
- Error response handling

Note: Using httpbin.org as a reliable demo API for testing.
In a real scenario, this would test the actual backend API used by the mobile app.
"""

import pytest
import requests


class TestLoginAPI:
    """
    Test class demonstrating Login API-style endpoint validation.
    
    Uses httpbin.org for reliable testing. Demonstrates:
    - POST request handling
    - Status code validation
    - Response structure validation
    - Error handling patterns
    """
    
    # API Configuration - Using httpbin.org for reliable demo
    BASE_URL = "https://httpbin.org"
    POST_ENDPOINT = f"{BASE_URL}/post"
    STATUS_ENDPOINT = f"{BASE_URL}/status"
    
    # Test Data (simulating login credentials)
    VALID_CREDENTIALS = {
        "email": "test@example.com",
        "password": "Password123"
    }
    
    MISSING_PASSWORD = {
        "email": "test@example.com"
    }
    
    # Request Headers
    HEADERS = {
        "Content-Type": "application/json"
    }
    
    @pytest.mark.smoke
    def test_login_api_valid_credentials(self):
        """
        Test Case: Simulate Login API with valid credentials
        
        Validates:
        - HTTP status code is 200
        - Response contains posted data
        - Request was properly received
        
        Expected: Successful POST with data echoed back
        """
        # Arrange & Act
        response = requests.post(
            self.POST_ENDPOINT,
            json=self.VALID_CREDENTIALS,
            headers=self.HEADERS
        )
        
        # Assert - Status Code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert - Response Structure
        response_json = response.json()
        assert "json" in response_json, "Response should contain 'json' field (echoed data)"
        assert response_json["json"]["email"] == self.VALID_CREDENTIALS["email"], \
            "Email should be echoed back correctly"
    
    @pytest.mark.regression
    def test_login_api_incomplete_data(self):
        """
        Test Case: API request with missing password field
        
        Validates:
        - Request is still processed (httpbin echoes data)
        - Only submitted fields are present in response
        
        Expected: Request processed, only email in response
        """
        # Arrange & Act
        response = requests.post(
            self.POST_ENDPOINT,
            json=self.MISSING_PASSWORD,
            headers=self.HEADERS
        )
        
        # Assert - Status Code (httpbin accepts any data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert - Response Structure shows missing password
        response_json = response.json()
        assert "json" in response_json, "Response should contain 'json' field"
        assert "password" not in response_json["json"], "Password should be missing from request"
    
    @pytest.mark.regression
    def test_api_empty_request_body(self):
        """
        Test Case: API with empty request body
        
        Validates:
        - API handles empty body gracefully
        - Returns 200 with empty json field
        
        Expected: Successful response with empty data
        """
        # Arrange & Act
        response = requests.post(
            self.POST_ENDPOINT,
            json={},
            headers=self.HEADERS
        )
        
        # Assert - Status Code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert - Empty json in response
        response_json = response.json()
        assert response_json["json"] == {}, "Empty JSON should be echoed"
    
    @pytest.mark.regression
    def test_api_response_time(self):
        """
        Test Case: API response time validation
        
        Validates:
        - API responds within acceptable time limit (< 5 seconds)
        
        Expected: Response received within 5 seconds
        """
        # Arrange & Act
        response = requests.post(
            self.POST_ENDPOINT,
            json=self.VALID_CREDENTIALS,
            headers=self.HEADERS,
            timeout=10
        )
        
        # Assert - Response Time
        assert response.elapsed.total_seconds() < 5, \
            f"Response time {response.elapsed.total_seconds()}s exceeds 5s threshold"
    
    @pytest.mark.regression
    def test_api_content_type_header(self):
        """
        Test Case: Verify API returns correct content type
        
        Validates:
        - Response Content-Type header is application/json
        
        Expected: JSON content type in response
        """
        # Arrange & Act
        response = requests.post(
            self.POST_ENDPOINT,
            json=self.VALID_CREDENTIALS,
            headers=self.HEADERS
        )
        
        # Assert - Content Type
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, \
            f"Expected JSON content type, got: {content_type}"
    
    @pytest.mark.regression
    def test_error_status_code_400(self):
        """
        Test Case: Validate 400 Bad Request response
        
        Validates:
        - API returns correct 400 status code
        - Response can be processed
        
        Expected: 400 status code returned
        """
        # Arrange & Act
        response = requests.get(f"{self.STATUS_ENDPOINT}/400")
        
        # Assert - Status Code
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    
    @pytest.mark.regression
    def test_error_status_code_401(self):
        """
        Test Case: Validate 401 Unauthorized response
        
        Validates:
        - API returns correct 401 status code (simulating invalid credentials)
        
        Expected: 401 status code returned
        """
        # Arrange & Act
        response = requests.get(f"{self.STATUS_ENDPOINT}/401")
        
        # Assert - Status Code
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"


class TestUserProfileAPI:
    """
    Test class for User Profile API-style endpoint validation.
    
    Demonstrates GET request testing for user data retrieval.
    """
    
    # API Configuration
    BASE_URL = "https://httpbin.org"
    GET_ENDPOINT = f"{BASE_URL}/get"
    STATUS_ENDPOINT = f"{BASE_URL}/status"
    
    @pytest.mark.smoke
    def test_get_user_profile_success(self):
        """
        Test Case: Simulate getting user profile successfully
        
        Validates:
        - HTTP status code is 200
        - Response contains expected structure
        
        Expected: User profile data returned successfully
        """
        # Arrange - Simulating user profile request with query params
        user_params = {"user_id": "123", "include": "profile"}
        
        # Act
        response = requests.get(self.GET_ENDPOINT, params=user_params)
        
        # Assert - Status Code
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Assert - Response Structure
        response_json = response.json()
        assert "args" in response_json, "Response should contain 'args' field"
        assert response_json["args"]["user_id"] == "123", "User ID should be in response"
    
    @pytest.mark.regression
    def test_get_nonexistent_resource(self):
        """
        Test Case: Simulate getting non-existent resource
        
        Validates:
        - HTTP status code is 404 for non-existent resource
        
        Expected: 404 Not Found error
        """
        # Arrange & Act
        response = requests.get(f"{self.STATUS_ENDPOINT}/404")
        
        # Assert - Status Code
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
