def get_cats_info(path):
    result = []

    try:
        with open(path, "r", encoding="utf-8") as cat_info_txt:
            for line in cat_info_txt:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                except ValueError:
                    print(f"Пошкоджений рядок пропущено: {line}")
                    continue

                cat = {"id": cat_id, "name": name, "age": age}

                result.append(cat)

    except FileNotFoundError:
        print(f"Файл {path} не існує.")
        return []

    except OSError as error:
        print(f"Помилка при читанні файлу: {error}.")
        return []

    return result


cat_info = get_cats_info("cats.txt")
print(cat_info)