from pathlib import Path
def get_cats_info(path: str | Path) -> list[dict]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Пропускаємо порожні рядки
                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                except ValueError:
                    print(f"Пошкоджений рядок пропущено: {line}")
                    continue

                cat = {"id": cat_id, "name": name, "age": age}
                cats.append(cat)

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except OSError as error:
        print(f"Не вдалося прочитати файл: {error}")
        return []

    return cats

if __name__ == "__main__":
    cats_file = Path(__file__).parent / "cats.txt"
    cat_info = get_cats_info(cats_file)
    print(cat_info)
