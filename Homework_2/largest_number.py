number = list(input("enter a number: "))
num = list(number)


def largest_number(largest_num1, largest_num2):
    for i in range(len(largest_num1)):
        largest_num1[i] = int(largest_num1[i])
    for i in range(len(number)):
        largest_num2[i] = int(largest_num2[i])
    largest_num1.sort(reverse=True)
    if largest_num1 == largest_num2:
        print('No')
    else:
        print("Yes")


largest_number(num, number)
