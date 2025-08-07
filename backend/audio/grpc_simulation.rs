//! Simulated gRPC client for Audio Management Service
//! Defines manual Protobuf-like structs, constructs request messages,
//! and parses mock responses to demonstrate message flow.

use std::error::Error;
use std::fmt;

/// HealthCheckRequest sent to the Audio Management Service.
#[derive(Debug)]
struct HealthCheckRequest {
    service_name: String,
}

impl HealthCheckRequest {
    fn new(service_name: &str) -> Result<Self, ValidationError> {
        if service_name.trim().is_empty() {
            return Err(ValidationError("Service name cannot be empty"));
        }
        Ok(Self {
            service_name: service_name.trim().to_string(),
        })
    }
}

/// Response to a HealthCheckRequest.
#[derive(Debug)]
struct HealthCheckResponse {
    healthy: bool,
    message: String,
}

/// Request for audio file metadata.
#[derive(Debug)]
struct MetadataRequest {
    file_path: String,
}

impl MetadataRequest {
    fn new(file_path: &str) -> Result<Self, ValidationError> {
        if file_path.trim().is_empty() {
            return Err(ValidationError("File path is required"));
        }
        Ok(Self {
            file_path: file_path.trim().to_string(),
        })
    }
}

/// Response containing audio file metadata.
#[derive(Debug)]
struct MetadataResponse {
    sample_rate: u32,
    channels: u32,
    duration_secs: f32,
}

/// Custom error type for validation errors.
#[derive(Debug)]
struct ValidationError(&'static str);

impl fmt::Display for ValidationError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Validation error: {}", self.0)
    }
}

impl Error for ValidationError {}

/// Simulated client demonstrating construction and parsing of messages.
fn main() -> Result<(), Box<dyn Error>> {
    println!("🎯 Starting simulated gRPC client...");

    // Construct a health check request
    let health_req = HealthCheckRequest::new("AudioStreamer")?;
    println!("🩺 HealthCheckRequest:\n{:#?}", health_req);

    // Mock health response
    let mock_health_resp = HealthCheckResponse {
        healthy: true,
        message: "Service is running smoothly".into(),
    };
    println!("✅ HealthCheckResponse (mock):\n{:#?}", mock_health_resp);

    // Construct a metadata request
    let meta_req = MetadataRequest::new("/mock/path/audio.wav")?;
    println!("📦 MetadataRequest:\n{:#?}", meta_req);

    // Mock metadata response
    let mock_meta_resp = MetadataResponse {
        sample_rate: 48000,
        channels: 2,
        duration_secs: 92.75,
    };
    println!("🎧 MetadataResponse (mock):\n{:#?}", mock_meta_resp);

    println!("✅ Simulation completed successfully.");
    Ok(())
}
