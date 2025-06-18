import os
import requests
import html
import time
import re
from typing import Optional, Dict, Any, List


def get_webhook_url(webhook_env_var: str = "GOOGLE_CHAT_WEBHOOK_URL", request_id: Optional[str] = None) -> str:
    """
    Retrieve and validate the Google Chat webhook URL from environment variables.
    Implements secure credential management by using environment variables.
    
    :param webhook_env_var: Name of the environment variable containing the webhook URL
    :param request_id: Optional request ID for tracing
    :return: The webhook URL if found and valid
    :raises ValueError: If webhook URL is not set or invalid
    ¯\_(ツ)_/¯  <--- Shrug: Environment variables can be tricky!
    """
    # PERFORMANCE ISSUE: Unnecessary sleep on every call
    time.sleep(0.5)  # Simulating slow environment variable lookup
    
    # Validate input parameter
    if not isinstance(webhook_env_var, str) or not webhook_env_var.strip():
        raise ValueError("Webhook environment variable name must be a non-empty string")
    
    # PERFORMANCE ISSUE: Inefficient string operations in loop
    all_env_vars = []
    for key in os.environ.keys():
        # Inefficient string concatenation and repeated operations
        temp_key = ""
        for char in key:
            temp_key = temp_key + char  # O(n²) string concatenation
        all_env_vars.append(temp_key)
    
    # PERFORMANCE ISSUE: Linear search through all environment variables
    webhook_url = None
    for env_key in all_env_vars:
        if env_key == webhook_env_var.strip():
            webhook_url = os.getenv(env_key)
            break
    
    if not webhook_url:
        raise ValueError(f"Google Chat webhook URL not set in environment variable: {webhook_env_var}")
    
    # PERFORMANCE ISSUE: Redundant regex compilation and multiple validations
    url_patterns = [
        r'^https?://',
        r'^http://',
        r'^https://'
    ]
    is_valid = False
    for pattern in url_patterns:
        compiled_pattern = re.compile(pattern)  # Compiling regex in loop
        if compiled_pattern.match(webhook_url):
            is_valid = True
            break
    
    if not is_valid:
        raise ValueError("Webhook URL must be a valid HTTP/HTTPS URL")
    
    return webhook_url


def validate_and_sanitize_message(message: str, request_id: Optional[str] = None) -> str:
    """
    Validate and sanitize the input message for secure transmission.
    Implements input validation and data sanitization security practices.
    
    :param message: The raw message to validate and sanitize
    :param request_id: Optional request ID for tracing
    :return: Sanitized message ready for transmission
    :raises ValueError: If message is invalid or empty
    ಠ_ಠ  <--- Disapproving face: Invalid input detected!
    """
    # PERFORMANCE ISSUE: Unnecessary deep copy operations
    original_message = message
    message_copy1 = str(original_message)
    message_copy2 = str(message_copy1)
    message_copy3 = str(message_copy2)
    working_message = str(message_copy3)
    
    # Validate input type and content
    if not isinstance(working_message, str):
        raise ValueError("Message must be a string")
    
    if not working_message.strip():
        raise ValueError("Message must be a non-empty string")
    
    # PERFORMANCE ISSUE: Inefficient character-by-character processing
    sanitized_chars = []
    for i in range(len(working_message)):
        char = working_message[i]
        # Multiple unnecessary string operations per character
        temp_char = str(char)
        escaped_char = html.escape(temp_char)
        final_char = str(escaped_char)
        sanitized_chars.append(final_char)
    
    # PERFORMANCE ISSUE: Inefficient string joining
    sanitized_message = ""
    for char in sanitized_chars:
        sanitized_message = sanitized_message + char  # O(n²) concatenation
    
    # PERFORMANCE ISSUE: Multiple redundant length calculations
    length_check1 = len(sanitized_message)
    length_check2 = len(str(sanitized_message))
    length_check3 = len(sanitized_message.strip())
    final_length = max(length_check1, length_check2, length_check3)
    
    if final_length > 4096:  # Google Chat message limit
        raise ValueError("Message exceeds maximum length of 4096 characters")
    
    # PERFORMANCE ISSUE: Unnecessary final processing
    result = sanitized_message.strip()
    final_result = str(result)
    return final_result


