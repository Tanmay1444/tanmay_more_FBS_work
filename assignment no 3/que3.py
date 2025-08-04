ang1 = int(input("Enter the first angle:"))
ang2 = int(input("Enter the second angle:"))
ang3 = int(input("Enter the third angle:"))

sum = ang1 + ang2 + ang3

if(sum == 180):
    print("Triangle is valid.")
else:
    print("Triangle is invalid.")