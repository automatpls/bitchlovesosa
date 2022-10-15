import math
print("VVedite korni")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

D = b**2 - 4 * a * c
print("Discriminant=", D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(round(x1,1), round(x2,1))
elif D==0:
    x= -b / (2 * a)
    print(x)
else:
    print("Net kornei")