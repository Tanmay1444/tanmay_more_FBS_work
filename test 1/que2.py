#### write a program to calculate simple interest based on Principal, Rate, and Time.

P = int(input("Enter the Principal amount:"))
R = int(input("Enter the Rate:"))
T = int(input("Enter the Time:"))

Simple_int = (P*R*T)/100

print(f'Simple interest is:{Simple_int}')