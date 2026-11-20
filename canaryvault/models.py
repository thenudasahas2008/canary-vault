from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone
import uuid

class HoneyToken(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    token_type: str  # "AWS_KEY", "DB_CREDENTIAL", "DOC_WATERMARK"
    payload: Dict[str, Any]
    canary_url: str
    description: str
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    triggered: bool = False
    last_triggered_at: Optional[str] = None

class CanaryAlert(BaseModel):
    alert_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    token_id: str
    token_type: str
    source_ip: str
    user_agent: str
    detected_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    severity: str = "CRITICAL"
