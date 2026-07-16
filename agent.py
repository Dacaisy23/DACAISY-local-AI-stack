import time
import os
import subprocess
from datetime import datetime

def scan_all_repos():
    try:
        subprocess.run(
            ["bash.exe", "-c", "./CAISY.bat"], 
            capture_output=True, 
            text=True, 
            shell=True
        )
    except Exception:
        pass

def send_report_to_slack():
    pass

def check_license():
    license_file = "license.key"
    
    # Check if the external license file exists in the directory
    if not os.path.exists(license_file):
        print(f"❌ Critical Error: '{license_file}' missing from application directory.")
        return False
        
    try:
        # Read the key securely
        with open(license_file, "r") as f:
            user_key = f.read().strip()
            
        # Validate against your custom proprietary string
        if user_key == "CAISY-DEMO-2026":
            return True
        else:
            print("❌ Critical Error: Invalid license key signature detected.")
            return False
    except Exception as e:
        print(f"❌ Critical Error reading license file: {e}")
        return False

if __name__ == "__main__":
    if not check_license():
        # Exit immediately if validation fails
        time.sleep(3) 
        exit(1)
        
    while True:
        try:
            scan_all_repos()
            send_report_to_slack()
        except Exception:
            pass
        time.sleep(3600)  
