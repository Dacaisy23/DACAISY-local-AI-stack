# 🤖 CAISY Local AI Stack

An automated cloud security and self-healing engine loop that targets high-risk cloud misconfigurations with automated security gatekeeper patches.

### 📊 System Status & Production App Distribution
📡 [![Pipeline Status](https://github.com)](https://github.com) 💾 [![Download CAISY AI App v1.0.4](https://shields.io)](https://github.com)

---

## 🚀 Architectural Components
* **Unified Control Hub (`CAISY_AI.exe`)**: The primary text-based desktop control panel dashboard used to track status structures and launch core workflows with a single click.
* **Sandbox Mode (`CAISY.bat`)**: Dev Tier tool for on-demand manual testing environments, localized threat validation, and immediate on-device code patches.
* **Continuous Daemon Mode (`CAISY_AGENT.exe`)**: Enterprise Tier tool running as a persistent 24/7 background agent built with the `--noconsole` framework to execute invisible, automated hourly scanning loops.
* **Pipeline Integration (`caisy.yml`)**: Continuous automated security gate checking execution triggered instantly upon repository code modifications using GitHub Actions cloud sandboxes.


## 🔒 Private On-Premises Monitoring & Incident Response

This application executes 100% locally within a completely closed network structure. It features native, secure fallback handlers to capture severe stack runtime crashes.

### Automated Alerts Workflow
1. **Local Disk Mirroring**: Whenever an unhandled system exception drops, the system instantly logs data on-premises to `./security_alerts.log`. The file rotates automatically when it approaches 5MB to avoid storage overconsumption.
2. **CISO Enterprise Interface**: An automated email compiled with full stack trace context and a clean HTML structure is sent to your internal security operations contact line.

### System Initialization Guide

1. Find the `.env.example` boilerplate file in your application root workspace directory.
2. Generate a local running instance configuration block file matching your corporate layout:
   ```bash
   cp .env.example .env
   ```
3. Update the parameters located within your target `.env` file structure:
   * **SMTP_HOST**: Enter your primary corporate on-prem network internal exchange server address.
   * **SMTP_PORT**: Assign your mail communication port line (e.g., Use `25` standard or `587` with strict TLS routing).
   * **CISO_EMAIL**: Provide the local distribution mailbox target path intended for processing critical infrastructure notifications.

*Notice: This system uses a protective local filtering strategy. Standard operations logs (`INFO`/`DEBUG`) remain completely silent. Only severe operational failure states trigger high-priority distribution actions.*
