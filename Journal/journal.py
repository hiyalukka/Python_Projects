import storage

MENU = """
1. Write entry
2. Read recent
3. Search
4. Exit
"""

def write():
    text = input("Entry: ").strip()
    if not text:
        return print("Nothing to save.")
    storage.save(text)
    print("Saved.")

def read():
    entries = storage.load()
    if not entries:
        return print("No entries yet.")
    for e in entries[-5:]:
        print(e, "\n")

def search():
    results = storage.search(input("Keyword: "))
    if not results:
        return print("No results.")
    for e in results:
        print(e, "\n")

ACTIONS = {"1": write, "2": read, "3": search}

def main():
    while (choice := input(MENU).strip()) != "4":
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Enter 1–4.")

if __name__ == "__main__":
    main()