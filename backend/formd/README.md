# Form-D Ingestion Service

Python simulation of financial data ingestion from TSV-style sources.

### Files:
- `ingestion_mock.py` – Cleans and transforms mock data rows.
- `edge_case_cleanup.py` – Handles edge cases like `"N/A"` to `None`.
- `schema_generator.py` – Converts JSON schema to SQL `CREATE TABLE` statements.
- `schema.json` – Sample metadata schema used in the generator.

### Highlights:
- Demonstrates cleaning, parsing, and schema evolution steps in a backend pipeline.
