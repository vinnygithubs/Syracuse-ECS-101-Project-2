# Global Variables
import pandas as pd
XL = pd.read_excel('P2M010_G5.xlsx', dtype=str)
# Columns
Char = list(XL['Char'])
Bin = list(XL['Bin'])
Dec = list(XL['Dec'])
#
ShortNum = 5
LongNum = 7
#

def isShort_Long(request):
    if Char[request]:
        pass
