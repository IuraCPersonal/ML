# tuples are made using () and tuples are immutable

spam = (0, 1, 2, 3)

# spam[1] = 122 -> error

# list() and tuple()

spam_list = list(spam)
spam_list[0] = 121
print(spam_list)