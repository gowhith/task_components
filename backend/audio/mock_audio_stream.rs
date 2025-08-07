//! Simulated audio stream chunking in Rust
//! Uses Vec<f32> to represent raw audio data and slices for chunking

use std::fmt;

/// Represents a mock in-memory audio stream.
#[derive(Debug)]
struct MockAudioStream {
    data: Vec<f32>,
    sample_rate: u32,
}

impl MockAudioStream {
    /// Create a new mock audio stream.
    fn new(data: Vec<f32>, sample_rate: u32) -> Self {
        Self { data, sample_rate }
    }

    /// Returns the first `n` samples as a new Vec.
    /// If `n` is larger than the data length, it returns all available samples.
    fn get_first_n_samples(&self, n: usize) -> Vec<f32> {
        let available = self.data.len();
        let chunk_size = n.min(available);

        self.data[..chunk_size].to_vec()
    }
}

/// Custom display for pretty printing sample chunk
fn display_chunk(samples: &[f32]) {
    println!("🎧 First {} audio samples:", samples.len());
    for (i, sample) in samples.iter().enumerate() {
        println!("  Sample {}: {:.4}", i + 1, sample);
    }
}

/// Simulate usage
fn main() {
    println!("🎯 Starting mock audio stream simulation...");

    // Simulate a waveform with 20 float samples (e.g., amplitude values)
    let sample_data: Vec<f32> = (0..20).map(|x| (x as f32) / 10.0).collect();
    let audio_stream = MockAudioStream::new(sample_data, 44100);

    // Get the first 5 samples
    let chunk = audio_stream.get_first_n_samples(5);
    display_chunk(&chunk);

    // Try getting more samples than available
    let oversized_chunk = audio_stream.get_first_n_samples(50);
    println!("\n⚠️ Requesting more than available (50): Got {}", oversized_chunk.len());
    display_chunk(&oversized_chunk);

    println!("✅ Mock audio stream processing finished.");
}
