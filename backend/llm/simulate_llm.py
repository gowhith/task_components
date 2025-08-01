# simulate_llm.py
from pydantic import BaseModel, ConfigDict
from typing import Optional
import json
import time

# === Pydantic Models ===

class ModelConfiguration(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    provider: str  # e.g., "LOCAL", "OPENAI"
    model_name: str
    temperature: float
    max_tokens: int

class GenerationRequest(BaseModel):
    prompt: str
    config: ModelConfiguration

class GenerationResult(BaseModel):
    response: str
    latency_ms: int

# === Mock Text Generation Function ===

def mock_generate_text(request: GenerationRequest) -> GenerationResult:
    start_time = time.time()
    # Simulated logic: Echo back the prompt
    output = f"Mocked response from {request.config.model_name}: \"{request.prompt}\""
    latency = int((time.time() - start_time) * 1000)  # Simulated latency in ms
    return GenerationResult(response=output, latency_ms=latency)

# === CLI Usage ===

if __name__ == "__main__":
    print("🔧 Initializing Model Configuration...\n")
    config = ModelConfiguration(
        provider="LOCAL",
        model_name="mock-model-v1",
        temperature=0.7,
        max_tokens=256
    )

    print("🧠 Type your prompts (type 'exit' to quit):\n")
    while True:
        prompt_input = input("💬 You: ")
        if prompt_input.strip().lower() in ("exit", "quit"):
            print("👋 Exiting...")
            break

        request = GenerationRequest(prompt=prompt_input, config=config)
        response = mock_generate_text(request)

        print("\n📝 Request JSON:")
        print(json.dumps(request.model_dump(), indent=2))
        print("\n🤖 Response:")
        print(json.dumps(response.model_dump(), indent=2))
        print("-" * 40)
