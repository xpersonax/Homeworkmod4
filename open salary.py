def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                parts = clean_line.split(",")
                salary = int(parts[1])
                count += 1
                total += salary
        average = total / count
        return total, average
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total, average = total_salary("несуществующий_файл.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")