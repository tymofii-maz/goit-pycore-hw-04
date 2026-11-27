from pathlib import Path

def total_salary(path: str | Path) -> tuple[int | float, int | float]:
    """
    Читає файл із зарплатами і повертає (загальна сума, середня зарплата).

    Кожен рядок файлу виглядає так:  Alex Korp,3000
    Якщо файлу немає або в ньому немає даних, повертає (0, 0).
    """
    salaries = []
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Пропускаємо порожні рядки
                if not line:
                    continue

                try:
                    name, salary = line.split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Пошкоджений рядок пропущено: {line}")

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except OSError as error:
        print(f"Не вдалося прочитати файл: {error}")
        return 0, 0

    count = len(salaries)

    # Порожній файл: ділити на 0 не можна
    if count == 0:
        return 0, 0

    total = sum(salaries)
    average = total / count

    # 2000.0 -> 2000, щоб вивід був як у прикладі
    if average == int(average):
        average = int(average)

    return total, average

if __name__ == "__main__":
    salary_file = Path(__file__).parent / "salary.txt"

    total, average = total_salary(salary_file)
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )
