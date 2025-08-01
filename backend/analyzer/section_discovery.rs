// section_discovery.rs
// Simulates extracting section names from a mock analysis structure

#[derive(Debug)]
struct SectionData {
    name: String,
    query_template: String,
}

#[derive(Debug)]
struct CompanyProfileAnalysis {
    sections: Vec<SectionData>,
}

impl CompanyProfileAnalysis {
    fn get_section_names(&self) -> Vec<String> {
        self.sections.iter().map(|s| s.name.clone()).collect()
    }
}

fn main() {
    let analysis = CompanyProfileAnalysis {
        sections: vec![
            SectionData {
                name: "Summary".to_string(),
                query_template: "SELECT * FROM summary;".to_string(),
            },
            SectionData {
                name: "Financials".to_string(),
                query_template: "SELECT * FROM financials;".to_string(),
            },
            SectionData {
                name: "Ownership".to_string(),
                query_template: "SELECT * FROM ownership;".to_string(),
            },
        ],
    };

    let names = analysis.get_section_names();
    println!("📊 Available Sections: {:?}", names);
}