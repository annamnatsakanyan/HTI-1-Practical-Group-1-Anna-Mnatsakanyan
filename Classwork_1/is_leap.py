year = int(input("enter a year"))

if year % 4 != 0:
    print("No")

elif year % 100 != 0:
    print('  Yes')
elif year % 400 == 0:
    print("Yes")
else:
    print("No")
