####Write a program to write a captcha. 
user_id = input("Enter the user id:")
user_pass = input("Enter the password:")

if(user_id == 'Admin' and user_pass == '12345'):
    print("Valid user ")
    import random
    captcha = random.randint(1111, 9999)
    print({captcha})
else:
    print("Invalid user")