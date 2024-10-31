# // ECS M012, Group 5 Decode File Function
# Vincent Gallagher
# Decode function will loop through the file provided
# in binary and loop through every char by tracking
# the current spot. Make sure row isnt empty, then
# add the char to the string 'newfile' and add one
# to the currspot variable. repeat this for long and
# short numbers. continue until currspot < len of the
# file provided.

def decode(fn="BinOutput.txt"):

    with open(fn, 'r') as f:
        fn = f.read()

    fn = fn.split(".")[1]

    # WHILE THE FILE ISNT DECODED // LOOP
    currentspot = 0 # where we're at in the oldfile
    newfile = '' # the newfile str

    # LOOP THROUGH ALL NUMBERS BELOW
    while currentspot < len(fn): # while the cursor < len
        if fn[currentspot] == '0': # SHORT NUM
            char_in_binary = fn[currentspot:currentspot + ShortNum]
            # start at curr spot up to 5 to get bin num
            row_index = XL[XL['Bin'] == char_in_binary].index
            # get the row
        elif fn[currentspot] == '1': # LONG NUM
            char_in_binary = fn[currentspot:currentspot + LongNum]
            # start at curr spot up to 7 to get bin num
            row_index = XL[XL['Bin'] == char_in_binary].index
            # get the row

        else:
            currentspot += 1
            continue

        # deals with replaced values and makes sure they are good
        if not row_index.empty:
            row = row_index[0]
            the_char = XL.loc[row, 'Char']
            newfile += replacements.get(the_char, the_char)
            currentspot += ShortNum if fn[currentspot] == '0' else LongNum

    TextOutput = open("TextOutput.txt")
    # creates file 
    with open('TextOutput.txt', 'w') as fileopen:
        fileopen.write(newfile)
