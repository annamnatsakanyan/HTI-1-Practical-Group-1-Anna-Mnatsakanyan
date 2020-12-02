def selection_sort(num):
    for i in range(len(num) - 1):
        min_index = i
        for j in range(i + 1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num


numbers = [int(elem) for elem in input().split()]
print(selection_sort(numbers))
