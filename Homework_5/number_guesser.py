count = 0


def number_guesser(start, end):
    mid_num = (start + end) // 2
    print("is the number ", mid_num, "?")

    answer = int(input("enter answer: "))
    global count
    while count <= 10:
        count += 1
        if answer == 0:
            return "you find number"
        elif answer == -1:
            return number_guesser(start, mid_num - 1)
        else:
            return number_guesser(mid_num + 1, end)
    return 'you cheated in one of the steps'


saved_number = int(input("enter number to save: "))
print(number_guesser(0, 1000))
