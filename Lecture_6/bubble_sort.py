def bubble_sort(num):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                is_swapped = True
    return num


numbers = [int(elem) for elem in input().split()]
print(bubble_sort(numbers))
