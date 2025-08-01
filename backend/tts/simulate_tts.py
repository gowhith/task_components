# simulate_tts.py
"""
Simulates a TTS gRPC-like request/response interaction.
"""

from pydantic import BaseModel
from typing import Literal


class GenerateSpeechRequest(BaseModel):
    text: str
    voice: Literal["male", "female"]
    language: str


class GenerateSpeechResponse(BaseModel):
    audio: bytes
    sample_rate: int
    format: str
    duration_secs: float


def simulate_tts(req: GenerateSpeechRequest) -> GenerateSpeechResponse:
    return GenerateSpeechResponse(
        audio=b'\x00\x01\x02\x03',
        sample_rate=22050,
        format="wav",
        duration_secs=2.3
    )


if __name__ == "__main__":
    req = GenerateSpeechRequest(
        text="Welcome to the demo.",
        voice="female",
        language="en-US"
    )

    res = simulate_tts(req)

    print("📤 TTS Request:", req.json())
    print("📥 TTS Response:", res.dict())