import Calcs
from tkinter import messagebox


res = {"dec": "", "binary": "", "octal": "", "hex": "", "special": ""}

def mainCalc(base, num, specBase):
    print(base)
    print(num)
    special = int(specBase)

    if base==10:
        res["dec"] = num
        res["binary"] = Calcs.calcFromDec(num,2)
        res["octal"] = Calcs.calcFromDec(num,8)
        res["hex"] = Calcs.calcFromDec(num,16)
        if special>=2:
            res["special"] = Calcs.calcFromDec(num, special)

        return res

    else:
        decimal = Calcs.calcToDec(num, base)

        res["dec"] = decimal
        res["binary"] = Calcs.calcFromDec(decimal, 2)
        res["octal"] = Calcs.calcFromDec(decimal, 8)
        res["hex"] = Calcs.calcFromDec(decimal, 16)
        if special>=2:
            res["special"] = Calcs.calcFromDec(decimal, special)

        return res
