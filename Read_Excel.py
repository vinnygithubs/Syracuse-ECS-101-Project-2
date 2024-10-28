# title
from importlib.resources import contents
from operator import truediv
import pandas as pd
#
XL = pd.read_excel('P2M012_G5.xlsx', dtype=str)
Char = list(XL['Char'])
Bin = list(XL['Bin'])
# variables
shortnum = 5
longnum = 7

for index,item in enumerate(Char):
    if item == '<space>':
        Char[index] = " "
    elif item == '<apostraphe>':
        Char[index] = "'"
    elif item == '<newline>':
        Char[index] = "\n"

print(Char)
