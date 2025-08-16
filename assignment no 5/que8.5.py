x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

i = 1
S = 0
while i <= n:
    term = ((-1)**(i+1)) * (x**i) / (2*i - 1)
    S += term
    i += 1

print("Sum =", S)