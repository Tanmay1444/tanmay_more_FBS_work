### WAP to calculate profit or loss.

cost_price = int(input("Enter the cost price:"))
selling_price = int(input("Enter the sellig price:"))

if(selling_price>cost_price):
    print("Profit")
elif(cost_price>selling_price):
    print("loss")
else:
    print("No profit No loss.")