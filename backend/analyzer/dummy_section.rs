// dummy_section.rs
// Returns a static "Dummy" SectionData with sample SQL and prompt templates

#[derive(Debug)]
struct SectionData {
    name: String,
    query_template: String,
    prompt_small: String,
    prompt_medium: String,
}

fn create_dummy_section() -> SectionData {
    SectionData {
        name: "Dummy Analysis".to_string(),
        query_template: "SELECT 'Hello Intern!' AS message;".to_string(),
        prompt_small: "Summarize result in one line.".to_string(),
        prompt_medium: "Summarize result in three sentences.".to_string(),
    }
}

fn main() {
    let section = create_dummy_section();
    println!("🧪 Dummy Section: {:?}", section);
}