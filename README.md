 Project Structure
 TASK_1/
├── frontend/
├── backend/
│   ├── formd/
│   ├── audio/
│   ├── tts/
│   ├── analyzer/
│   └── llm/
# 📘 Frontend Lit Components - Production Design Summary

This README provides a summary of the frontend components developed using **Lit**, along with the **production-level design approaches** adopted for each. These approaches are chosen for scalability, maintainability, and real-world deployment readiness.

---

## ✅ Component Summary Table

| Component                            | File Name                       | Approach Chosen                                     | Rationale                                                                 |
|-------------------------------------|----------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|
| 🎛️ Audio Mixer Element              | `audio-mixer-element.html`       | Approach 3: Shadow DOM + Slots + Custom Events      | Ensures modularity and supports interactive drag-and-drop UX.            |
| 💡 Service Health Indicator         | `status-display.html`            | Approach 2: Modular Lit Components                  | Clean separation of indicator and tooltip; reusable and reactive.         |
| 📝 Input With Character Count       | `input-component.html`           | Approach 2: Custom Event Integration                | Integrates with external forms using `form-submitted` and `submit-failed`. |
| 🤖 LLM Prompt Controller            | `llm-prompt-controller.html`     | Approach 2: External Logger Utility                 | Simulates async LLM call and logs using a decoupled logger utility.      |
| 🔗 Markdown Renderer (Text Sharing) | `render-markdown-element.html`   | Approach 2: Scoped Pub/Sub EventBus                 | Ensures component decoupling and event-driven communication.             |
| 🔊 Web Audio Player UI              | `web-audio-stream-element.html`  | Approach 2: Event-Driven UI with Custom Events      | Flexible UI triggers external logic; uses `play`, `mute`, `volume` events.|

---

## 📌 Design Principles Used

- **Shadow DOM + Slot Composition**: Used in complex visual layouts for component encapsulation.
- **Custom Events**: All interactive components emit events like `text-copied`, `submit-failed`, `volume-changed`, etc.
- **Scoped EventBus (Pub/Sub)**: Enables inter-component communication without tight DOM coupling.
- **Modularization**: Tooltip, Status Display, Input fields are built as isolated, composable components.

---

## 🧪 Test & Integration Readiness

All components:
- Are fully **runnable in the browser as standalone HTML**.
- Can be **tested using Web Test Runner or Playwright**.
- Follow **production-ready reactivity and event-based architecture**.



# 🧠 Backend Architecture Simulation – Project README

This repository simulates a production-ready backend system composed of five microservices using Python and Rust, each following clean architecture principles such as **Hexagonal Design**, **Protocol-based Interfaces**, and **Modular Components**.

---

## 📦 Overview of Backend Phases & Approaches

                        | Phase | Task | File | Approach |
                        |-------|------|------|----------|

| **1. Form-D Ingestion Service (Python)** 
| Simulate Data Ingestion | `formd_ingestor_simulation.py` | ✅ Class-Based Mini Pipeline |
| Edge Case Cleaner | `column_cleaner.py` | ✅ Rule-Based Mapping Function |
| Schema Extension | `generate_sql.py` + `mock_schema.json` | ✅ SQLAlchemy + Jinja2 Fallback |

| **2. Audio Management Service (Rust)** 
| gRPC Client Simulation | `grpc_simulation.rs` | ✅ Manual Struct Simulation |
| Audio Metadata Calc | `audio_metadata.rs` | ✅ File Metadata using PathBuf |
| Audio Chunking | `mock_audio_stream.rs` | ✅ Slice from Vec<f32> |

| **3. Company Profile Analysis (Rust)** 
| Section Discovery | `section_discovery_vec.rs` | ✅ Vec<SectionData> (Per Spec) |
| Dummy Section | `dummy_section_builder.rs` | ✅ Builder Pattern |
| SQL Interpolation | `template_engine.rs` | ✅ Mini Template Engine (w/ Cache) |

| **4. Text Generation Service (Python)**       
| LLM Request/Response Simulation | `llm_simulation.py` | ✅ Enum-Based Pydantic Models |
| Dummy LLM Provider | `dummy_llm_provider.py` | ✅ Protocol-based Typing (PEP 544) |
| Config History | `in_memory_config_adapter.py` | ✅ Circular Queue (`deque(maxlen=5)`) |

| **5. Text-to-Speech (TTS) Service (Python)** 
| TTS gRPC Simulation | `simulate_tts_client.py` | ✅ `.proto` → `tts_pb2.py` (grpcio-tools) |
| Add `volume_boost` Param | `speech_params.py` | ✅ Pydantic Model |
| Audio Format Resolution | `audio_format_resolver.py` | ✅ Dict-Based Format Mapping |

---

## ✅ Architectural Patterns Used

- **Hexagonal Architecture (Ports & Adapters)**
- **Protocol-based Interfaces (`typing.Protocol`)**
- **Class + Function Separation**
- **Validation First Design (`pydantic`)**
- **Mock-first Testing**

---

## 🛠️ Tech Stack

| Language | Use Case |
|----------|----------|
| Python | gRPC simulation, LLM adapters, TTS |
| Rust | Audio management, ingestion pipeline, section analysis |
| Protobuf | gRPC message definitions |
| SQLAlchemy | Dynamic schema simulation |
| Pydantic | Data validation & modeling |
| Deque | Config caching (circular queue) |

---

## 🧪 Testing Philosophy

- Isolated unit test functions with validation
- Graceful error handling with `try/except`
- Simulated payloads instead of real network calls
- Mocking responses for LLM and TTS components

---
