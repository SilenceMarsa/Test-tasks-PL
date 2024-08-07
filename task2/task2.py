# Задание 2
import sys

# Функция чтения центра и радиуса окружности из файла
def read_circle(file_path):
    with open(file_path, 'r') as file:
        cx, cy = map(float, file.readline().split())  # Читаем координаты центра окружности
        radius = float(file.readline().strip())      # Читаем радиус окружности
    return cx, cy, radius

# Функция чтения координат точек из файла
def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            px, py = map(float, line.split())  # Читаем координаты каждой точки
            points.append((px, py))            # Добавляем точку в список
    return points

# Функция проверки положения точки относительно окружности
def check_point(cx, cy, radius, px, py):
    dist_sq = (px - cx) ** 2 + (py - cy) ** 2  # Вычисляем квадрат расстояния от точки до центра окружности
    radius_sq = radius ** 2                    # Квадрат радиуса окружности
    if dist_sq < radius_sq:
        return 1  # Точка внутри окружности
    elif dist_sq == radius_sq:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

def main():
    if len(sys.argv) != 3:
        print("Используйте - python task2.py circle.txt points.txt")
        return

    # Получаем пути к файлам из аргументов командной строки (имя файла указаны при запуске)
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        # Читаем данные из файлов
        cx, cy, radius = read_circle(circle_file)
        points = read_points(points_file)

        # Проверяем каждую точку и выводим результат
        for px, py in points:
            result = check_point(cx, cy, radius, px, py)
            print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
