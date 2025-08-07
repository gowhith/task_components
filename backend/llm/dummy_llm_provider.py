from typing import Protocol
from enum import Enum
from pydantic import BaseModel
import json
import time


# ------------ Enums ------------ #

class ProviderType(str, Enum):
    LOCAL = "LOCAL"
    OPENAI = "OPENAI"

class ModelKind(str, Enum):  # Renamed to avoid 'model_' conflict
    CAUSAL_LM = "CAUSAL_LM"
    SEQ2SEQ = "SEQ2SEQ"


# ------------ Pydantic Models ------------ #

class ModelConfiguration(BaseModel):
    name: str
    provider: ProviderType
    kind: ModelKind  # renamed from model_type
    max_tokens: int = 512
    temperature: float = 0.7
    device: str = "cpu"

    model_config = {"protected_namespaces": ()}


class GenerationRequest(BaseModel):
    prompt: str
    config: ModelConfiguration


class GenerationResult(BaseModel):
    output_text: str
    token_count: int
    duration_secs: float
    model_name: str

    model_config = {"protected_namespaces": ()}


# ------------ Protocol Interface (Port) ------------ #

class ModelProviderPort(Protocol):
    def generate_text(self, request: GenerationRequest) -> GenerationResult:
        ...


# ------------ Dummy Adapter ------------ #

class DummyLLMProvider:
    def generate_text(self, request: GenerationRequest) -> GenerationResult:
        start = time.time()

        return GenerationResult(
            output_text="Hello from Dummy LLM!",
            token_count=len(request.prompt.split()),
            duration_secs=round(time.time() - start, 3),
            model_name=request.config.name
        )


# ------------ Demo ------------ #

def main():
    config = ModelConfiguration(
        name="dummy-llm",
        provider=ProviderType.LOCAL,
        kind=ModelKind.CAUSAL_LM,
        max_tokens=100,
        temperature=0.5,
        device="cpu"
    )

    request = GenerationRequest(
        prompt="What is hexagonal architecture?",
        config=config
    )

    provider: ModelProviderPort = DummyLLMProvider()
    result = provider.generate_text(request)

    print("✅ Dummy LLM Result:")
    print(json.dumps(result.model_dump(), indent=2))  # ✅ Works in Pydantic v2


if __name__ == "__main__":
    main()
