import logging
from typing import List, Dict, Any

# --- Setup logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FormDIngestor")

class DataValidationError(Exception):
    pass

class MockFormDIngestor:
    def __init__(self, raw_data: List[Dict[str, Any]]):
        self.raw_data = raw_data
        self.cleaned_data = []

    def clean_row(self, row: Dict[str, str]) -> Dict[str, Any]:
        try:
            # Clean and normalize each field
            issuer_name = row.get("issuer_name", "").strip().strip('"') or None
            zip_code = self.clean_zip_code(row.get("zip_code", ""))
            phone_number = self.clean_phone(row.get("phone_number", ""))
            city = row.get("city", "").strip() or "UNKNOWN"

            # Truncate long names only if issuer_name is not None
            if issuer_name is not None and len(issuer_name) > 100:
                issuer_name = issuer_name[:100]

            return {
                "issuer_name": issuer_name,
                "zip_code": zip_code,
                "phone_number": phone_number,
                "city": city
            }

        except Exception as e:
            logger.error(f"Error cleaning row: {e}")
            raise DataValidationError(f"Invalid row: {row}")

    def clean_zip_code(self, value: str) -> str:
        if value.upper() in ["", "N/A", "NULL"]:
            return None
        return value.zfill(5)

    def clean_phone(self, value: str) -> str:
        digits = ''.join(filter(str.isdigit, value))
        if len(digits) != 10:
            return None
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

    def run(self) -> List[Dict[str, Any]]:
        for row in self.raw_data:
            try:
                cleaned = self.clean_row(row)
                self.cleaned_data.append(cleaned)
                logger.info(f"Cleaned: {cleaned}")
            except DataValidationError as e:
                logger.warning(f"Skipping row due to validation error: {e}")
        return self.cleaned_data

# --- Sample Mock Raw Data ---
mock_raw_data = [
    {
        "issuer_name": ' "Acme Corp" ',
        "zip_code": "1234",
        "phone_number": "(123) 456-7890",
        "city": "New York"
    },
    {
        "issuer_name": '""',
        "zip_code": "N/A",
        "phone_number": "1234567",
        "city": "   "
    }
]

# --- Expected Cleaned Output ---
expected_cleaned = [
    {
        "issuer_name": "Acme Corp",
        "zip_code": "01234",
        "phone_number": "123-456-7890",
        "city": "New York"
    },
    {
        "issuer_name": None,
        "zip_code": None,
        "phone_number": None,
        "city": "UNKNOWN"
    }
]

# --- Run Ingestor ---
if __name__ == "__main__":
    ingestor = MockFormDIngestor(mock_raw_data)
    result = ingestor.run()

    # --- Assertions (can convert to pytest later) ---
    assert result == expected_cleaned, f"Output mismatch!\nGot: {result}\nExpected: {expected_cleaned}"

