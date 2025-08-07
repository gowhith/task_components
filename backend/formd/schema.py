import json
from sqlalchemy import Column, MetaData, Table, String, Integer
from sqlalchemy.schema import CreateTable
from jinja2 import Template

# Map JSON data types to SQLAlchemy types
SQL_TYPE_MAP = {
    "string": String,
    "int": Integer,
    "integer": Integer,
    # Add more mappings as needed
}

# Load schema JSON
with open("metadata.json", "r") as f:
    metadata_json = json.load(f)

# Extract pathology tables
tables = metadata_json["pathology"]["tables"]

# SQLAlchemy metadata object
metadata = MetaData()

for table_def in tables:
    table_name = table_def["table"]
    fields = table_def["fields"]

    sqlalchemy_columns = []

    for field in fields:
        field_name = field["field"]
        field_type = field["datatype"].lower()

        if field_type not in SQL_TYPE_MAP:
            raise ValueError(f"Unsupported type: {field_type}")

        sqlalchemy_type = SQL_TYPE_MAP[field_type]
        sqlalchemy_columns.append(Column(field_name, sqlalchemy_type))

    # ➕ Add hypothetical column
    sqlalchemy_columns.append(Column("new_field", String(255)))

    # Build SQLAlchemy Table
    table = Table(table_name, metadata, *sqlalchemy_columns)

    # Generate and print SQLAlchemy SQL
    sql = str(CreateTable(table).compile(compile_kwargs={"literal_binds": True}))
    print(f"\n🔧 SQLAlchemy-generated SQL for '{table_name}':\n{sql}")

    # Fallback Jinja2 template (if needed)
    jinja_template = Template("""
CREATE TABLE IF NOT EXISTS {{ table_name }} (
{% for col in columns -%}
    {{ col.name }} {{ col.type }}{% if not loop.last %},{% endif %}
{% endfor %}
);
""")

    jinja_columns = [
        {
            "name": col.name,
            "type": f"VARCHAR(255)" if isinstance(col.type, String) else str(col.type),
        }
        for col in table.columns
    ]

    rendered_sql = jinja_template.render(table_name=table_name, columns=jinja_columns)
    print(f"\n📝 Jinja2 fallback SQL for '{table_name}':\n{rendered_sql}")
