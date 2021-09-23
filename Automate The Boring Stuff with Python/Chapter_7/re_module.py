import re


#                              (Group 1)  (   Group 2     )
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search("Is here 555-666-8888 any phone number?")
print(mo.group(1))  # 555
print(mo.group(2))  # 666-8888
print(mo.group())   # 555-666-8888
print(mo.groups())  # ('555', '666-8888') -> Returns a tuple of multiple values