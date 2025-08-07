from typing import Optional


# ------------------ Format Resolver Function ------------------ #

def resolve_audio_format(requested_format: str) -> tuple[str, Optional[str]]:
    """
    Resolves the actual audio output format and returns a warning message if needed.

    Args:
        requested_format (str): The audio format requested by the user.

    Returns:
        Tuple[str, Optional[str]]: The actual format used, and an optional warning message.
    """
    requested = requested_format.strip().lower()

    # Format map: format → (actual_format, optional warning)
    format_map = {
        "wav": ("wav", None),
        "mp3": ("wav", "MP3 not yet supported, defaulting to WAV."),
    }

    return format_map.get(
        requested,
        ("wav", "Unsupported format, defaulting to WAV.")
    )


# ------------------ Demo / Example Usage ------------------ #

def main():
    test_inputs = ["wav", "mp3", "ogg", "aac", "WAV", "", "Mp3"]

    for fmt in test_inputs:
        actual, warning = resolve_audio_format(fmt)
        print(f"🔍 Requested format: {fmt or '<empty>'}")
        print(f"✅ Resolved format: {actual}")
        if warning:
            print(f"⚠️ Warning: {warning}")
        print("-" * 40)


if __name__ == "__main__":
    main()
