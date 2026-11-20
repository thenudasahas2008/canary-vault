from typing import Optional
from canaryvault.models import CanaryAlert, HoneyToken
from datetime import datetime, timezone

class CanaryAlertDispatcher:
    @staticmethod
    def process_trigger(token: HoneyToken, source_ip: str, user_agent: str) -> CanaryAlert:
        token.triggered = True
        token.last_triggered_at = datetime.now(timezone.utc).isoformat()
        
        return CanaryAlert(
            token_id=token.id,
            token_type=token.token_type,
            source_ip=source_ip,
            user_agent=user_agent,
            severity="CRITICAL"
        )
