# CAISY: Cloud AI Security & Automated Remediation Loop (IaC)

An agentic, automated DevSecOps self-healing pipeline built to enforce zero-trust security postures on Infrastructure as Code (IaC) architectures. This engine programmatically targets, parses, and patches severe infrastructure misconfigurations (such as leaky or public object storage buckets) to block data exfiltration vectors before live deployment.

## 🛠️ System Architecture & Stack

- **Infrastructure Layer:** HashiCorp Terraform (HCL) blueprints defining scalable cloud asset topologies.
- **Remediation Logic Engine:** Native POSIX Shell / Bash parsing matrices executing ultra-lightweight stream editing scripts (`sed`).
- **Local AI Controller:** Offline, secure Large Language Model integration utilizing **Ollama (`qwen2.5-coder:0.5b`)** to cross-evaluate configurations locally.
- **Zero-Footprint Paradigm:** Configured entirely to decouple backend runtimes from host systems, utilizing external storage vectors (`E:\`) to simulate sandbox orchestration environments.

---

## 🔒 The Security Vulnerability Solved

In cloud native engineering, public object storage buckets remain a primary threat vector for corporate data breaches. This project targets a critically misconfigured AWS S3 Public Access Block architecture where strict access controls are deactivated:

```hcl
# VULNERABLE SOURCE STATE (Detected by Engine)
resource "aws_s3_bucket_public_access_block" "caisy_security" {
  block_public_acls       = false  # CRITICAL VULNERABILITY
  block_public_policy     = false  # CRITICAL VULNERABILITY
  ignore_public_acls      = false  # CRITICAL VULNERABILITY
  restrict_public_buckets = false  # CRITICAL VULNERABILITY
}
```

---

## ⚡ Self-Healing Execution Flow

When executed, the `caisy_engine.sh` controller acts as an automated security gatekeeper by looping through the following phases:

1. **[1/3] Reading Assets:** Scans the target workspace environment for Infrastructure as Code files (`main.tf`).
2. **[2/3] Static Threat Analysis:** Programmatically maps structural logic flaws against strict organizational access governance matrices.
3. **[3/3] Dynamic Patch Compilation:** Re-writes the physical abstraction layers in real-time, instantly converting exposed configurations into hardened public access blocks (`= true`).

### 🟢 Remediated Compliant Output:
```hcl
resource "aws_s3_bucket_public_access_block" "caisy_security" {
  bucket = aws_s3_bucket.caisy_bucket.id

  block_public_acls       = true  # SECURED BY CAISY ENGINE
  block_public_policy     = true  # SECURED BY CAISY ENGINE
  ignore_public_acls      = true  # SECURED BY CAISY ENGINE
  restrict_public_buckets = true  # SECURED BY CAISY ENGINE
}
```

---

## 🚀 How to Run Locally (Lightweight Sandbox Mode)

Execute the entire automated scanning and self-healing loop instantly inside a **Git Bash** terminal interface:

```bash
# Clone the repository
git clone https://github.com
cd CAISY-local-AI-stack

# Trigger the automated self-healing cloud security gatekeeper
bash caisy_engine.sh
```

---

## 💼 DevSecOps Professional Highlights

- **Shift-Left Security Gatekeeping:** Emulates production-grade automated deployment pipelines (CI/CD) by intercepting infrastructure flaws before cloud execution.
- **Air-Gapped Compliance Ready:** Built specifically to support highly regulated industries (defense, banking, healthcare) where code privacy mandates prohibit routing proprietary assets to external third-party APIs.
- **Dynamic Policy Enforcement:** Leverages programmatic token replacement concepts to rapidly secure assets without interrupting deployment runtimes.
