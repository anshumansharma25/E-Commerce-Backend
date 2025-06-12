import smtplib
from email.mime.text import MIMEText


def send_reset_email(to_email: str, token: str):
    msg = MIMEText(f"Your reset token link is: {token}")
    msg["Subject"] = "Reset Your Password"
    msg["From"] = "your_email@example.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("anshuman25sharma@gmail.com", "jpvirzyajdggapyw")
        server.sendmail(msg["From"], [msg["To"]], msg.as_string())
