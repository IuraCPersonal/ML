_userName = "Zero"
_password = "29032001"

while True:
    print("Enter your user name")
    userName = input()
    if userName != _userName:
        continue 
    print("Hello " + userName + '. Please, enter the password!')
    password = input()
    if password == _password:
        break

print("Access granted.") 