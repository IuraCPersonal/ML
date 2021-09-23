while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    password = input("Enter the passwords: ")
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")