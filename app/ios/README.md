# Ave — iOS App

## Planned Approach

A native iOS application sharing the SwiftUI codebase developed for macOS,
adapted for the iPhone and iPad form factor.

## Architecture

- **Language:** Swift
- **UI Framework:** SwiftUI
- **Speech:** AVSpeechSynthesizer (AVFoundation)
- **Deployment Target:** iOS 16 or later
- **Distribution:** App Store (free)

## Planned Features

- All features of the macOS app
- Portrait and landscape layouts
- Large text display of the prayer as it is spoken
- Suitable for personal devotion, catechesis, and language learning

## Relationship to macOS App

SwiftUI's cross-platform support means the core logic, text data,
and speech code will be written once and shared.
The iOS target adds only layout adaptations.

## Status

**Planned.** Dependent on macOS app development.

Contributions welcome — see `../README.md` for principles.
