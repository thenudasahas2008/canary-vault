import pytest
from canaryvault.generators.aws_token import AWSHoneytokenGenerator
from canaryvault.generators.db_token import DBHoneytokenGenerator
from canaryvault.generators.document_watermark import DocumentWatermarker
from canaryvault.dispatcher import CanaryAlertDispatcher

def test_aws_honeytoken_generation():
    token = AWSHoneytokenGenerator.generate("https://alerts.test.local")
    assert token.token_type == "AWS_KEY"
    assert token.payload["aws_access_key_id"].startswith("AKIA")
    assert len(token.payload["aws_access_key_id"]) == 20
    assert len(token.payload["aws_secret_access_key"]) == 40
    assert "alerts.test.local" in token.canary_url

def test_db_honeytoken_generation():
    token = DBHoneytokenGenerator.generate("https://alerts.test.local", db_type="postgres")
    assert token.token_type == "DB_CREDENTIAL"
    assert "postgresql://" in token.payload["connection_string"]

def test_document_watermarking_roundtrip():
    marker = "CONFID-987"
    encoded = DocumentWatermarker.encode_binary_marker(marker)
    decoded = DocumentWatermarker.decode_binary_marker(encoded)
    assert decoded == marker

def test_canary_alert_dispatch():
    token = AWSHoneytokenGenerator.generate("https://alerts.test.local")
    alert = CanaryAlertDispatcher.process_trigger(
        token,
        source_ip="198.51.100.42",
        user_agent="aws-cli/2.15.0"
    )
    assert token.triggered is True
    assert alert.source_ip == "198.51.100.42"
    assert alert.severity == "CRITICAL"
