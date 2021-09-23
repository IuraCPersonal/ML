username = ''
password = ''

logging_option = input("Log In or Sing Up: ")
if logging_option == "1":
	username = input("Username: ")
	password = input("Password: ")
	with open('manager.txt') as manager:
		for line in manager:
			if line == username:
				print("Success!")
			else:
				pass
