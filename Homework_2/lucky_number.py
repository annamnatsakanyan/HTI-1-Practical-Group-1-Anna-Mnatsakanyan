numbers = input("enter a number: ")
numbers = list(numbers)


def lucky_number(num):
    sum_odds = 0
    sum_evens = 0
    for i in range(len(num)):
        if i % 2 != 0:
            sum_odds += int(num[i])
        else:
            sum_evens += int(num[i])
    if sum_odds == sum_evens:
        print("Yes")
    else:
        print("No")


lucky_number(numbers)
