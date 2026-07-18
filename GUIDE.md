# 📘 CAISY AI • Enterprise Integration & User Guide

This official documentation outlines the architecture, deployment models, and security governance for the **CAISY AI Local Security Stack**. Engineered for highly regulated sectors (Banking, Healthcare, Biopharma, and Insurance), this platform operates **100% offline and localized**, ensuring complete regulatory compliance without third-party data exposure.

---

### 🎛️ 1. Navigating the Unified Control Hub (`CAISY_AI.exe`)

The central desktop application dashboard serves as your unified command center:
* **`CAISY_ENGINE.SH` (Core Engine)**: Displays real-time local verification status. It shows a permanent green status reading `ACTIVE & SECURE (OFFLINE)` to confirm the localized AI rules are active.
* **`CAISY.bat` (Dev Tier Button)**: Launches an interactive terminal console for manual, on-demand code audits.
* **`CAISY_AGENT.exe` (Enterprise Tier Button)**: Instantly initializes the silent, 24/7 background guard loop.

---

### 🔑 2. Activating Your Proprietary License

The application suite is structurally license-gated to protect intellectual property:
1. Locate your unique activation string provided directly by the Architecture Owner.
2. Create a plain text file named exactly **`license.key`**.
3. Paste your specific enterprise activation string inside the file and save it.
4. Place the **`license.key`** file inside the application directory right next to the executable files.

*Note: If the key file is missing, altered, or unauthorized, the software will drop its execution loop and shut down instantly.*

---

### 🛠️ 3. Operational Modes & Deployment Models

#### Tier 1: On-Demand Developer Sandbox (`CAISY.bat`)
Built for developers and security engineers to vet infrastructure templates *before* code commitments.
* **How it works**: Triggered via the UI Dashboard or local terminal. It scans local infrastructure-as-code files (e.g., `main.tf`), identifies security anomalies (such as unencrypted data blocks), and uses the local AI engine to suggest or execute immediate self-healing patches natively on the workstation.

#### Tier 2: 24/7 Server Daemon Deployment (`CAISY_AGENT.exe`)
Built for persistent monitoring on internal corporate staging servers or secure configuration management nodes.
* **How to deploy**: Copy the application bundle onto your central, private server host. Configure the `.exe` binary to run as a persistent background daemon via Windows Task Scheduler or as a native background service.
* **Automation**: The agent runs completely invisibly in the background. Every hour, it automatically awakens, runs an architectural configuration scan, applies any necessary remediation patches, and goes back to sleep without human interaction.

#### Tier 3: Automated CI/CD Pipeline Gatekeeper (`caisy.yml`)
Built to integrate seamlessly into modern corporate delivery pipelines (Jenkins, GitHub Actions, GitLab CI, or Azure DevOps).
* **The Process**: The exact millisecond a developer pushes a code update, the pipeline runner pulls the secure binary.
* **The Gate**: The agent parses the incoming code changes before deployment. If the code is clean, the pipeline proceeds to production. If high-risk vulnerabilities are found, the agent flags the threat, breaks the pipeline execution automatically, and prevents the exploit from going live.

---

### 🔒 4. Compliance & Air-Gapped Isolation

Because **CAISY AI** uses purely localized model parsing, it requires **zero internet access** and completely isolates data tracking loops. It fully complies with strict compliance parameters:
* **No Cloud Overhead**: Zero telemetry data, source code, or infrastructure maps leave your perimeter.
* **Regulatory Alignment**: Fully compatible with strict air-gapped network configurations required by HIPAA, PCI-DSS, and GDPR frameworks.

---
**Architecture Owner & Lead Engineer:** `TONMEU CAISY`  
**Latest Distribution Stable Release:** `v1.0.3`
