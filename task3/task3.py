# Задание 3
import json
import sys

# Функция чтения JSON файла
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка при чтении JSON из файла {file_path}.")

# Функция записи JSON файла
def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise Exception(f"Ошибка при записи JSON в файл {file_path}: {e}")

# Функция создания словаря значений по id из values.json
def create_values_dict(values_list):
    return {item['id']: item['value'] for item in values_list}

# Рекурсивная функция для заполнения поля value в структуре tests.json, используя словарь значений
def fill_values(test, values_dict):
    if 'id' in test and test['id'] in values_dict:
        test['value'] = values_dict[test['id']]
    
    if 'values' in test:
        for subtest in test['values']:
            fill_values(subtest, values_dict)

def main():
    if len(sys.argv) != 4:
        print("Используйте - python task3.py values.json tests.json report.json")
        return

    # Получаем пути к файлам из аргументов командной строки
    values_file = sys.argv[1]
    tests_file  = sys.argv[2]
    report_file = sys.argv[3]

    try:
        # Читаем данные из файлов
        values_data = read_json(values_file)
        tests_data = read_json(tests_file)

        # Создаем словарь значений по id
        values_dict = create_values_dict(values_data['values'])

        # Заполняем поля value в структуре tests.json
        for test in tests_data['tests']:
            fill_values(test, values_dict)

        # Записываем результат в report.json
        write_json(tests_data, report_file)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
