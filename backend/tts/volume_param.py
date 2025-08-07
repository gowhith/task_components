from pydantic import BaseModel, Field, ValidationError


# ------------------ Pydantic Model ------------------ #

class SpeechParams(BaseModel):
    volume_boost: float = Field(
        default=1.0,
        ge=0.0,
        description="Optional gain factor (e.g., 1.0 = normal, 2.0 = double volume)"
    )


# ------------------ Logic to Use It ------------------ #

def print_speech_params(params: SpeechParams):
    print("🔊 Received Speech Parameters:")
    print(f"- Volume Boost: {params.volume_boost}")


# ------------------ Demo ------------------ #

def main():
    try:
        # ✅ Example 1: Valid input
        params = SpeechParams(volume_boost=1.5)
        print_speech_params(params)

        # ❌ Example 2: Invalid input (negative volume)
        invalid = SpeechParams(volume_boost=-2.0)
        print_speech_params(invalid)

    except ValidationError as e:
        print("❌ Validation Error:")
        print(e.json(indent=2))


if __name__ == "__main__":
    main()
