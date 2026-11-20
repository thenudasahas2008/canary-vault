import secrets
import string
from canaryvault.models import HoneyToken

class DBHoneytokenGenerator:
    @staticmethod
    def generate(webhook_base_url: str, db_type: str = "postgresql", description: str = "Decoy DB Credential") -> HoneyToken:
        token_id = secrets.token_hex(8)
        password = secrets.token_urlsafe(18)
        host = f"canary-db-{token_id}.internal-metrics.net"
        username = "sec_svc_admin"
        
        prefix = "postgresql" if db_type in ("postgres", "postgresql") else db_type
        canary_url = f"{webhook_base_url.rstrip('/')}/v1/canary/db/{token_id}"
        conn_str = f"{prefix}://{username}:{password}@{host}:5432/finance_prod"

        return HoneyToken(
            token_type="DB_CREDENTIAL",
            payload={
                "db_type": db_type,
                "username": username,
                "password": password,
                "host": host,
                "connection_string": conn_str
            },
            canary_url=canary_url,
            description=description
        )
