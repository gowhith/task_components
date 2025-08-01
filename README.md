# 🔧 Intern Task Suite: Frontend + Backend Projects

This project demonstrates a sandboxed implementation of multiple frontend components and backend microservices across Python and Rust.

---

## 📁 Project Structure

```
TASK_1/
├── frontend/
├── backend/
│   ├── formd/
│   ├── audio/
│   ├── tts/
│   ├── analyzer/
│   └── llm/
```

---

## ✨ Frontend Components (Lit)

All components are implemented using [Lit](https://lit.dev/) and work independently via browser:

| Component                | File                      | Key Feature                             |
|--------------------------|---------------------------|------------------------------------------|
| Audio Mixer              | `audio-mixer.html`        | Drag-and-drop reordering                 |
| Health Status Tooltip    | `health-status.html`      | Status dot + hover tooltip               |
| Input Validation         | `input-validation.html`   | Live char count + overflow + error       |
| LLM Logger               | `llm-logger.html`         | Prompt + mock response + logger          |
| Text Copy Bridge         | `text-copy-demo.html`     | CustomEvent-based cross-component sync   |
| Audio UI (Mock)          | `audio-ui.html`           | Play/pause + volume + mute + event logs  |

---

## 🧩 Backend Services (Python + Rust)

| Service         | Language | Description                                  |
|------------------|----------|----------------------------------------------|
| FormD Ingestion  | Python   | Cleans TSV data, schema evolution            |
| Audio Mgmt       | Rust     | Simulated audio stream + gRPC logic          |
| Text-to-Speech   | Python   | Fakes TTS API and format handling            |
| Company Analyzer | Rust     | SQL templating + section logic               |
| LLM Controller   | Python   | Fake prompt generation + config management   |

---

## 🚀 Getting Started

### Frontend
```bash
cd TASK_1/frontend
npx serve
# Open browser at: http://localhost:3000/
```

### Backend (Python)
```bash
cd TASK_1/backend/formd
python ingestion_mock.py
```

### Backend (Rust)
```bash
cd TASK_1/backend/audio
rustc grpc_client.rs && ./grpc_client
```

---

## 📚 Learning Highlights

- 🧠 LLM Simulation
- 🧾 Form ingestion + schema evolution
- 🎵 Audio & TTS APIs
- 🔧 Event-driven Lit components
- ✅ Component-level UI validation

---

## 🛠 Tools

- `lit` (frontend)
- `pydantic`, `abc` (Python)
- `rustc` (Rust microservices)
- `serve` for local browser testing

---
