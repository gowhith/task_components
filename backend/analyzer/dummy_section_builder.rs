//! Task 2: Implement a New "Dummy" Analysis Section using Builder Pattern

use std::collections::HashMap;

/// Represents a single analysis section with query + prompt templates.
#[derive(Debug)]
struct SectionData {
    name: String,
    query_template: String,
    prompt_templates: HashMap<String, String>, // e.g., Small, Medium
}

/// Fluent builder for creating a SectionData instance.
struct DummySectionBuilder {
    name: Option<String>,
    query_template: Option<String>,
    prompt_templates: HashMap<String, String>,
}

impl DummySectionBuilder {
    /// Create a new builder instance.
    fn new() -> Self {
        Self {
            name: Some("Dummy".to_string()),
            query_template: None,
            prompt_templates: HashMap::new(),
        }
    }

    /// Set the SQL query template.
    fn query(mut self, sql: &str) -> Self {
        self.query_template = Some(sql.to_string());
        self
    }

    /// Add a prompt template for a specific size.
    fn prompt(mut self, size: &str, template: &str) -> Self {
        self.prompt_templates.insert(size.to_string(), template.to_string());
        self
    }

    /// Build the final SectionData or return an error if required fields are missing.
    fn build(self) -> Result<SectionData, String> {
        let name = self.name.unwrap_or_else(|| "Unnamed".to_string());

        let query_template = match self.query_template {
            Some(q) => q,
            None => return Err("Missing SQL query template".into()),
        };

        if self.prompt_templates.is_empty() {
            return Err("At least one prompt template is required".into());
        }

        Ok(SectionData {
            name,
            query_template,
            prompt_templates: self.prompt_templates,
        })
    }
}

/// Main function to build and print the dummy section.
fn main() {
    println!("🛠 Building Dummy Analysis Section...");

    let result = DummySectionBuilder::new()
        .query("SELECT 'Hello Intern!' as message;")
        .prompt("Small", "Give a short explanation of the output.")
        .prompt("Medium", "Give a more detailed interpretation of the result.")
        .build();

    match result {
        Ok(section) => {
            println!("✅ Dummy Section Created:\n{:#?}", section);
        }
        Err(e) => {
            println!("❌ Error building section: {}", e);
        }
    }

    println!("✅ Dummy section generation completed.");
}
