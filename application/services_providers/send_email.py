# application/services/send_email.py
import os
from pathlib import Path
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from data.email_addresses import EMAIL_ADDRESSES

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

TEMPLATE_PATH = Path(__file__).resolve(
).parents[1] / "templates" / "email_template.html"


def send_email(subject: str = "Test Email from Job Explorer", html_body: str | None = None) -> None:
    """Send a simple HTML email to all recipients in EMAIL_ADDRESSES."""
    if not SENDGRID_API_KEY or not FROM_EMAIL:
        print("❌ Missing SENDGRID_API_KEY or FROM_EMAIL in .env")
        return

    # Use provided HTML body or fall back to template file
    if html_body:
        html_content = html_body
    else:
        try:
            html_content = TEMPLATE_PATH.read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"❌ Email template not found at: {TEMPLATE_PATH}")
            return

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=EMAIL_ADDRESSES,
        subject=subject,
        html_content=html_content,
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ Email sent! Status code: {response.status_code}")
    except Exception as e:
        print("❌ Error sending email:", e)
