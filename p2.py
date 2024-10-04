# // Variables

import pandas as pd
XL = pd.read_excel('P2M010_G5.xlsx', dtype=str)
Char,Bin,Dec = list(XL['Char']),list(XL['Bin']),list(XL['Dec']) # The 3 Columns (Char,Bin,Dec)
ShortNum = 5
LongNum = 7

# // Functions

def grab_Info(request,start,end):
    # Request Params: Char,Bin,Dec
    if request != Bin and request != Dec and request != Char:
        return "Request Param Failed"
    if start or end < 0:
        return "Start and/or End Param Failed"

    if request == Bin and Bin != "":
        return request[start:end]
    elif request == Char and Char !="":
        return str(request[start:end])
    elif request == Dec and Dec !="":
        return request[start:end]

    # if all else fails
    return request

def grab_Short():
    return Char[0:15]

def grab_Long():
    return Char[15:126]

def grab_Char(request):
    # Request param can be Bin or Dec
    pass

def get_Bin(request):
    # Request param can be Char or Dec
    pass

def get_Dec(request):
    # Request param can be Bin or Char
    pass




# // Function Examples:
print(grab_Info(Bin,-1,15)) #Error Example
print(grab_Info('RANDOM',0,15)) #Error Example
print(grab_Info(Dec,0,15)) #Success Example

print(grab_Short()) # Returns all ShortNums with length 5
print(grab_Long()) # Returns all LongNums with length 7




