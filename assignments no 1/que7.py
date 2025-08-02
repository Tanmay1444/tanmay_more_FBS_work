#### Write a program to find the roots of quadratic equation.

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

sqrt = ((b**2)-(4*a*c))
res1 = (-b+sqrt**0.5)/2*a
res2 = (-b-sqrt**0.5)/2*a
print(f'First root is: {res1}, Second root is: {res2}')
