// stream_processor.rs
// Simulates audio data streaming and sample extraction.

#[derive(Debug)]
struct MockAudioStream {
    data: Vec<f32>,
    sample_rate: u32,
}

impl MockAudioStream {
    fn get_first_n_samples(&self, n: usize) -> Vec<f32> {
        self.data.iter().cloned().take(n).collect()
    }
}

fn main() {
    let stream = MockAudioStream {
        data: vec![0.1, 0.3, 0.5, 0.7, 0.9],
        sample_rate: 44100,
    };

    let samples = stream.get_first_n_samples(3);
    println!("🎧 First 3 samples: {:?}", samples);

    let all = stream.get_first_n_samples(10); // handles overflow safely
    println!("🔁 Requested 10, got {} samples: {:?}", all.len(), all);
}