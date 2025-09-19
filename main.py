import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(items: list[dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def add(task: str) -> None:
    items = load_todos()
    items.append({"task": task, "done": False})
    save_todos(items)


def list_items() -> None:
    items = load_todos()
    if not items:
        print("Bo'sh.")
        return
    for i, item in enumerate(items, 1):
        mark = "[x]" if item["done"] else "[ ]"
        print(f"{i}. {mark} {item['task']}")


def toggle(index: int) -> None:
    items = load_todos()
    if 1 <= index <= len(items):
        items[index - 1]["done"] = not items[index - 1]["done"]
        save_todos(items)
    else:
        print("Noto'g'ri indeks")


def remove(index: int) -> None:
    items = load_todos()
    if 1 <= index <= len(items):
        items.pop(index - 1)
        save_todos(items)
    else:
        print("Noto'g'ri indeks")


def main() -> None:
    print("Todo: buyruqlar add, list, done <n>, del <n>, exit")
    while True:
        cmd = input("> ").strip()
        if cmd in {"exit", "quit", "q"}:
            break
        if cmd == "list":
            list_items()
        elif cmd.startswith("add"):
            task = cmd[3:].strip() or input("Vazifa: ")
            add(task)
        elif cmd.startswith("done"):
            try:
                n = int(cmd.split()[1])
                toggle(n)
            except Exception:
                print("Foydalanish: done 2")
        elif cmd.startswith("del"):
            try:
                n = int(cmd.split()[1])
                remove(n)
            except Exception:
                print("Foydalanish: del 2")
        else:
            print("Noma'lum buyruq")


if __name__ == "__main__":
    main()


