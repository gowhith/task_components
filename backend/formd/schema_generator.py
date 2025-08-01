# schema_generator.py
"""
Reads schema.json and generates SQL `CREATE TABLE` with an added column.
"""

import json

# Load mock schema
with open("schema.json") as f:
    schema = json.load(f)

table_name = list(schema.keys())[0]
columns = schema[table_name]["columns"]

# Add a new column dynamically
columns["new_field"] = "VARCHAR(255)"

# Generate SQL
sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
sql += ",\n".join([f"  {col} {dtype}" for col, dtype in columns.items()])
sql += "\n);"

print("Generated SQL:")
print(sql)