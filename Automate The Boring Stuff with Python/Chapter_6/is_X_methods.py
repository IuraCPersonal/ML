# isalpha() -> only letters
# isalnum() -> only letters and numbers
# isdecimal() -> only numeric chars
# isspace() -> only space, tabs, newlines
# istitle() -> Title / My Name / Hello

print('hello'.isalpha()) # out: True

print('hello'.isalnum()) # out: True
print('hello121'.isalnum()) # out: True

print('word'.isdecimal()) # out: False
print('1412'.isdecimal()) # out: True
# print(131.isdecimal()) -> syntax error

print('     '.isspace()) # out: True

print('Hello'.istitle()) # out: True
print('Hello World'.istitle()) # out: True
