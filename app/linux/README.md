# Ave — Linux App

## Planned Approach

A Linux desktop application using **Electron** or **Python/tkinter**,
sharing as much code as possible with the Windows implementation.

## Speech on Linux

Linux text-to-speech options include:
- **espeak-ng** — lightweight, widely available, good multilingual support
- **Festival** — richer voices, more configuration
- **pyttsx3** — Python wrapper that uses espeak-ng on Linux

## Planned Features

- Same language, voice, and rate controls as other platforms
- Compatible with major desktop environments (GNOME, KDE, XFCE)
- Installable via package or AppImage

## Note on Voices

Linux TTS voices are more variable than macOS system voices.
The app will detect available voices and offer those that match
the selected language.

## Status

**Planned.** Dependent on Windows/Electron work.

Contributions from Linux developers especially welcome.
See `../README.md` for principles.
