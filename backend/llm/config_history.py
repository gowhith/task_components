# config_history.py
"""
Stores a rolling history of recent ModelConfigurations.
"""

from typing import List
from pydantic import BaseModel, ConfigDict
import json

class ModelConfiguration(BaseModel):
    model_config = ConfigDict(protected_namespaces=())       

                                                                                                  # ✅ Avoid model_name conflict
    
    provider: str
    model_name: str
    temperature: float
    max_tokens: int

class InMemoryConfigurationAdapter: 
    def __init__(self, capacity: int = 5):
        self.history: List[ModelConfiguration] = []
        self.capacity = capacity

    def save_configuration(self, config: ModelConfiguration):
        if len(self.history) >= self.capacity:
            self.history.pop(0)
        self.history.append(config)

    def get_config_history(self) -> List[ModelConfiguration]:
        return self.history

                                                                                                      # === Example Usage ===

if __name__ == "__main__":
    adapter = InMemoryConfigurationAdapter()

                                                     # Simulate saving 6 configurations (one will be dropped due to cap = 5)
    
    for i in range(6):
        cfg = ModelConfiguration(
            provider="DUMMY",
            model_name=f"model-{i}",
            temperature=0.6 + i * 0.1,
            max_tokens=128
        )
        adapter.save_configuration(cfg)

    print("📚 Recent Configurations:")
    for config in adapter.get_config_history():
        print(json.dumps(config.model_dump()))