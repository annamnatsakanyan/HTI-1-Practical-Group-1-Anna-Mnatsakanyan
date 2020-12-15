def stools(height):
    sum = 0
    max_elem = max(students_height)
    for i in range(len(height)):
        sum += max_elem - height[i]
    return sum


students_height = [int(elem) for elem in input("enter the heights: ").split()]

print(stools(students_height))
