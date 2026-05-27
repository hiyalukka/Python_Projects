import os
from datetime import datetime

FILE = "entries.txt"

def save(text):
    with open(FILE, "a") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M}]\n{text.strip()}\n---\n")

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        blocks = f.read().split("---\n")
    return [b.strip() for b in blocks if b.strip()]

def search(keyword):
    return [e for e in load() if keyword.lower() in e.lower()]