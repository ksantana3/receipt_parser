import os
import sys
import string
import re
from sys import platform
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import easygui

image_upload = easygui.fileopenbox()

istring = pytesseract.image_to_string(f'{image_upload}')
# istring = pytesseract.image_to_string(Image.open(f'{test_print}'))
# lines = istring
lines = istring.split('\n')
# with open("parseddata.txt", 'r') as file_in:
#     lines = file_in.readlines()
# lines = "".join(lines).split('\n')
alpha = string.ascii_letters+string.whitespace
num = string.digits+string.whitespace+string.punctuation
word_list = ["coupon", "total", "savings", "price", "phone", "tax", "sales", "deposit"]
receipt = []
for line in lines:
    if len(line)>5:
        receipt.append(line.rstrip(alpha).lstrip(num))
        if len (receipt[len(receipt)-1]) < 5: 
            receipt.pop()
        elif any(s in line.lower() for s in word_list):
            receipt.pop()
        elif not re.search(r'(\.[0-9]{2})$', line.rstrip(alpha)):
            receipt.pop()


for l in receipt:
    print(l)
# print(lines)
