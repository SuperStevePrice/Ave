# Ave — Windows App

## Planned Approach

A Windows desktop application using either **Electron** (JavaScript/HTML)
or **PyQt6** (Python), providing the same Ave Maria experience to Windows users.

## Options Under Consideration

### Option A: Electron
- Cross-platform with Linux from a single codebase
- Uses the Windows Speech API (SAPI) via a Node.js bridge
- Familiar web technologies (HTML, CSS, JavaScript)

### Option B: PyQt6
- Closer in spirit to Ave.py
- Uses `pyttsx3` or Windows SAPI directly for speech
- Simpler architecture for a single-purpose app

## Planned Features

- Same language, voice, and rate controls as other platforms
- Windows-native look and feel
- Free, no installer required if possible (portable .exe)

## Status

**Planned.** Architecture decision pending.

Contributions from Windows developers especially welcome.
See `../README.md` for principles.
