def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        print(numbers)  # 정렬되는 과정


numbers = [5, 7, 3, 8, 1, 4, 6, 2]
bubble_sort(numbers)
print(f'\n{numbers}')
