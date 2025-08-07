from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict
import json


# ------------------ ENUMS ------------------ #

class ProviderType(str, Enum):
    LOCAL = "LOCAL"
    OPENAI = "OPENAI"
    CLAUDE = "CLAUDE"
    HUGGINGFACE = "HUGGINGFACE"


class ModelKind(str, Enum):  # renamed from `model_type` to avoid conflict
    CAUSAL_LM = "CAUSAL_LM"
    SEQ2SEQ = "SEQ2SEQ"


# ------------------ Pydantic Models ------------------ #

class ModelConfiguration(BaseModel):
    name: str = Field(..., min_length=1)
    provider: ProviderType
    kind: ModelKind  # renamed from model_type
    max_tokens: int = 512
    temperature: float = 0.7
    device: Optional[str] = "cpu"

    model_config = {"protected_namespaces": ()}  # Allow field names like 'model_name'

    @field_validator("temperature")
    @classmethod
    def validate_temperature(cls, val):
        if not (0.0 <= val <= 1.0):
            raise ValueError("temperature must be between 0.0 and 1.0")
        return val


class GenerationRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    config: ModelConfiguration

    @field_validator("prompt")
    @classmethod
    def prompt_must_not_be_empty(cls, val):
        if not val.strip():
            raise ValueError("Prompt must not be empty.")
        return val


class GenerationResult(BaseModel):
    output_text: str
    token_count: int
    duration_secs: float
    model_name: str

    model_config = {"protected_namespaces": ()}


# ------------------ Mock Logic ------------------ #

def mock_generate_text(request: GenerationRequest) -> GenerationResult:
    output = f"Simulated response for: '{request.prompt}'"
    token_count = len(request.prompt.split())
    duration = 0.05

    return GenerationResult(
        output_text=output,
        token_count=token_count,
        duration_secs=duration,
        model_name=request.config.name
    )


# ------------------ Main ------------------ #

def main():
    try:
        config = ModelConfiguration(
            name="local-llm-v1",
            provider=ProviderType.LOCAL,
            kind=ModelKind.CAUSAL_LM,
            max_tokens=256,
            temperature=0.5,
            device="cpu"
        )

        request = GenerationRequest(
            prompt="What is the capital of France?",
            config=config
        )

        response = mock_generate_text(request)

        print("🔹 GenerationRequest JSON:\n", json.dumps(request.model_dump(), indent=2))
        print("\n🔹 GenerationResult JSON:\n", json.dumps(response.model_dump(), indent=2))

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
