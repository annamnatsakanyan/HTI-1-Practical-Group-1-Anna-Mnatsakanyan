year = int(input("enter a year: "))
century = int(year / 100)
if (year % 100) != 0:
    century += 1
print(century)
