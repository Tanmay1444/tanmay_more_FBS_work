n = int(input("Enter n: "))

total = 0
for i in range(n+1):
    total += 2**i

print("Sum =", total)