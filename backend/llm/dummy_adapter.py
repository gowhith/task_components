# dummy_adapter.py
"""
Defines a dummy LLM provider adapter using an ABC-style interface.
"""

from abc import ABC, abstractmethod
from pydantic import BaseModel, ConfigDict
import json

# === Base Model Definitions ===

class ModelConfiguration(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    provider: str
    model_name: str
    temperature: float
    max_tokens: int
    top_k: int = 0  # Defaulted to avoid missing errors
    top_p: float = 1.0

class GenerationResult(BaseModel):
    response: str
    latency_ms: int

# === Adapter Port Interface ===

class ModelProviderPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, config: ModelConfiguration) -> GenerationResult:
        pass

# === Dummy Adapter Implementation ===

class DummyLLMAdapter(ModelProviderPort):
    def generate_text(self, prompt: str, config: ModelConfiguration) -> GenerationResult:
        return GenerationResult(
            response=f"[Dummy Response] You asked: {prompt}",
            latency_ms=123
        )

# === Example Usage ===

if __name__ == "__main__":
    adapter = DummyLLMAdapter()
    config = ModelConfiguration(
        provider="DUMMY",
        model_name="test-dummy",
        temperature=0.5,
        max_tokens=128
    )

    result = adapter.generate_text("What is Rust?", config)
    print("📘 Dummy LLM Output:")
    print(json.dumps(result.model_dump(), indent=2))  # Pydantic v2-compatible