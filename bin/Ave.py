#!/usr/bin/env python3
"""
Ave.py — Read the Hail Mary using macOS voices in English, German, and Italian.

Usage:
    Ave.py                              # list languages and speakers, no audio
    Ave.py --voice VOICE --language LANGUAGE [--rate RATE]
    Ave.py --all [--language LANGUAGE] [--voice VOICE] [--rate RATE]
    Ave.py --help
"""

import argparse
import subprocess
import sys

# ── Texts ──────────────────────────────────────────────────────────────────────

TEXTS = {
    "english": (
        "Hail Mary, full of grace, the Lord is with thee.\n"
        "Blessed art thou among women,\n"
        "and blessed is the fruit of thy womb, Jesus.\n"
        "Holy Mary, Mother of God, pray for us sinners,\n"
        "now and at the hour of our death. Amen."
    ),
    "german": (
        "Gegrüßet seist du, Maria, voll der Gnade, der Herr ist mit dir.\n"
        "Du bist gebenedeit unter den Frauen,\n"
        "und gebenedeit ist die Frucht deines Leibes, Jesus.\n"
        "Heilige Maria, Mutter Gottes, bitte für uns Sünder\n"
        "jetzt und in der Stunde unseres Todes. Amen."
    ),
    "italian": (
        "Ave Maria, gratia plena, Dominus tecum.\n"
        "Benedicta tu in mulieribus,\n"
        "et benedictus fructus ventris tui, Iesus.\n"
        "Sancta Maria, Mater Dei, ora pro nobis peccatoribus,\n"
        "nunc et in hora mortis nostrae. Amen."
    ),
}

# ── Voice roster ───────────────────────────────────────────────────────────────

VOICES = {
    "english": {
        "Eddy":    "Eddy (English (US))",
        "Flo":     "Flo (English (US))",
        "Grandma": "Grandma (English (US))",
        "Grandpa": "Grandpa (English (US))",
        "Reed":    "Reed (English (US))",
        "Rocko":   "Rocko (English (US))",
        "Sandy":   "Sandy (English (US))",
        "Shelley": "Shelley (English (US))",
    },
    "german": {
        "Eddy":    "Eddy (German (Germany))",
        "Flo":     "Flo (German (Germany))",
        "Grandma": "Grandma (German (Germany))",
        "Grandpa": "Grandpa (German (Germany))",
        "Reed":    "Reed (German (Germany))",
        "Rocko":   "Rocko (German (Germany))",
        "Sandy":   "Sandy (German (Germany))",
        "Shelley": "Shelley (German (Germany))",
    },
    "italian": {
        "Eddy":    "Eddy (Italian (Italy))",
        "Flo":     "Flo (Italian (Italy))",
        "Grandma": "Grandma (Italian (Italy))",
        "Grandpa": "Grandpa (Italian (Italy))",
        "Reed":    "Reed (Italian (Italy))",
        "Rocko":   "Rocko (Italian (Italy))",
        "Sandy":   "Sandy (Italian (Italy))",
        "Shelley": "Shelley (Italian (Italy))",
    },
}

VOICE_NAMES    = list(next(iter(VOICES.values())).keys())  # same for all languages
LANGUAGE_NAMES = list(TEXTS.keys())
DEFAULT_RATE   = 100

# ── Listing ────────────────────────────────────────────────────────────────────

def list_info() -> None:
    """Print available languages and speakers; no audio."""
    print("\nAve Maria — available languages and speakers\n")
    print(f"  Languages : {', '.join(LANGUAGE_NAMES)}")
    print(f"  Voices    : {', '.join(VOICE_NAMES)}")
    print()
    print("  Run  Ave.py --help  for full usage and examples.")
    print()

# ── Core function ──────────────────────────────────────────────────────────────

def speak(voice_name: str, language: str, rate: int) -> None:
    voice_str = VOICES[language][voice_name]
    text      = TEXTS[language]

    # Header
    print(f"\n{'─' * 60}")
    print(f"  🎙  {voice_name}  ·  {language.capitalize()}  ·  rate {rate}")
    print(f"{'─' * 60}")

    # Print the full prayer text
    for line in text.splitlines():
        print(f"  {line}")
    print()

    # Speak — pass the plain text (newlines replaced with spaces for say)
    subprocess.run(
        ["say", "-v", voice_str, "-r", str(rate), text.replace("\n", " ")],
        check=True,
    )

# ── CLI ────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Ave.py",
        description=(
            "\"Hail, thou that art highly favoured, the Lord is with thee.\"\n"
            "                                          — Luke 1:28\n\n"
            "Ave Maria — hear the Hail Mary spoken by macOS voices\n"
            "in English, German, and Italian (Latin text).\n\n"
            "Run Ave.py with no arguments to list languages and speakers.\n\n"
            "The Italian voices render Church Latin more faithfully\n"
            "than German or English voices."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  Ave.py                              # list languages and speakers\n"
            "  Ave.py --voice Grandma --language italian\n"
            "  Ave.py --voice Rocko   --language german\n"
            "  Ave.py --language english --rate 80\n"
            "  Ave.py --all                        # all 24 voice/language combos\n"
            "  Ave.py --all --language italian     # all 8 Italian voices\n"
            "  Ave.py --all --voice Grandma        # Grandma in all 3 languages\n\n"
            f"Voices    : {', '.join(VOICE_NAMES)}\n"
            f"Languages : {', '.join(LANGUAGE_NAMES)}\n"
        ),
    )
    parser.add_argument(
        "--voice", "-v",
        choices=VOICE_NAMES,
        default=None,
        help=f"Voice to use. Choices: {', '.join(VOICE_NAMES)}",
    )
    parser.add_argument(
        "--language", "-l",
        choices=LANGUAGE_NAMES,
        default=None,
        help="Language / text to use. Note: Italian voices read the Latin text.",
    )
    parser.add_argument(
        "--rate", "-r",
        type=int,
        default=DEFAULT_RATE,
        metavar="WPM",
        help=f"Speech rate in words per minute (default: {DEFAULT_RATE}). "
             "Try 80 for a meditative pace, 60 for near-chant.",
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Speak with every voice. Combine with --language or --voice to filter.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args   = parser.parse_args()

    # No arguments at all → show full --help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        print()
        return

    if args.all:
        voices    = [args.voice]    if args.voice    else VOICE_NAMES
        languages = [args.language] if args.language else LANGUAGE_NAMES

        total = len(voices) * len(languages)
        print(f"\nAve Maria — {total} voice{'s' if total != 1 else ''} will speak the prayer.")

        for lang in languages:
            for voice in voices:
                speak(voice, lang, args.rate)

    else:
        # Defaults when called with partial args
        voice    = args.voice    or "Grandma"
        language = args.language or "italian"
        speak(voice, language, args.rate)

    print(f"\n{'─' * 60}")
    print("  Amen.")
    print(f"{'─' * 60}\n")


if __name__ == "__main__":
    main()
