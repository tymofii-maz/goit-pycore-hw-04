def total_salary(path):
    total = 0
    average = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as salary_file:
            for line in salary_file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Пошкоджений рядок пропущено: {line}")
            average = total / count
            return (total, int(average))
    
    except FileNotFoundError:
        print(f"Файл {path} не існує.")
        quit()
    
    except OSError as error:
        print(f"Помилка при читанні файлу: {error}.")
        quit()
        

total, average = total_salary("task-1/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
