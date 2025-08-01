// grpc_client.rs
// Simulates a gRPC client by defining Rust structs that match expected Protobuf messages.

#[derive(Debug)]
struct HealthCheckRequest {
    service: String,
}

#[derive(Debug)]
struct HealthCheckResponse {
    status: String, // e.g., "SERVING"
}

#[derive(Debug)]
struct MetadataRequest {
    audio_id: String,
}

#[derive(Debug)]
struct MetadataResponse {
    sample_rate: u32,
    channels: u8,
    duration_secs: f32,
}

fn main() {
    // Simulate sending a health check request
    let health_request = HealthCheckRequest {
        service: "audio-service".into(),
    };

    let health_response = HealthCheckResponse {
        status: "SERVING".into(),
    };

    println!("📡 HealthCheckRequest: {:?}", health_request);
    println!("✅ HealthCheckResponse: {:?}", health_response);

    // Simulate metadata request/response
    let metadata_request = MetadataRequest {
        audio_id: "clip123".into(),
    };

    let metadata_response = MetadataResponse {
        sample_rate: 44100,
        channels: 2,
        duration_secs: 180.5,
    };

    println!("🎶 MetadataRequest: {:?}", metadata_request);
    println!("📊 MetadataResponse: {:?}", metadata_response);
}