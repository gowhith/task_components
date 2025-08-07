//! Task 3: Simulate SQL Query Template Interpolation using a Mini Template Engine

use std::collections::HashMap;

/// Represents a reusable mini template engine for SQL interpolation.
struct TemplateEngine {
    cache: HashMap<String, String>, // Caches previously rendered templates
}

impl TemplateEngine {
    /// Creates a new template engine instance.
    fn new() -> Self {
        Self {
            cache: HashMap::new(),
        }
    }

    /// Interpolates the given template with parameters.
    /// Replaces all placeholders like `{key}` with values from the map.
    fn render(&mut self, template: &str, params: &HashMap<String, String>) -> Result<String, String> {
        // Return cached version if it already exists
        if let Some(cached) = self.cache.get(template) {
            return Ok(cached.clone());
        }

        let mut result = template.to_string();

        for (key, value) in params {
            let placeholder = format!("{{{}}}", key);
            result = result.replace(&placeholder, value);
        }

        // Validation: ensure no unresolved placeholders remain
        if result.contains('{') && result.contains('}') {
            return Err("Missing parameter for one or more placeholders.".to_string());
        }

        // Cache the rendered result
        self.cache.insert(template.to_string(), result.clone());

        Ok(result)
    }

    /// Utility to extend a base query with additional clauses (e.g., ORDER BY).
    fn extend_query(base: &str, clause: &str) -> String {
        format!("{} {}", base.trim_end_matches(';'), clause)
    }
}

/// Example usage
fn main() {
    let mut engine = TemplateEngine::new();

    let base_template = "SELECT * FROM {table_name} WHERE id = {id};";
    let mut params = HashMap::new();
    params.insert("table_name".to_string(), "issuers".to_string());
    params.insert("id".to_string(), "123".to_string());

    println!("🔍 Rendering base template...");
    match engine.render(base_template, &params) {
        Ok(query) => println!("✅ Rendered SQL:\n{}\n", query),
        Err(e) => println!("❌ Error: {}", e),
    }

    // Now extend the query
    let extended = TemplateEngine::extend_query(base_template, "ORDER BY created_at DESC;");
    println!("🛠 Extended Template:\n{}\n", extended);

    match engine.render(&extended, &params) {
        Ok(query) => println!("✅ Extended Rendered SQL:\n{}", query),
        Err(e) => println!("❌ Error: {}", e),
    }
}
