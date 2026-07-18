import os
import sys
import traceback
import smtplib
import logging
from logging.handlers import RotatingFileHandler
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

# --- STEP 1: CONFIGURE LOCAL FILE LOGGING ---
log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log_file = "security_alerts.log"

file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3, encoding="utf-8")
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.ERROR)

logger = logging.getLogger("DACAISY_Local_Monitor")
logger.setLevel(logging.ERROR)
logger.addHandler(file_handler)


# --- STEP 2: CONFIGURE SECURE HTML EMAIL SYSTEM ---
def send_ciso_critical_alert(error_message, traceback_details):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    ciso_email = os.getenv("CISO_EMAIL")
    environment = os.getenv("ENVIRONMENT", "production")

    if not smtp_host or not ciso_email:
        logger.error(f"Local SMTP or CISO Email configuration missing. Alert could not be sent over network. Error: {error_message}")
        print("[ALERT SYSTEM ERROR] Configuration missing. Logged to local security_alerts.log file.")
        return

    subject = f"[CRITICAL SECURITY ALERT] {environment.upper()} System Exception"
    
    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333333; margin: 0; padding: 20px;">
        <div style="max-width: 650px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 4px; overflow: hidden;">
            <div style="background-color: #d9534f; color: #ffffff; padding: 15px 20px; font-size: 18px; font-weight: bold;">
                ⚠️ CRITICAL SECURITY INCIDENT DETECTED
            </div>
            <div style="padding: 20px; background-color: #ffffff;">
                <p style="margin-top: 0;"><strong>Attention CISO / Security Operations Team,</strong></p>
                <p>An unexpected runtime exception has caused a crash within your local <strong>DACAISY AI Stack</strong> instance.</p>
                
                <table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                    <tr>
                        <td style="padding: 8px; border-bottom: 1px solid #eeeeee; font-weight: bold; width: 30%;">Environment:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #eeeeee; color: #d9534f; font-weight: bold;">{environment.upper()}</td>
                    </tr>
                    <tr>
                        <td style="padding: 8px; border-bottom: 1px solid #eeeeee; font-weight: bold;">Error Summary:</td>
                        <td style="padding: 8px; border-bottom: 1px solid #eeeeee; font-style: italic;">{error_message}</td>
                    </tr>
                </table>
                
                <p style="font-weight: bold; margin-bottom: 5px;">Technical Stack Trace:</p>
                <pre style="background-color: #f8f9fa; border: 1px solid #e1e4e8; padding: 12px; border-radius: 4px; font-family: Consolas, Monaco, monospace; font-size: 12px; overflow-x: auto; white-space: pre-wrap;">{traceback_details}</pre>
                
                <p style="font-size: 11px; color: #777777; margin-top: 25px; border-top: 1px solid #eeeeee; padding-top: 10px;">
                    This is an automated local transmission routed exclusively through your internal corporate mail systems. Zero data has left your closed private cloud perimeter.
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    message = MIMEMultipart("alternative")
    message["From"] = "CAISY-AI-SYSTEM@caisy.local"
    message["To"] = ciso_email
    message["Subject"] = subject
    message.attach(MIMEText(html_body, "html"))

    try:
        port = int(smtp_port) if smtp_port else 25
        with smtplib.SMTP(smtp_host, port) as server:
            if port == 587:
                server.starttls()
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
                
            server.sendmail(message["From"], ciso_email, message.as_string())
        print(f"[SUCCESS] High-priority security report routed to local CISO: {ciso_email}")
    except Exception as smtp_error:
        logger.error(f"Failed to route secure email via local server {smtp_host}. Error: {smtp_error}. Original App Failure: {error_message}")
        print(f"[ALERT SYSTEM CRASH] Internal mail routing failed. Error backed up safely to security_alerts.log.")

def global_exception_handler(exctype, value, tb):
    traceback_details = "".join(traceback.format_exception(exctype, value, tb))
    error_message = str(value)
    logger.error(f"Application Unhandled Exception: {error_message}\n{traceback_details}")
    send_ciso_critical_alert(error_message, traceback_details)
    sys.__excepthook__(exctype, value, tb)

sys.excepthook = global_exception_handler

if __name__ == "__main__":
    print("Application executing active tasks. Inducing systemic test failure...")
    raise RuntimeError("Unauthorized access detected on database configuration node.")
