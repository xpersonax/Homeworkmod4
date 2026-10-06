def total_salary(path):
    """Повертає кортеж (загальна сума, середня зарплата) з файлу.

    Кожен рядок файлу: "Прізвище Ім'я,зарплата".
    Якщо файл відсутній, пошкоджений або порожній — повертає (0.0, 0.0)
    і виводить повідомлення про помилку.
    """
    total = 0.0
    count = 0
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                total += float(line.split(",")[1])
                count += 1
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return 0.0, 0.0
    except (IndexError, ValueError):
        print(f"Файл '{path}' пошкоджений: невірний формат рядка.")
        return 0.0, 0.0

    if count == 0:
        return 0.0, 0.0
    return total, total / count


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
