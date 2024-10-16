file_1='eeee'
file_2='eeZee'

def same(f1,f2):
    for char in file_1:
        for char2 in file_2:
            if char2 == char:
                continue
            else:
                print(char2,'in "file 2" not equal to',char,'in "file 1"')
                return False
    return True

print(same(file_1,file_2))
