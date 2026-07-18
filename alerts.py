import os
import sys
import traceback
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_ciso_critical_alert(error_message, traceback_details):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    ciso_email = os.getenv("CISO_EMAIL")
    environment = os.getenv("ENVIRONMENT", "production")

    if not smtp_host or not ciso_email:
        print("[ALERT SYSTEM ERROR] Local configuration missing. Cannot alert CISO.")
        return

    subject = f"[CRITICAL SECURITY ALERT] {environment.upper()} System Exception"
    
    body = f"""ATTENTION CISO / SECURITY OPERATIONS:
    
A critical unexpected exception has occurred within the local DACAISY stack instance.

--- ERROR DETAILS ---
Error Summary: {error_message}

--- STACK TRACE ---
{traceback_details}

---------------------
This is an automated local notification sent via your internal corporate mail system.
"""

    message = MIMEMultipart()
    message["From"] = "caisy-system@local.ai"
    message["To"] = ciso_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        port = int(smtp_port) if smtp_port else 25
        with smtplib.SMTP(smtp_host, port) as server:
            if port == 587:
                server.starttls()
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
                
            server.sendmail(message["From"], ciso_email, message.as_string())
        print(f"[SUCCESS] Security alert successfully pushed to local CISO: {ciso_email}")
    except Exception as smtp_error:
        print(f"[ALERT SYSTEM CRASH] Failed to route local mail via {smtp_host}: {smtp_error}")

def global_exception_handler(exctype, value, tb):
    traceback_details = "".join(traceback.format_exception(exctype, value, tb))
    error_message = str(value)
    sys.__excepthook__(exctype, value, tb)
    send_ciso_critical_alert(error_message, traceback_details)

sys.excepthook = global_exception_handler

if __name__ == "__main__":
    print("Application running. Simulating a critical runtime failure...")
    raise RuntimeError("Unauthorized access detected on database configuration node.")
