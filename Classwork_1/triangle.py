a = int(input("enter a side of triangle"))
b = int(input("enter a side of triangle"))
c = int(input("enter a side of triangle"))

if a >= b and a >= c:
    c, a = a, c
elif b >= c and b >= a:
    b, c = c, b

if c >= a + b:
    print("Not a triangle")
elif c*c == a*a + b*b:
    print("Right triangle")
elif c*c < a*a + b*b:
    print("Acute triangle")
else:
    print("Obtuse triangle")