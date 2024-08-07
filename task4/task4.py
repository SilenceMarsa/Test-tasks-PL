# Задание 4
import sys

# Функция для чтения массива чисел из файла
def read_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except ValueError:
        raise ValueError(f"Ошибка при чтении чисел из файла {file_path}. Убедитесь, что данные корректны.")

# Функция для нахождения минимального количества ходов для приведения всех элементов к одному числу
def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]  # Находим медиану массива
    print("Среднее значение массива", median)
    return sum(abs(num - median) for num in nums)  # Считаем сумму разниц чисел с медианой по модулю

def main():
    if len(sys.argv) != 2:
        print("Используйте - python task4.py nums.txt")
        return

    # Получаем путь к файлу из аргументов командной строки
    nums_file = sys.argv[1]

    try:
        # Читаем числа из файла
        nums = read_numbers(nums_file)

        # Находим минимальное количество ходов
        result = min_moves(nums)

        # Выводим результат в консоль
        print(result)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
