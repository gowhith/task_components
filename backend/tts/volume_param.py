# volume_param.py
"""
Defines a speech parameter model including volume_boost.
"""

from pydantic import BaseModel


class SpeechParams(BaseModel):
    speed: float = 1.0
    pitch: float = 1.0
    volume_boost: float = 1.5  # New parameter


def print_params(params: SpeechParams):
    print("🔊 Speech Parameters:", params.dict())


if __name__ == "__main__":
    params = SpeechParams(speed=0.9, pitch=1.2, volume_boost=2.0)
    print_params(params)