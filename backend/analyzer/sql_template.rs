// sql_template.rs
// Replaces placeholders in SQL template using a HashMap

use std::collections::HashMap;

fn interpolate_template(template: &str, params: &HashMap<String, String>) -> String {
    let mut result = template.to_string();
    for (key, val) in params {
        let placeholder = format!("{{{}}}", key);
        result = result.replace(&placeholder, val);
    }
    result
}

fn main() {
    let template = "SELECT * FROM {table_name} WHERE id = {id} ORDER BY {order_col};";

    let mut params = HashMap::new();
    params.insert("table_name".to_string(), "issuers".to_string());
    params.insert("id".to_string(), "42".to_string());
    params.insert("order_col".to_string(), "name".to_string());

    let interpolated = interpolate_template(template, &params);

    println!("🧠 Original Template: {}", template);
    println!("🔧 Interpolated SQL: {}", interpolated);
}