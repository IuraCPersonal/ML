import re

phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
text = input()
mo = phone_number_regex.search(text)

# -- .group() --

print(mo.group()) # out: 415-555-4545

# -- .groups() --

#print(mo.groups()) # out: ('415', '555-4545')

