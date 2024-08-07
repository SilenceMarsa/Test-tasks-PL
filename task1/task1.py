# Задание 1

def circular_array_path(n, m):
    # Массив с элементами от 1 до n
    array = list(range(1,n + 1))

    # Результирующий путь
    path = []

    # Начальный индекс/позиция
    index = 0
    
    # Начало движения по круговому массиву
    while True:
        # Добавляем начальный элемент интервала в путь
        path.append(array[index])
        
        # Рассчитываем следующий индекс, добавляя интервал m
        index = (index + m - 1) % n
        
        # Когда вернулись к первому элементу, останавливаемся
        if index == 0:
            break
        
    return path

# Ввод n и m
n = int(input('input n: '))
m = int(input('input m: '))
# Вывод 
print(circular_array_path(n, m)) 
