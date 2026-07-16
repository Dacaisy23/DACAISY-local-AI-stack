import time
import os
from datetime import datetime

def scan_all_repos():
    # your existing scan logic here
    print(f"[{datetime.now()}] Running CAISY scan...")

def send_report_to_slack():
    # your existing slack/webhook logic here
    print("Report sent")

def check_license():
    # read license.key and validate
    return True

if __name__ == "__main__":
    if not check_license():
        print("Invalid license. Exiting.")
        exit(1)
        
    print("CAISY AGENT started in daemon mode")
    
    while True:
        try:
            scan_all_repos()
            send_report_to_slack()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(3600)  # wait for 1 hour before next scan
