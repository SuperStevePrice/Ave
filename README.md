# Ave Maria

> *"Hail, thou that art highly favoured, the Lord is with thee."*
> — Luke 1:28

Hear the Hail Mary spoken in many voices, in many languages, on many platforms.

---

## What This Is

**Ave** is an open-source project that brings the ancient prayer of the Ave Maria
to modern computing platforms — beginning with a Python command-line tool for macOS,
with native apps for macOS, iOS, Windows, and Linux planned.

The project was conceived by Rodney Stephen Price (called Steve), an Episcopal lay
preacher and retired software engineer, in a conversation about the meaning of the
word *bitte* in the German Hail Mary. It was built in collaboration with Claude,
Anthropic's AI assistant — an early example of human devotional intention and
artificial capability working together toward a prayerful end.

---

## Current Release: Ave.py

A Python command-line tool for macOS using the built-in `say` command.

### Requirements
- macOS (any recent version)
- Python 3
- No external dependencies

### Installation
```bash
cp Ave.py ~/bin/
chmod +x ~/bin/Ave.py
```

### Usage
```bash
Ave.py                              # show help
Ave.py --voice Grandma --language italian
Ave.py --voice Rocko   --language german
Ave.py --language english --rate 80
Ave.py --all                        # all 24 voice/language combos
Ave.py --all --language italian     # all 8 Italian voices
Ave.py --all --voice Grandma        # Grandma in all 3 languages
```

### Languages
| Language | Text |
|----------|------|
| English  | Traditional liturgical English |
| German   | Deutsches Gebet |
| Italian  | Latin text (ecclesiastical) |

### Voices
Eddy, Flo, Grandma, Grandpa, Reed, Rocko, Sandy, Shelley — available in all three languages.

> **Note:** Italian voices render Church Latin more faithfully than German or English voices.
> Rocko prays the German Ave Maria with unexpected dignity.

---

## Future Development

Native apps for macOS, iOS, Windows, and Linux are planned.
See the [`app/`](app/) folder for roadmap and architecture notes.

**Additional languages welcome.** Adding a new language requires only a text entry
and the appropriate system voice. French, Spanish, Portuguese, Polish, Tagalog —
wherever the prayer has traveled, a voice can follow.

Pull requests from any language community are welcome.

---

## License

MIT — free to use, modify, and extend for any purpose.

---

*Ave Maria, gratia plena.*
