spam = {'color': 'red', 'age': 42}

# -- values() --

for v in spam.values():
    print(v)

# -- keys() --

for k in spam.keys():
    print(k)

# -- items() --

for i in spam.items():
    print(i)

# -- get() --

picnic_items = {'apples': 5, 'cups': 2}
print('There are ' + str(picnic_items.get('cups', 0)) + ' cups.')
print('There are ' + str(picnic_items.get('eggs', 12)) + ' eggs.')

# -- setdefault() -- 

spam.setdefault('height', 1.80)
print(spam)