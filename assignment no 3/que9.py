####Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = int(input("Enter the marks of marathi:"))
m2 = int(input("Enter the marks of english:"))
m3 = int(input("Enter the marks of hindi:"))
m4 = int(input("Enter the marks of maths:"))
m5 = int(input("Enter the marks of science:"))

gain_marks = m1+m2+m3+m4+m5
percentage = (gain_marks/500)*100

if(percentage>90):
    print("First class")
elif(percentage>80 and percentage<91):
    print("second class")
elif(percentage>50 and percentage<81):
    print("Third class")
elif(percentage>35 and percentage<51):
    print("Average")
else:
    print("Fail")