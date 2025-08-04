#### Write a program to check if user has entered correct userid and password.
user_id = input("Enter the user id:")
user_pass = input("Enter the password:")

if(user_id == 'Admin' and user_pass == '12345'):
    print("Valid user ")
else:
    print("Invalid user")