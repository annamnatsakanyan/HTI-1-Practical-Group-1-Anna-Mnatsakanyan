n = int(input('enter a number: '))
list_num = []
for num in range(1, n + 1):
    count = 0
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            count += 1
            break
    if count == 0 and num != 1:
        list_num.append(num)


def goldbach_conjecture():
    for elem in range(len(list_num)):
        for j in range(len(list_num)):
            if list_num[elem] + list_num[j] == n:
                print(list_num[elem], list_num[j])
                return


goldbach_conjecture()
