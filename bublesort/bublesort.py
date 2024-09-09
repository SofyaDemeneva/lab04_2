def bubble_sort(arr):
    n = len(arr)
    # Проход по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Меняем элементы местами, если они в неправильном порядке
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    # Запрашиваем у пользователя количество чисел
    n = int(input("Введите количество чисел: "))

    # Вводим числа с клавиатуры
    numbers = []
    for _ in range(n):
        number = int(input(f"Введите число {_ + 1}: "))
        numbers.append(number)

    # Сортируем список с помощью алгоритма сортировки пузырьком
    bubble_sort(numbers)

    # Выводим отсортированные числа
    print("Отсортированные числа:", numbers)
