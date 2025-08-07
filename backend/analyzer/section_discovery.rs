//! Task: Simulate Analysis Section Discovery
//! Implements Vec-based CompanyProfileAnalysis structure with GetSectionNames logic

/// Represents a simplified analysis section.
#[derive(Debug)]
struct SectionData {
    name: String,
    query_template: String,
}

/// Holds a collection of analysis sections.
#[derive(Debug)]
struct CompanyProfileAnalysis {
    sections: Vec<SectionData>,
}

impl CompanyProfileAnalysis {
    /// Create a new analysis instance with some mock sections.
    fn new() -> Self {
        let sections = vec![
            SectionData {
                name: "Issuer Overview".to_string(),
                query_template: "SELECT * FROM issuers WHERE id = {id}".to_string(),
            },
            SectionData {
                name: "Financial Metrics".to_string(),
                query_template: "SELECT revenue, expenses FROM financials WHERE company_id = {id}".to_string(),
            },
            SectionData {
                name: "Fundraising Events".to_string(),
                query_template: "SELECT * FROM offerings WHERE issuer_id = {id}".to_string(),
            },
        ];

        Self { sections }
    }

    /// Simulates the GetSectionNames gRPC call by returning a list of available section names.
    fn get_section_names(&self) -> Vec<String> {
        self.sections.iter().map(|s| s.name.clone()).collect()
    }
}

/// Main function to demonstrate section discovery.
fn main() {
    println!("📊 Initializing CompanyProfileAnalysis...");

    let analysis = CompanyProfileAnalysis::new();
    let section_names = analysis.get_section_names();

    if section_names.is_empty() {
        println!("⚠️ No sections available.");
    } else {
        println!("✅ Available Analysis Sections:");
        for name in section_names {
            println!("- {}", name);
        }
    }

    println!("✅ Section discovery completed.");
}
