import smtplib
from email.mime.text import MIMEText
from app.core.config import settings


def send_reset_email(to_email: str, token: str):
    msg = MIMEText(f"Your reset token link is: {token}")
    msg["Subject"] = "Reset Your Password"
    msg["From"] = settings.EMAIL_USER
    msg["To"] = to_email

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_USER, settings.EMAIL_PASS)
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())
