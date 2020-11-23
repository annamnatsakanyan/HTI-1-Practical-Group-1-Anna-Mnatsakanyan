first_num = int(input("enter a first number of progression: "))
second_num = int(input("enter a second number of progression: "))
N = int(input("enter an index of number: "))

diff = second_num - first_num
progression_list: list = [first_num, second_num]
for i in range(N):
    latest_num = progression_list[len(progression_list) - 1] + diff
    progression_list.append(latest_num)

print("The N-est number of progression is: " + str(progression_list[N - 1]))
