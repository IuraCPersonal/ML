birthdays = {'Iura': '29 Martie'}

while True:
    name = input("Enter a name: ")
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name])
    else:
        new_birthday = input("I don't have a birthday for " + name + ". Enter their birthday: ")
        birthdays[name] = new_birthday
        print('Database updated.')