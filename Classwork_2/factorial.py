num = int(input("enter a number: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("factorial of the " + str(num) + "is " + str(factorial))