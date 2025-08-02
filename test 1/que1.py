#### write a program to find the area and perimeter of following figure.

l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))
r = int(input("Enter the radius of semicircle:"))

area = (l*b) + (1/2*3.14*r**2)

perimeter = (2*l+b) + (3.14*r)


print("Area:", round(area, 2))
print("Perimeter:", round(perimeter, 2))