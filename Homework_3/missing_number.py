def missing_number(num):
    n = len(num) + 1
    _missing_number = n * (n + 1) // 2 - sum(num)
    return _missing_number


numbers = [int(elem) for elem in input("enter the numbers: ").split()]
print(missing_number(numbers))
