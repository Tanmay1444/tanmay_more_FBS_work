# WAP to input any alphabet and check whether is is vowel or consonant.

alpha = input("Enter the alphabet:")

if(alpha in 'aeiouAEIOU'):
    print("{alpha} is vowel.")
else:
    print("It is consonant.")