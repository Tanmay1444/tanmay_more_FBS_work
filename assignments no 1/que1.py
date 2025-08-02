#### Write a program to calculate the percentage of student based on marks of any 5 subjects

m1 = int(input("Enter the marks of marathi:"))
m2 = int(input("Enter the marks of english:"))
m3 = int(input("Enter the marks of hindi:"))
m4 = int(input("Enter the marks of science:"))
m5 = int(input("Enter the marks of maths:"))

gain_marks = m1 + m2 + m3 + m4 + m5

percentage = (gain_marks / 500)*100
print(f'Total percentage of the student is: {percentage}%')