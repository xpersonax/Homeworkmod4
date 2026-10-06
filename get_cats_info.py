def get_cats_info(path):
    """Читає файл з котами і повертає список словників
    [{"id": ..., "name": ..., "age": ...}, ...].
    Якщо файл відсутній або пошкоджений — повертає порожній список.
    """
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except ValueError:
        print(f"Файл '{path}' пошкоджений: невірний формат рядка.")
        return []
    return cats


if __name__ == "__main__":
    print(get_cats_info("cats_file.txt"))
