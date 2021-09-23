spam = 'Hello'

# -- upper() --

print(spam.upper()) # out: HELLO

# -- lower() --

print(spam.lower()) # out: hello

# -- islower() --

print(spam.islower()) # out: False

# -- isupper() --

print(spam.isupper()) # out: False

# -- startswith() --

print(spam.startswith('Hel')) # out: True

# -- endswith() --

print(spam.endswith('lo')) # out: True

# -- join() --

my_array = ['cat', 'dog', 'plane']
print(', '.join(my_array)) # out: cat, dog, plane

# -- split() --

my_string = 'My name is Zero.'
print(my_string.split())

# -- center() --

print(spam.center(20))
print(spam.center(20, '-'))

# -- strip() --

print('      Hi      '.strip()) # out: Hi
# the white space is removed

# use of methods

mood = input("How are you? ")
if mood.lower() == "good": # even if the input is GOOd, the condition will run
    print("I am good too.")
else:
    print("This is bad")
