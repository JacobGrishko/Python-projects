import tkinter


nums = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
key_list = list(nums.keys())
val_list = list(nums.values())

Errors = {1:"An Integer cannot be higher or equal to the base.",
          2:"The program does not support bases higher than 16.",
          3:"The program doesnt support that char or int."}
Error=0

def checkInts(base, number):
    intbase = int(base)
    for char in number:
        if ord(char)<58 and ord(char)>47 or ord(char)<70 and ord(char)>64:
            number = key_list[val_list.index(char)]
        else:
            return Errors[3]
        if number >= intbase:
            return Errors[1]
    if intbase>16:
        return Errors[2]
    return 0

