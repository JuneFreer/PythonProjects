#! python3
# phoneAndEmail.py Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                   # area code
    (\s|-|\.)?                           # seperater
    (\d{3})                              # first 3 digits
    (\s|-|\.)                            # seperater
    (\d{4})                              # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?       # extension
    )''', re.VERBOSE)


# create email regex
emailRegex = re.compile('''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste()) # pyperclip.paste()函数将取得一个 字符串，内容是剪贴板上的文本
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0], groups[2], groups[4]])
    if groups[5] != '':
        phoneNum += ' x' + groups[5]
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
