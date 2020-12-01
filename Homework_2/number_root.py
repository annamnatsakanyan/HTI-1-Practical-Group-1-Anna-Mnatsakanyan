num = int(input("enter a number: "))


def number_root(num):
    sum = 0
    while num / 10 != 0:
        elem = num % 10
        sum += elem
        num //= 10
    if sum > 9:
        sum = (sum % 10) + (sum // 10)

    return sum


print(number_root(num))
