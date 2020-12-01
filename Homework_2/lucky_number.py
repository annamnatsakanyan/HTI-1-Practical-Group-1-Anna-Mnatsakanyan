num = input("enter a number: ")
num = list(num)


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

    return sum_evens, sum_odds


lucky_number(num)
