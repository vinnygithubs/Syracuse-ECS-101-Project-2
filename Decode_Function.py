# // ECS M012, Group 5 Decode File Function
from importlib.resources import contents
from operator import truediv
import pandas as pd
#
XL = pd.read_excel('P2M012_G5.xlsx', dtype=str)
Char = list(XL['Char'])
Bin = list(XL['Bin'])
#
shortnum=5
longnum=7
# sample=10010010000000101011001100011110101011011001101111 < - IGNORE (TESTING)
#
with open('samplefile.txt', 'r') as fileopen:
    oldfile = fileopen.read()
    print("Encoded:", oldfile)

# Decode function will loop through the file provided
# in binary and loop through every char by tracking
# the current spot. Make sure row isnt empty, then
# add the char to the string 'newfile' and add one
# to the currspot variable. repeat this for long and
# short numbers. continue until currspot < len of the
# file provided.

def decode_Start(info:str):
    # WHILE THE FILE ISNT DECODED // LOOP
    currentspot=0 # where we're at in the oldfile
    newfile = '' # the newfile str

    # LOOP THROUGH ALL NUMBERS BELOW
    while currentspot < len(info): # while the cursor/spot is less than the length possible (of info)
        if info[currentspot] == '0': # SHORT NUM
            char_in_binary = info[currentspot:currentspot + shortnum] # start at curr spot up to 5 to get bin num
            row_index = XL[XL['Bin'] == char_in_binary].index # get the row

            if not row_index.empty:  # make sure row isnt empty
                newfile += the_char # add char
                currentspot += shortnum  # Increase currspot for next loop
                continue

        elif info[currentspot] == '1': # LONG NUM
            char_in_binary = info[currentspot:currentspot + longnum]
            row_index = XL[XL['Bin'] == char_in_binary].index
            # NO COMMENTS BECAUSE IT IS PRATICALLY THE SAME, BESIDE += longnum
            if not row_index.empty:
                newfile += the_char
                currentspot += longnum
                continue

    return newfile

new_content = decode_Start(oldfile)
with open('samplefile.txt', 'w') as fileopen:
    fileopen.write(new_content)
print("Decoded:", new_content)
