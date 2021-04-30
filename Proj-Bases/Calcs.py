

nums = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
key_list = list(nums.keys())
val_list = list(nums.values())

def  calcFromDec(number, base):
    num = int(number)
    newNum = "0"
    if (num == 0):
        return newNum
    newNum = ''

    if num < base and num != 0:
        newNum = str(nums[num])
        return newNum

    while num>=base:
        quotient = divmod(num,base)[1]
        if quotient==0:
            newNum+="0"
        else:
            newNum += str(nums[quotient])
        num = int(num/base)
        if num<base and num!=0:
            newNum+=str(nums[num])
    return newNum[::-1]


def calcToDec(num, base):
    sum = 0
    strNum= str(num)
    left = len(strNum) - 1

    for char in strNum:
        number = key_list[val_list.index(char)]
        baseInt=(pow(int(base), left))
        decInt = number*baseInt
        sum += decInt
        left -= 1
    return sum

