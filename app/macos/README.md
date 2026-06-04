# Ave — macOS App

## Planned Approach

A native macOS application built with **SwiftUI** and **AVSpeechSynthesizer**
— the same speech engine that powers `Ave.py` under the hood, exposed through
a clean, prayerful native interface.

## Architecture

- **Language:** Swift
- **UI Framework:** SwiftUI
- **Speech:** AVSpeechSynthesizer (AVFoundation)
- **Deployment Target:** macOS 13 Ventura or later
- **Distribution:** Mac App Store (free) and direct download

## Planned Features

- Language selector: English, German, Italian (Latin), and more
- Voice selector: all available system voices for the chosen language
- Rate slider: from conversational to near-chant
- Prayer text displayed line by line as spoken
- Simple, uncluttered interface — one screen, one purpose

## Shared Codebase

The macOS and iOS apps will share a single SwiftUI codebase,
differing only in layout adaptations for screen size.
See `../ios/` for iOS-specific notes.

## Status

**Planned.** Xcode project not yet created.

Contributions welcome — see `../README.md` for principles.
