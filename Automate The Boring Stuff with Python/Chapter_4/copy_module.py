import copy

spam = ['a', 'b', 'c', 'd']
spam2 = copy.copy(spam)
spam2[0] = 'A'

print(spam)
print(spam2)