# 🤖 LLM Prompt Simulation Service

This module provides a lightweight simulation of a Language Model (LLM) API using Python. It includes structured prompt handling, dummy adapter architecture, and an in-memory configuration manager — all fully decoupled for testability.

---

## 🧩 Folder Purpose

To simulate how a prompt request might be handled by different LLM providers (e.g., OpenAI, Local, Dummy) in a clean and extensible backend system. Useful for mocking LLM behavior in UI testing, service integration, and experimentation with configurable model parameters.

---

## 📄 Contents

### 1. `simulate_llm.py`

Simulates an LLM prompt/response using Pydantic models.

- Defines:
  - `ModelConfiguration`: holds provider info (e.g. OpenAI), model name, temperature, token limits.
  - `GenerationRequest`: wraps the user prompt and model config.
  - `GenerationResult`: includes generated response and simulated latency.
- Includes:
  - `mock_generate_text()` — simulates a 2-second delay and echoes the prompt.
  - CLI-friendly printout of JSON output.

> ✅ *Great for mocking how an LLM backend behaves without needing a live API key.*

---

### 2. `dummy_adapter.py`

Implements a **dummy LLM adapter** using a clean interface-first design.

- Defines `ModelProviderPort` abstract base class (ABC).
- Implements `DummyLLMAdapter`, which:
  - Accepts any prompt/config.
  - Returns a hardcoded mock response.
- Demonstrates dependency-injection and mocking concepts.

> ✅ *Mimics real-world provider plugins (like Hugging Face or OpenAI) using the Adapter pattern.*

---

### 3. `config_history.py`

Tracks the last few model configurations in memory.

- Implements `InMemoryConfigurationAdapter`:
  - Saves recent `ModelConfiguration` objects.
  - Keeps up to `N=5` latest entries (FIFO logic).
  - Supports retrieval and introspection.
- Provides a `__main__` example that prints stored configurations in JSON.

> ✅ *Useful for reproducing results, caching common setups, or simulating user history.*

---

## 🧪 Learning Highlights

| Concept                    | Covered in File       |
|---------------------------|------------------------|
| Pydantic modeling          | `simulate_llm.py`, `dummy_adapter.py` |
| Async logic simulation     | `simulate_llm.py` (via `time.sleep`) |
| ABC interface & Adapter    | `dummy_adapter.py` |
| Memory-capped history store| `config_history.py` |
| JSON logging / formatting  | All modules |

---

## 💡 Extension Ideas

- Replace `DummyLLMAdapter` with a real OpenAI or HuggingFace integration
- Add CLI flag to control provider and generation parameters
- Log each request to a file for later analysis

---

## 🏁 How to Run

```bash
cd backend/llm

# Run the simulation
python simulate_llm.py

# Run dummy adapter
python dummy_adapter.py

# Save + inspect config history
python config_history.py