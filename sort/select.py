def select_sort(numbers):
    for i in range(len(numbers) - 1):
        min_num = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_num]:
                min_num = j
        numbers[i], numbers[min_num] = numbers[min_num], numbers[i]
        print(numbers)


numbers = [5, 7, 3, 8, 1, 4, 6, 2]
select_sort(numbers)
print(f"\n{numbers}")