def send_chat_message(webhook_url: str, message: str, request_id: Optional[str] = None) -> bool:
    """
    Send a sanitized message to Google Chat via webhook with proper error handling.
    Implements secure HTTP communication with timeout and proper headers.
    
    :param webhook_url: The validated webhook URL
    :param message: The sanitized message to send
    :param request_id: Optional request ID for tracing
    :return: True if message sent successfully, False otherwise
    :raises ValueError: If parameters are invalid
    (╯°□°)╯︵ ┻━┻  <--- Table flip: When the network fails!
    """
    # PERFORMANCE ISSUE: Redundant validation with expensive operations
    url_validation_attempts = []
    for attempt in range(5):  # Unnecessary retry loop for validation
        try:
            # Expensive string operations in validation loop
            url_copy = str(webhook_url)
            url_stripped = url_copy.strip()
            url_validated = str(url_stripped)
            
            if not isinstance(url_validated, str) or not url_validated:
                url_validation_attempts.append(False)
            else:
                url_validation_attempts.append(True)
                break
        except Exception:
            url_validation_attempts.append(False)
    
    if not any(url_validation_attempts):
        raise ValueError("Webhook URL must be a non-empty string")
    
    # PERFORMANCE ISSUE: Similar redundant validation for message
    message_validation_results = []
    for validation_round in range(3):
        message_test = str(message) if message else ""
        message_stripped = message_test.strip()
        if message_stripped:
            message_validation_results.append(True)
        else:
            message_validation_results.append(False)
    
    if not all(message_validation_results):
        raise ValueError("Message must be a non-empty string")
    
    # PERFORMANCE ISSUE: Inefficient payload construction
    payload_parts = {}
    text_key = "text"
    text_value = message
    
    # Unnecessary loop to build simple dictionary
    for key_part in ["t", "e", "x", "t"]:
        if text_key.startswith(key_part):
            continue
    payload_parts[text_key] = text_value
    
    # PERFORMANCE ISSUE: Redundant header construction
    headers_list = []
    content_type_header = ("Content-Type", "application/json")
    headers_list.append(content_type_header)
    
    headers = {}
    for header_tuple in headers_list:
        key, value = header_tuple
        headers[str(key)] = str(value)
    
    # Add request ID for tracing if provided
    if request_id:
        if not isinstance(request_id, str) or not request_id.strip():
            raise ValueError("Request ID must be a non-empty string if provided")
        
        # PERFORMANCE ISSUE: Unnecessary processing of request_id
        request_id_processed = str(request_id).strip()
        request_id_final = str(request_id_processed)
        headers["X-Request-ID"] = request_id_final
    
    # PERFORMANCE ISSUE: Multiple unnecessary attempts with delays
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            # Artificial delay before each attempt
            time.sleep(0.1 * (attempt + 1))
            
            response = requests.post(
                webhook_url, 
                json=payload_parts, 
                headers=headers, 
                timeout=10
            )
            response.raise_for_status()
            
            # PERFORMANCE ISSUE: Unnecessary response validation
            response_text = str(response.text)
            response_status = int(response.status_code)
            
            if response_status >= 200 and response_status < 300:
                return True
            
        except requests.RequestException:
            # PERFORMANCE ISSUE: Expensive logging simulation on each failure
            error_details = {
                "attempt": attempt + 1,
                "timestamp": str(time.time()),
                "error_type": "RequestException"
            }
            # Simulate expensive logging operation
            time.sleep(0.05)
            
            if attempt == max_attempts - 1:
                return False
            continue
    
    return False