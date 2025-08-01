# edge_case_cleanup.py
"""
Standalone cleanup function handling "N/A" values and conversion.
Includes test cases to validate edge behavior.
"""

def cleanup(value: str):
    if value == "N/A":
        return None
    if value.isdigit():
        return int(value)
    return value

# ✅ Test cases
examples = ["12345", "N/A", "Company ABC"]
results = [cleanup(val) for val in examples]

# Expected: [12345, None, "Company ABC"]
print("Input values:     ", examples)
print("Cleaned values:   ", results)