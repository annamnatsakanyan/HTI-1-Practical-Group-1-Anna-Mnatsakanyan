num = int(input("enter a number: "))



def is_prime(num):
    isprime = True
    for i in range(2, num // 2+1):
        if num % i == 0:
            isprime = False
            break

    return isprime


if is_prime(num):
    print("Yes")
else:
    print("No")
