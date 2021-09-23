cat_names = []
while True:
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name] # list concatenation

print(cat_names)