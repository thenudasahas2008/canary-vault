import argparse
import json
import sys
from canaryvault.generators.aws_token import AWSHoneytokenGenerator
from canaryvault.generators.db_token import DBHoneytokenGenerator
from canaryvault.generators.document_watermark import DocumentWatermarker

def main():
    parser = argparse.ArgumentParser(
        description="CanaryVault — Active Cyber Deception & Honeytoken Generation Engine"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # AWS command
    aws_parser = subparsers.add_parser("aws", help="Generate decoy AWS credentials")
    aws_parser.add_argument("--webhook", default="https://alerts.canaryvault.internal", help="Webhook reporting endpoint")
    aws_parser.add_argument("--desc", default="Decoy AWS IAM credential in repo", help="Token description")

    # DB command
    db_parser = subparsers.add_parser("db", help="Generate decoy database credentials")
    db_parser.add_argument("--webhook", default="https://alerts.canaryvault.internal", help="Webhook reporting endpoint")
    db_parser.add_argument("--type", default="postgres", choices=["postgres", "mysql", "mongodb"], help="Database flavor")
    db_parser.add_argument("--desc", default="Decoy database connection string", help="Token description")

    # Watermark command
    doc_parser = subparsers.add_parser("watermark", help="Generate zero-width steganographic document watermark")
    doc_parser.add_argument("--webhook", default="https://alerts.canaryvault.internal", help="Webhook reporting endpoint")

    args = parser.parse_args()

    print("=" * 65)
    print("CANARYVAULT // CYBER DECEPTION PLATFORM")
    print("=" * 65)

    if args.command == "aws":
        token = AWSHoneytokenGenerator.generate(args.webhook, args.desc)
        print(f"[+] Generated AWS Decoy Honeytoken (ID: {token.id})")
        print(f"  AWS_ACCESS_KEY_ID:     {token.payload['aws_access_key_id']}")
        print(f"  AWS_SECRET_ACCESS_KEY: {token.payload['aws_secret_access_key']}")
        print(f"  Monitoring Webhook:    {token.canary_url}")

    elif args.command == "db":
        token = DBHoneytokenGenerator.generate(args.webhook, args.type, args.desc)
        print(f"[+] Generated Database Decoy Honeytoken (ID: {token.id})")
        print(f"  Connection String: {token.payload['connection_string']}")
        print(f"  Monitoring Webhook: {token.canary_url}")

    elif args.command == "watermark":
        token = DocumentWatermarker.generate(args.webhook)
        print(f"[+] Generated Steganographic Document Watermark (ID: {token.id})")
        print(f"  Watermark Payload ID: {token.payload['marker_id']}")
        print(f"  Monitoring Webhook:   {token.canary_url}")

    print("=" * 65)

if __name__ == "__main__":
    main()
