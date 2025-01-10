import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class MailSender:
    """
    A class to send emails using the SendGrid API.
    """

    def __init__(self):
        """
        Initializes the MailSender instance by fetching the API key from environment variables.
        """
        # Fetch the SendGrid API key
        self.api_key = os.getenv("SENDGRID_API_KEY")
        if not self.api_key:
            raise ValueError("SendGrid API key is missing! Ensure it is set in the environment variables.")

        # Initialize the SendGrid client
        self.client = SendGridAPIClient(self.api_key)

    def send_email(self, from_email, to_email, subject, content):
        """
        Sends an email using SendGrid API.

        Args:
            from_email (str): Sender's email address.
            to_email (str): Recipient's email address.
            subject (str): Subject of the email.
            content (str): Email body content (plain text or HTML).

        Returns:
            dict: The response status code and body from the SendGrid API.
        """
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            html_content=content
        )
        try:
            response = self.client.send(message)
            return {
                "status_code": response.status_code,
                "body": response.body.decode() if response.body else None
            }
        except Exception as e:
            raise RuntimeError(f"Failed to send email: {str(e)}") from e