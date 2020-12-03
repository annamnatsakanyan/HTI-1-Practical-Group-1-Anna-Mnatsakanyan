students_height = input("enter the numbers: ").split()


def stools(height):
    for i in range(len(height)):
        height[i] = int(height[i])
    sum = 0
    max_elem = height[0]
    for i in range(len(height)):
        if height[i] > max_elem:
            max_elem = height[i]
    for i in range(len(height)):
        sum += max_elem - height[i]
    return sum


print(stools(students_height))
