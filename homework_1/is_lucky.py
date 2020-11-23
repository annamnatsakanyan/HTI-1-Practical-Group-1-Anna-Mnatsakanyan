num = int(input("enter the number: "))
ticket_number = list(map(int, str(num)))
sum_first_middle = 0
sum_second_middle = 0
length = len(ticket_number)
middle_length = length // 2
for i in range(middle_length, length):
    sum_first_middle += ticket_number[i]
for i in range(0, middle_length):
    sum_second_middle += ticket_number[i]
if sum_first_middle == sum_second_middle:
    print("Yes")
else:
    print("No")
