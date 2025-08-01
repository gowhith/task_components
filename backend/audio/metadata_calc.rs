// metadata_calc.rs
// Simulates metadata analysis with a custom method: file_size_bytes().

use std::path::PathBuf;

#[derive(Debug)]
struct AudioMetadata {
    path: PathBuf,
    sample_rate: u32,
    channels: u16,
    duration_secs: f32,
}

impl AudioMetadata {
    fn file_size_bytes(&self) -> u64 {
        // Estimate file size as: duration × sample_rate × channels × 2 bytes/sample
        (self.duration_secs * self.sample_rate as f32 * self.channels as f32 * 2.0) as u64
    }
}

fn main() {
    let metadata = AudioMetadata {
        path: PathBuf::from("mock/audio/clip.wav"),
        sample_rate: 44100,
        channels: 2,
        duration_secs: 60.0,
    };

    println!("🔎 AudioMetadata: {:?}", metadata);
    println!("📁 Estimated file size: {} bytes", metadata.file_size_bytes());
}