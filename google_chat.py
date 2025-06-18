import os
import requests
import html
from typing import Optional

class GoogleChatIntegration:
    """
    Basic integration for sending messages to Google Chat via webhook.
    All methods support request tracing with a request_id parameter.
    Inputs are validated and sanitized for security.
    Webhook URL is loaded from environment variables for secret management.
    
    (\_/)
    ( •_•)  <--- Bunny: Stay hoppy and secure!
    """

    def __init__(self, webhook_env_var: str = "GOOGLE_CHAT_WEBHOOK_URL"):
        """
        Initialize the GoogleChatIntegration with the webhook URL from environment variables.
        :param webhook_env_var: Name of the environment variable containing the webhook URL.
        (>'-')>  <--- Kirby: Ready to send messages!
        """
        self.webhook_url = os.getenv(webhook_env_var)
        if not self.webhook_url:
            raise ValueError("Google Chat webhook URL not set in environment variable: {}".format(webhook_env_var))

    def send_message(self, message: str, request_id: Optional[str] = None) -> bool:
        """
        Send a message to the Google Chat room via webhook.
        :param message: The message to send (will be sanitized).
        :param request_id: Optional request ID for tracing.
        :return: True if the message was sent successfully, False otherwise.
        (o_o)7  <--- Saluting face: Message sent with honor!
        """
        if not isinstance(message, str) or not message.strip():
            raise ValueError("Message must be a non-empty string.")
        sanitized_message = html.escape(message.strip())
        payload = {"text": sanitized_message}
        headers = {"Content-Type": "application/json"}
        if request_id:
            headers["X-Request-ID"] = request_id
        try:
            response = requests.post(self.webhook_url, json=payload, headers=headers, timeout=5)
            response.raise_for_status()
            return True
        except requests.RequestException:
            # Log error securely in production (no PII or secrets)
            return False
