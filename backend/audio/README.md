# Audio Management Service

Simulates a Rust-based audio streaming backend.

### Files:
- `grpc_client.rs` – Simulates sending/receiving gRPC messages for audio metadata and health check.
- `metadata_calc.rs` – Computes file size from mock metadata input (path, sample rate, etc.).
- `stream_processor.rs` – Returns the first N samples from a mock audio buffer.

### Highlights:
- Uses Rust structs to simulate Protobuf message interaction.
- No real audio playback—focus on system integration and API shape.
