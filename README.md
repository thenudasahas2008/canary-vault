# CanaryVault

Active cyber deception and honeytoken deployment engine.

## Features
- Generates realistic canary AWS credentials (`AKIA...`) linked to tracking webhooks.
- Generates decoy database strings and credentials.
- Injects zero-width unicode steganographic watermarks into sensitive documents.
- Real-time intrusion alert dispatcher with source IP and user agent capture.

## Usage
```bash
pip install -e .
canary-vault aws --webhook https://your-webhook-host.com
canary-vault db --type postgres --webhook https://your-webhook-host.com
canary-vault watermark --webhook https://your-webhook-host.com
```
