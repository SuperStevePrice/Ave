#!/usr/bin/env python3
"""
installAve.py — Install Ave.py to ~/bin with backup and PATH verification.

Usage:
    python3 installAve.py
"""

import os
import shutil
import stat
import sys
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────

HOME       = Path.home()
BIN        = HOME / "bin"
BACKUP     = BIN / "backup"
AVE_SRC    = Path(__file__).parent / "bin" / "Ave.py"
AVE_DST    = BIN / "Ave.py"
ALPHA      = BACKUP / "Ave.py.alpha"

# ── Helpers ────────────────────────────────────────────────────────────────────

def make_executable(path: Path) -> None:
    """Set rwxr-xr-x permissions on a file."""
    path.chmod(stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP |
               stat.S_IROTH | stat.S_IXOTH)

def check_path() -> None:
    """Warn if ~/bin is not on the PATH."""
    path_dirs = os.environ.get("PATH", "").split(":")
    if str(BIN) not in path_dirs:
        print(f"\n  ⚠️  Warning: {BIN} is not on your PATH.")
        print("     Add this to your shell profile (~/.kshrc or equivalent):")
        print(f"     export PATH=\"$HOME/bin:$PATH\"\n")
    else:
        print(f"  ✅  {BIN} is on your PATH.")

# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    print("\nAve Maria Installer")
    print("=" * 60)
    print(f'  "In the beginning was the Word." — John 1:1\n')

    # ── Verify source exists ───────────────────────────────────────────────────
    if not AVE_SRC.exists():
        print(f"  ❌  Source not found: {AVE_SRC}")
        print("     Run installAve.py from the root of the Ave project.")
        sys.exit(1)
    print(f"  📄  Source   : {AVE_SRC}")

    # ── Create ~/bin if needed ─────────────────────────────────────────────────
    if not BIN.exists():
        print(f"  📁  Creating : {BIN}")
        BIN.mkdir(parents=True, exist_ok=True)
        BIN.chmod(stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP |
                  stat.S_IROTH | stat.S_IXOTH)
        print(f"  ✅  Created  : {BIN}")
    else:
        print(f"  ✅  Found    : {BIN}")

    # ── Create ~/bin/backup if needed ─────────────────────────────────────────
    if not BACKUP.exists():
        print(f"  📁  Creating : {BACKUP}")
        BACKUP.mkdir(parents=True, exist_ok=True)
        print(f"  ✅  Created  : {BACKUP}")
    else:
        print(f"  ✅  Found    : {BACKUP}")

    # ── Alpha backup — first and eternal ──────────────────────────────────────
    if not ALPHA.exists():
        shutil.copy2(AVE_SRC, ALPHA)
        make_executable(ALPHA)
        print(f"\n  ✝️   Alpha backup (the first): {ALPHA}")
    else:
        print(f"\n  ✝️   Alpha backup already exists: {ALPHA}")

    # ── Handle existing ~/bin/Ave.py ──────────────────────────────────────────
    if AVE_DST.exists():
        print(f"\n  ⚠️   {AVE_DST} already exists.")
        answer = input("     Install new version? [y/N] ").strip().lower()

        if answer != "y":
            print("\n  Installation cancelled. Existing Ave.py unchanged.")
            sys.exit(0)

        # Backup existing version with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = BACKUP / f"Ave.py.{timestamp}"
        shutil.copy2(AVE_DST, backup_path)
        make_executable(backup_path)
        print(f"  💾  Backed up existing: {backup_path}")

    # ── Install ────────────────────────────────────────────────────────────────
    shutil.copy2(AVE_SRC, AVE_DST)
    make_executable(AVE_DST)
    print(f"\n  ✅  Installed : {AVE_DST}")

    # ── Verify ────────────────────────────────────────────────────────────────
    print("\n  Verification:")
    os.system(f"ls -l {AVE_DST}")

    # ── PATH check ────────────────────────────────────────────────────────────
    print()
    check_path()

    print("\n  Ave Maria. Installation complete.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
