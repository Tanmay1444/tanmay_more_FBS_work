#### write a program to accept distance in km and convert it into meters and centimeters.

K = int(input("Enter the distance in km:"))

meters = K * 1000
centimeters = meters*100

print(f'After conversion distance in meter is:{meters}meters.')
print(f'After conversion distance in centimeters is:{centimeters}centimeters.')