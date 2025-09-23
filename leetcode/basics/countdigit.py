# CODE AND DEBUG
# part 6 ... count number of digits in a integer
# solution 1
def countdigit(num):
    c=0
    while num>0:
        c+=1
        num//=10
    return c
print(countdigit(1122))


# solution 2
# from math import *
# def countDigits(num):
#     return int(log10(num)+1)
# countDigits(11)