import secrets
import string
from canaryvault.models import HoneyToken

class AWSHoneytokenGenerator:
    @staticmethod
    def generate(webhook_base_url: str, description: str = "Production CloudWatch Decoy") -> HoneyToken:
        # AWS Access Key IDs start with AKIA followed by 16 uppercase alphanumeric chars
        alphabet = string.ascii_uppercase + string.digits
        key_id = "AKIA" + "".join(secrets.choice(alphabet) for _ in range(16))
        
        # Secret Access Key is 40 chars of base64 chars
        sec_alphabet = string.ascii_letters + string.digits + "+/"
        secret_key = "".join(secrets.choice(sec_alphabet) for _ in range(40))

        canary_url = f"{webhook_base_url.rstrip('/')}/v1/canary/aws/{key_id}"

        return HoneyToken(
            token_type="AWS_KEY",
            payload={
                "aws_access_key_id": key_id,
                "aws_secret_access_key": secret_key,
                "region": "us-east-1"
            },
            canary_url=canary_url,
            description=description
        )
