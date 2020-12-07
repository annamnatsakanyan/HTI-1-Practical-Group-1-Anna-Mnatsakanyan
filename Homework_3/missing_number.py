def missing_number(num):
    sum = 0
    max_number = max(num)
    for i in range(len(num)):
        sum += num[i]
    _numbers_sum = round((1 + max_number) / 2 * max_number)
    _missing_number = _numbers_sum - sum
    return _missing_number


numbers = [int(elem) for elem in input().split()]
print(missing_number(numbers))
