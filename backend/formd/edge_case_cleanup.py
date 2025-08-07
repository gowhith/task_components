# column_cleaner.py

def clean_column_value(column_name: str, value: str) -> str | None:
    """Cleans a specific value based on column rules."""
    if not isinstance(value, str):
        return None  # Defensive: if somehow it's not string

    val = value.strip()

    # Generic Null handling
    if val.upper() in ["", "N/A", "NULL", "NONE"]:
        return None

    # Rule-based corrections
    cleaning_rules = {
        "state": {
            "Calfornia": "California",  # Known typo
            "Texs": "Texas",            # Another example
        },
        "zip_code": {
            "00000": None  # Placeholder ZIP to NULL
        },
        "issuer_name": {
            '"': '',  # Strip stray quotes
        }
    }

    if column_name in cleaning_rules:
        for match_val, corrected_val in cleaning_rules[column_name].items():
            if val == match_val:
                return corrected_val

    return val
if __name__ == "__main__":
    # Examples showing before → after
    test_cases = [
        ("state", "Calfornia", "California"),     # Typo fix
        ("state", "Texas", "Texas"),              # No change
        ("state", "N/A", None),                   # Null
        ("zip_code", "00000", None),              # ZIP edge case
        ("issuer_name", '"Acme"', '"Acme"'),      # No full match (partial quote, not replaced)
        ("issuer_name", '"', ''),                 # Exact match to quote
        ("city", "", None),                       # Default null handling
    ]

    for col, val, expected in test_cases:
        result = clean_column_value(col, val)
        assert result == expected, f"{col}: '{val}' → Expected: {expected}, Got: {result}"
        print(f"✅ {col}: '{val}' → '{result}'")
