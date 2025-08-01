# ingestion_mock.py
"""
Simulates raw Form-D ingestion by transforming mock TSV-like rows
into cleaned data using a cleanup function.
"""

from typing import List

# Mock raw TSV-like rows
raw_rows = [
    ["Company A", "1000000", "2025-07-29"],
    ["Company B", "N/A", "2025-07-28"],
    ["Company C", "2500000", "N/A"]
]

def cleanup(row: List[str]) -> List:
    def sanitize(value):
        if value == "N/A":
            return None
        try:
            if value.isdigit():
                return int(value)
            return value
        except:
            return value

    return [sanitize(cell) for cell in row]

# Expected cleaned rows
expected = [
    ["Company A", 1000000, "2025-07-29"],
    ["Company B", None, "2025-07-28"],
    ["Company C", 2500000, None]
]

# Apply cleanup
cleaned = [cleanup(row) for row in raw_rows]

# Assertions
assert cleaned == expected, f"Cleaned output mismatch:\n{cleaned}\n!=\n{expected}"

print("✅ Data ingestion simulation passed.")