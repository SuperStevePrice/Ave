# Ave — App Development Roadmap

This folder contains the future native application implementations of Ave Maria.

The Python CLI tool (`Ave.py`) is the working proof of concept. The apps in this
folder will bring the same prayer to broader audiences — people who do not use
a terminal, who carry their faith on a phone, who pray on Windows or Linux.

---

## Platform Plan

| Platform | Folder | Approach | Status |
|----------|--------|----------|--------|
| macOS    | `macos/` | SwiftUI + AVSpeechSynthesizer | Planned |
| iOS      | `ios/`   | Shared SwiftUI codebase with macOS | Planned |
| Windows  | `windows/` | Electron or Python/PyQt | Planned |
| Linux    | `linux/`   | Electron or Python/tkinter | Planned |

---

## Design Principles

The apps should be:

- **Simple** — one screen, one purpose: hear the prayer
- **Multilingual** — every language the prayer has traveled
- **Unhurried** — rate control, meditative pacing
- **Free** — no cost, no ads, no account required
- **Open** — MIT licensed, contributions welcome

---

## Contributing

If you are a developer who loves this prayer and knows Swift, Electron,
PyQt, or any relevant technology — pull requests are welcome.
New language text contributions are especially encouraged.

*"They said the words. The words arrived."*
