# Ashley Gottorff
# The same function compares the two text files and
# creates an errors file if the texts are different.
def same(fn1, fn2 = "TextOutput.txt"):
    f1 = open(fn1)
    text1 = f1.read()
    f1.close()
    print(text1)
# Reading in the content of text 2.
    f2 = open(fn2)
    text2 = f2.read()
    f2.close()
    print(text2)

    if text1 == text2:
        print("Identical Files")
    else:
        print("Different Files")
        # Create errors file.
        errors = open("Errors.txt", "w")
        # Write the lengths of the input files to
        # the errors file.
        L1 = len(text1)
        L2 = len(text2)
        errors.write("file 1: %d and file 2: %d\n" %(L1, L2))
        # Find the shortest length of the
        # two text strings.
        m = min(L1, L2)
        # Loop through all the functions
        # from 0 to the min length.
        for i in range(m):
           if text1[i] != text2[i]:
            errors.write("%d: %s: %s\n" %(i, text1[i], text2[i]))
        # Print extra characters to errors file.
        if L1 > L2:
            errors.write(text1[m:])
        elif L2 > L1:
            errors.write(text2[m:])
        errors.close()
same("Text1.txt")
