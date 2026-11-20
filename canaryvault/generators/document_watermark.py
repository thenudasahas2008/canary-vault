import uuid
from canaryvault.models import HoneyToken

ZERO_WIDTH_SPACE = "\u200B"
ZERO_WIDTH_NON_JOINER = "\u200C"

class DocumentWatermarker:
    @staticmethod
    def encode_binary_marker(guid: str) -> str:
        # Encode UUID hex into zero-width steganographic sequence
        binary_str = "".join(format(ord(c), "08b") for c in guid)
        return "".join(ZERO_WIDTH_SPACE if b == "1" else ZERO_WIDTH_NON_JOINER for b in binary_str)

    @staticmethod
    def decode_binary_marker(text: str) -> str:
        zw_chars = [c for c in text if c in (ZERO_WIDTH_SPACE, ZERO_WIDTH_NON_JOINER)]
        if not zw_chars or len(zw_chars) % 8 != 0:
            return ""
        
        bits = "".join("1" if c == ZERO_WIDTH_SPACE else "0" for c in zw_chars)
        chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
        return "".join(chars)

    @classmethod
    def generate(cls, webhook_base_url: str, description: str = "Confidential Strategy Doc Watermark") -> HoneyToken:
        marker_id = str(uuid.uuid4())[:12]
        watermark_seq = cls.encode_binary_marker(marker_id)
        canary_url = f"{webhook_base_url.rstrip('/')}/v1/canary/doc/{marker_id}"

        return HoneyToken(
            token_type="DOC_WATERMARK",
            payload={
                "marker_id": marker_id,
                "zero_width_sequence": watermark_seq
            },
            canary_url=canary_url,
            description=description
        )
