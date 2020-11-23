num = input("enter the numbers: ")
num_list = num.split()
new_list = []

for i in range(len(num_list) - 1):
    adjacent_result = int(num_list[i]) * int(num_list[i + 1])
    new_list.append(adjacent_result)

print("maximum adjacent elements product is: " + str(max(new_list)))
