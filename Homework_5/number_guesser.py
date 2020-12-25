def number_guesser(start, end, count=0):
    mid_num = (start + end) // 2
    print("is the number ", mid_num, "?")

    answer = int(input("enter answer: "))
    while count <= 10:
        if answer == 0:
            return "you find number"
        elif answer == -1:
            return number_guesser(start, mid_num - 1, count+1)
        else:
            return number_guesser(mid_num + 1, end, count+1)
    return 'you cheated in one of the steps'


saved_number = int(input("enter number to save: "))
print(number_guesser(0, 1000))
