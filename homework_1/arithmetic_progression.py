first_num = int(input("enter a first number of progression: "))
second_num = int(input("enter a second number of progression: "))
N = int(input("enter an index of number: "))

diff = second_num - first_num
N_est_num = first_num + (N - 1) * diff
print("The N-est number of progression is: " + str(N_est_num))
