def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    
    print(left, right)
    return merge(left, right)


def merge(left, right):
    sort_numbers = []
    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            sort_numbers.append(left[l_index])
            l_index += 1
        else:
            sort_numbers.append(right[r_index])
            r_index += 1
    sort_numbers += left[l_index:] + right[r_index:]

    return sort_numbers


numbers = [5, 7, 3, 8, 1, 4, 6, 2]
print(merge_sort(numbers))
