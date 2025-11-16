# 🗂️ Files Organizer

Organize files from a source directory into categorized folders by extension. Handy for cleaning downloads folders, USB drives, or bulk reorganization tasks.

---

- ✅ Categorizes common file types (images, documents, video, audio, archives, code, etc.)
- ✅ Moves files into destination folders with safe creation of directories
- ✅ Windows-friendly paths and examples
- ✅ Simple to extend with new categories

---

## Table of contents

- 🔧 Requirements
- 🚀 Quick Start (Windows)
- 🧩 Usage (library + script)
- 🛠️ Configuration & extension
- 🧪 Tests
- 🧾 License
- 🤝 Contributing
- ⚠️ Safety & notes

---

## 🔧 Requirements

- Python 3.8+

No external dependencies required for the core script, but consider running inside a virtualenv for safety.

---

## 🚀 Quick Start (Windows)

Example: organize files from `C:\Users\user\suip_files` into `D:\Suip_Organized\Organized_files`:

```powershell
cd 'c:\Users\user\Desktop\Python_Pro_BootCamp\Web_Dev\CodeAlpha\Files_Organizer'
python -c 'from main import organize_files_by_extension; organize_files_by_extension(r"C:\User\user\suip_files", r"D:\Suip_Organized\Organized_files")'
```

Or run via your package's `__main__` wrapper if set up:

```powershell
python -m Files_Organizer
```

---

## 🧩 Usage (library)

Import the main function:

```python
from main import organize_files_by_extension

organize_files_by_extension(source_dir=r'C:\Users\me\Downloads', destination_dir=r'C:\Organized')
```

Function signature:

```python
def organize_files_by_extension(source_dir: str, destination_dir: str) -> None:
    ...
```

- Moves files (not copies) by default.
- Preserves filenames; if collisions are a concern, extend the script to append indexes or timestamps.

---

## 🛠️ Configuration & extension

- FILE_CATEGORIES mapping is defined in `main.py`. Add or change categories as needed:

```python
FILE_CATEGORIES['ebooks'] = {'.epub', '.mobi', '.azw3'}
```

- To change behavior (copy instead of move), replace `shutil.move` with `shutil.copy2` and update logging.

- Consider adding:
  - Dry-run mode (display actions but don't move)
  - Collision handling (rename duplicates)
  - Recursive traversal (currently top-level only; you can extend with os.walk)

---

## 🧪 Tests

- Create tests that:
  - Build a temporary directory with sample files of different extensions
  - Run `organize_files_by_extension` and assert files moved to expected folders
  - Test error conditions: missing source dir, permission errors (use temp dirs and adjust perms)

Use pytest and tempfile fixtures:

```python
def test_organize(tmp_path):
    src = tmp_path / 'src'
    dst = tmp_path / 'dst'
    src.mkdir()
    (src / 'a.txt').write_text('hello')
    organize_files_by_extension(str(src), str(dst))
    assert (dst / 'documents' / 'a.txt').exists()
```

---

## 🧾 License

MIT License — see full text below.

```
MIT License

Copyright (c) 2025 Theophilus Asamoah

Permission is hereby granted, free of charge, to any person obtaining a copy

...
```
[`See License`](./LICENSE)

---

## 🤝 Contributing

- Add issues for new categories or bugs.
- Submit PRs with tests and clear commit messages.
- Keep changes backwards compatible: preserve the default categories and move behavior.

---

## ⚠️ Safety & notes

- The script moves files — ensure you have backups or test on a copy of your directory first.
- For large directories, consider adding logging and progress output.
- If you need to preserve metadata timestamps, use `shutil.copy2` followed by `os.remove` (for a move-like behavior while preserving metadata).
