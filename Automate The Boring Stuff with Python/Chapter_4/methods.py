# -- index() --

spam = ['hello', 'hi', 'ola', 'ciao']
print(spam.index('hello'))

# -- append() --

spam.append('bonjour') # adds '..' to the end of the list
print(spam)

# -- insert() --

spam.insert(1, 'kalimera') # adds '..' before the index i
print(spam)

# -- remove() --

spam.remove('ola')
print(spam)

# if the are two elements the same, only the first one will be removed

string = ['apple', 'samsung', 'xiaomi', 'apple']
string.remove('apple')
print(string)

# -- sort() --

numbers = [3, -2 , 5, 10, 142, -921]
numbers.sort()
print(numbers)

numbers.sort(reverse=True) # sort the values in reverse order
print(numbers)