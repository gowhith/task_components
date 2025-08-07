//! Simulated Audio Metadata Service
//! Reads mock audio file metadata from the file system (via PathBuf)
//! and calculates file size in bytes.

use std::fs;
use std::path::{PathBuf};
use std::fmt;
use std::error::Error;

/// Struct to represent audio file metadata.
#[derive(Debug)]
struct AudioMetadata {
    path: PathBuf,
    sample_rate: u32,
    channels: u16,
}

impl AudioMetadata {
    /// Creates a new AudioMetadata instance.
    fn new(path: impl Into<PathBuf>, sample_rate: u32, channels: u16) -> Self {
        Self {
            path: path.into(),
            sample_rate,
            channels,
        }
    }

    /// Attempts to retrieve the file size in bytes from the file system.
    fn file_size_bytes(&self) -> Result<u64, AudioMetadataError> {
        if !self.path.exists() {
            return Err(AudioMetadataError::FileNotFound(self.path.clone()));
        }

        let metadata = fs::metadata(&self.path).map_err(|e| {
            AudioMetadataError::IoError(self.path.clone(), e.to_string())
        })?;

        Ok(metadata.len())
    }
}

/// Custom error type for audio metadata operations.
#[derive(Debug)]
enum AudioMetadataError {
    FileNotFound(PathBuf),
    IoError(PathBuf, String),
}

impl fmt::Display for AudioMetadataError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            AudioMetadataError::FileNotFound(p) => {
                write!(f, "File not found: {}", p.display())
            }
            AudioMetadataError::IoError(p, msg) => {
                write!(f, "IO error while reading {}: {}", p.display(), msg)
            }
        }
    }
}

impl Error for AudioMetadataError {}

/// Simulates file-based metadata logic
fn main() -> Result<(), Box<dyn Error>> {
    println!("🎧 Simulating Audio Metadata Lookup...");

    // Change this to a real file on your system to test with real metadata
    let mock_path = PathBuf::from("mock_audio.wav");

    let audio_meta = AudioMetadata::new(mock_path, 44100, 2);

    match audio_meta.file_size_bytes() {
        Ok(size) => println!("📦 File size: {} bytes", size),
        Err(e) => println!("⚠️ Error: {}", e),
    }

    println!("✅ Audio metadata simulation finished.");
    Ok(())
}
