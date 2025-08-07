from enum import Enum
from collections import deque
from typing import List
from pydantic import BaseModel
import json


# ------------------ Enums ------------------ #

class ProviderType(str, Enum):
    LOCAL = "LOCAL"
    OPENAI = "OPENAI"

class ModelKind(str, Enum):  # Avoid "model_" conflicts
    CAUSAL_LM = "CAUSAL_LM"
    SEQ2SEQ = "SEQ2SEQ"


# ------------------ Pydantic Configuration Model ------------------ #

class ModelConfiguration(BaseModel):
    name: str
    provider: ProviderType
    kind: ModelKind
    max_tokens: int = 512
    temperature: float = 0.7
    device: str = "cpu"

    model_config = {"protected_namespaces": ()}


# ------------------ In-Memory Adapter ------------------ #

class InMemoryConfigurationAdapter:
    def __init__(self, history_size: int = 5):
        self._current: ModelConfiguration | None = None
        self._history: deque[ModelConfiguration] = deque(maxlen=history_size)

    def save_configuration(self, config: ModelConfiguration) -> None:
        if self._current:
            self._history.append(self._current)
        self._current = config

    def get_current(self) -> ModelConfiguration | None:
        return self._current

    def get_config_history(self) -> List[ModelConfiguration]:
        return list(self._history)


# ------------------ Demo ------------------ #

def main():
    adapter = InMemoryConfigurationAdapter()

    for i in range(1, 7):
        config = ModelConfiguration(
            name=f"llm-v{i}",
            provider=ProviderType.LOCAL,
            kind=ModelKind.CAUSAL_LM,
            max_tokens=256 + i * 10,
            temperature=0.5,
            device="cpu"
        )
        adapter.save_configuration(config)
        print(f"✅ Saved configuration: {config.name}")

    print("\n🧠 Current Config:")
    current = adapter.get_current()
    print(json.dumps(current.model_dump(), indent=2))

    print("\n🕓 Config History:")
    for c in adapter.get_config_history():
        print(f"- {c.name}")


if __name__ == "__main__":
    main()
