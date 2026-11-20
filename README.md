# CanaryVault — Active Cyber Deception & Honeytoken Deployment Toolkit

[![Deception: Honeytoken](https://img.shields.io/badge/Security-Cyber%20Deception-purple.svg)](#)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)

CanaryVault is an active cyber deception framework engineered to plant decoy credentials, fake configuration files, and tracking tokens across enterprise networks, repositories, and cloud workloads to entrap intruders.

---

## Core Deception Modules

1. **AWS Decoy Credentials**:
   - Generates realistic AWS Access Key IDs (`AKIA...`) and 40-character secret keys.
   - Bound to an intrusion telemetry webhook to catch attackers attempting unauthorized AWS API calls.
2. **Database Decoy Credentials**:
   - Synthesizes realistic PostgreSQL, MySQL, and MongoDB connection strings.
   - Routes connection probes to canary monitoring endpoints.
3. **Steganographic Document Watermarks**:
   - Injects zero-width invisible Unicode characters into sensitive text and markdown files.
   - Traces leaked insider documents back to the exact source without altering visible document text.
4. **Intrusion Dispatcher**:
   - Real-time event capture logging source IP, timestamp, and User-Agent telemetry with `CRITICAL` severity escalation.

---

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/thenudasahas2008/canary-vault.git
cd canary-vault

# Install dependencies and local CLI
pip install -e .
```

---

## CLI Usage

### 1. Generate Fake AWS Credentials
```bash
canary-vault aws --webhook https://alerts.your-canary-domain.com --desc "Production AWS Root Key"
```

### 2. Generate Decoy Database Credentials
```bash
canary-vault db --type postgres --webhook https://alerts.your-canary-domain.com
```

### 3. Generate Steganographic Document Watermark
```bash
canary-vault watermark --webhook https://alerts.your-canary-domain.com
```

---

## Automated Verification & Testing

```bash
# Run pytest verification suite (4 test cases)
pytest -v tests
```

---

## Repository Structure

```
canary-vault/
├── canaryvault/
│   ├── generators/
│   │   ├── aws_token.py          # Realistic AWS IAM honeytoken generator
│   │   ├── db_token.py           # Decoy database credentials generator
│   │   └── document_watermark.py # Zero-width unicode document watermarking
│   ├── dispatcher.py             # Intrusion alert dispatcher and telemetry handler
│   ├── models.py                 # Pydantic schemas for tokens and alerts
│   └── cli.py                    # Command-line interface
└── tests/                        # Pytest test cases
```
