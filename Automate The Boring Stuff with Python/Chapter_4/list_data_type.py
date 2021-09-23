# to declare a list we use "[..]"

numbers = [1, 2, 3, 4]
animals = ["cat", "dog", "cow"]
mix = ["bannana", 132, "Australia", 10.21]

# to access an element, we call its index

numbers[0]
animals[2]
mix[3]

# nested lists

two_lists = [["12", "13", "142"], ["John", "Kile", "Tom"]]

print(two_lists[1][1])

# negative indexes

#         -5 -4 -3 -2 -1
my_list = [0, 1, 2, 3, 4]
print(my_list[-1]) # out: 4