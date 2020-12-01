num = int(input("enter a number"))
product = 1
last_n = num % 10
while num // 10 != 0:
    digit = num % 10
    if digit != 0:
        product = product * digit
    num = num // 10

product = product * num
print(product)
