def division(number):
    try:
        return 100 / number
    except ZeroDivisionError:
        print("Error: Invalid argument")

print(division(12))
print(division(0))
print(division(1))
print(division(3))