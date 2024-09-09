def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Проход по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Условие сортировки зависит от выбранного направления
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел: "))

    # Вводим числа с клавиатуры
    numbers = []
    for i in range(n):
        number = int(input(f"Введите число {i + 1}: "))
        numbers.append(number)

    # Запрашиваем направление сортировки
    direction = input("Введите направление сортировки (возрастание/убывание): ").strip().lower()

    # Определяем, по возрастанию или по убыванию будет сортировка
    if direction == "возрастание":
        ascending = True
    elif direction == "убывание":
        ascending = False
    else:
        print("Некорректное направление сортировки. По умолчанию будет выполнена сортировка по возрастанию.")
        ascending = True

    # Сортируем список с помощью алгоритма сортировки пузырьком
    bubble_sort(numbers, ascending)

    # Выводим отсортированные числа
    print("Отсортированные числа:", numbers)