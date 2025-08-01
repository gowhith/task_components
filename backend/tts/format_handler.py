# format_handler.py
"""
Handles requested audio format and provides fallback/warning.
"""

from typing import Tuple, Optional


def get_supported_format(requested_format: str) -> Tuple[str, Optional[str]]:
    if requested_format.lower() == "wav":
        return "wav", None
    elif requested_format.lower() == "mp3":
        return "wav", "⚠️ MP3 not supported. Falling back to WAV."
    else:
        return "wav", f"⚠️ Format '{requested_format}' unsupported. Defaulting to WAV."


# Test cases
if __name__ == "__main__":
    for fmt in ["wav", "mp3", "ogg"]:
        final_fmt, warning = get_supported_format(fmt)
        print(f"Requested: {fmt} ➡ Final: {final_fmt} {'('+warning+')' if warning else ''}")