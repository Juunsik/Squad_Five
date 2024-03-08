def insert_sort(numbers):
    for i in range(1, len(numbers)):
        while i - 1 >= 0:
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
            i -= 1
        print(numbers)


numbers = [5, 7, 3, 8, 1, 4, 6, 2]
insert_sort(numbers)
print(numbers)
