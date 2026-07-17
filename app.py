import customtkinter as ctk
import subprocess
import os

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CAISY AI Security Stack Hub")
app.geometry("600x520")

header_frame = ctk.CTkFrame(app, fg_color="transparent")
header_frame.pack(pady=20)

title_text = ctk.CTkLabel(header_frame, text="CAISY AI", font=("Helvetica", 26, "bold"), text_color="#1f77b4")
title_text.pack()

engine_frame = ctk.CTkFrame(app, height=75, width=500, fg_color="#1a1a1a", border_width=1, border_color="#333333")
engine_frame.pack(pady=15, padx=40, fill="x")
engine_frame.pack_propagate(False)

engine_title = ctk.CTkLabel(engine_frame, text="CAISY_ENGINE.SH", font=("Helvetica", 14, "bold"), text_color="#1f77b4")
engine_title.pack(anchor="w", padx=20, pady=(10, 2))

engine_text = ctk.CTkLabel(engine_frame, text="Local Engine Core Status: ACTIVE & SECURE (OFFLINE)", font=("Helvetica", 12), text_color="green")
engine_text.pack(anchor="w", padx=20)

def run_sandbox():
    status_label.configure(text="⚡ Executing Interactive On-Demand Scan...", text_color="#1f77b4")
    subprocess.Popen(["cmd.exe", "/c", "CAISY.bat"], creationflags=subprocess.CREATE_NEW_CONSOLE)

bat_frame = ctk.CTkFrame(app, fg_color="transparent")
bat_frame.pack(pady=15, padx=40, fill="x")

btn_bat = ctk.CTkButton(
    bat_frame, 
    text="CAISY.bat\nDev Tier for instant local fixes", 
    command=run_sandbox, 
    font=("Helvetica", 14, "bold"), 
    height=70, 
    fg_color="#242424", 
    hover_color="#333333", 
    border_width=1, 
    border_color="#1f77b4"
)
btn_bat.pack(fill="x")

def run_daemon():
    if not os.path.exists("license.key"):
        status_label.configure(text="❌ Error: Activation failed. 'license.key' is missing!", text_color="red")
        return
    status_label.configure(text="✅ 24/7 Persistent Monitoring Active (Running in Details tab)", text_color="green")
    subprocess.Popen(["./CAISY_AGENT.exe"])

agent_frame = ctk.CTkFrame(app, fg_color="transparent")
agent_frame.pack(pady=15, padx=40, fill="x")

btn_agent = ctk.CTkButton(
    agent_frame, 
    text="CAISY_AGENT.exe\nEnterprise Tier for CI/CD", 
    command=run_daemon, 
    font=("Helvetica", 14, "bold"), 
    height=70, 
    fg_color="#242424", 
    hover_color="#333333", 
    border_width=1, 
    border_color="#9437ff"
)
btn_agent.pack(fill="x")

status_label = ctk.CTkLabel(app, text="📡 Standby Loop Awaiting Input", font=("Helvetica", 12, "italic"), text_color="gray")
status_label.pack(side="bottom", pady=25)

app.mainloop()
