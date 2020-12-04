def insertion_sort(num):
    for i in range(1, len(num)):
        value_to_insert = num[i]
        j = i - 1
        while j >= 0 and value_to_insert < num[j]:
            num[j + 1], num[j] = num[j], num[j + 1]
            j -= 1


numbers = [int(elem) for elem in input("enter the numbers: ").split()]
insertion_sort(numbers)

print(numbers)

