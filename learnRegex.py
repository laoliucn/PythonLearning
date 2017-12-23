#! python3
# learnRegex.py - Finds phone numbers and email address on the clipboard.

import re, pyperclip

# phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phoneNumberRegex.search('My number is 415-555-4242 or 415-446-5362')
# listAll = phoneNumberRegex.findall('My number is 415-555-4242 or 415-446-5362')
# print('Phone number found: ' + mo.group())
# print('multinumber found: ', listAll)

# agentNameRegex = re.compile(r'Agent (\w{2})\w*', re.IGNORECASE)
# subResult = agentNameRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
# print(subResult)

#Create phone regex.
# phoneRegex = re.compile(r'''
#     (\d{3}|\(\d{3}\))?          #area code
#     (\s|-|\.)?                  #separator
#     (\d{3})                     #first 3 digits
#     (\s|-|\.)                   #separator
#     (\d{4})                     #last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
#     )''', re.VERBOSE)

# #Create email regex.
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+           #username
#     @                           #@ symbol
#     [a-zA-Z0-9.-]+              #domain name
#     (\.[a-zA-Z]{2,4})           #dot-something
#     )''', re.VERBOSE)

# #Find matches in clipboard text.
# text = pyperclip.paste()

datePattern = re.compile( r'''^(.*?) # all text before the date 　 
        ((0|1)?\d)- # one or two digits for the month 　 
        ((0|1|2|3)?\d)- # one or two digits for the day 　 
        ((19|20)\d\d) # four digits for the year 　 
        (.*?)$ # all text after the date
        ''', re.VERBOSE)

samplefile = 'spam4-5-1984.txt'
mo = datePattern.search(samplefile)
print(mo.groups())
print(mo.group(1))
print(mo.group(2))
print(mo.group(4))
print(mo.group(6))
print(mo.group(8))
print(mo.group(0))
# print(mo.group(1))
# print(mo.group(1))
