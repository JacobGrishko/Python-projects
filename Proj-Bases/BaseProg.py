from tkinter import Tk, Button, Label, Entry, Radiobutton, IntVar, messagebox
from main import mainCalc
import Errs
import sys


window = Tk()
window.title('Base Converter')
window.geometry("340x280")
#window.iconbitmap('app.ico')
window.resizable(False, False)

r = IntVar()

#Label
lbl1 = Label(window, text = "Welcome")
lbl1.place(x = 10,y = 10)
lbl2 = Label(window, text = "Choose a Base, a number and convert(Capital, positive only)")
lbl2.place(x = 10,y = 35)

#Decimal
rb1 = Radiobutton(text="Decimal", variable=r, value=1)
rb1.place(x=10, y=70)
ent1 = Entry(window, width= 30)
ent1.place(x = 100,y = 70)

#Binary
rb1 = Radiobutton(text="Binary", variable=r, value=2)
rb1.place(x=10, y=100)
ent2 = Entry(window, width= 30)
ent2.place(x = 100, y = 100)

#Octal
rb1 = Radiobutton(text="Octal", variable=r, value=3)
rb1.place(x=10, y=130)
ent3 = Entry(window, width= 30)
ent3.place(x = 100, y = 130)

#Hex
rb1 = Radiobutton(text="Hex", variable=r, value=4)
rb1.place(x=10, y=160)
ent4 = Entry(window, width= 30)
ent4.place(x = 100, y = 160)

#Special

ent5 = Entry(window, width= 5)
ent5.place(x = 100, y = 190)
ent6 = Entry(window, width= 23)
ent6.place(x = 140, y = 190)
rb1 = Radiobutton(text="Special", variable=r, value=5)
rb1.place(x=10, y=190)


def convert():
#Base for special
    if ent5.get()=='':
        ent5.insert(0,3)

#Extract relevant base and number
    set = {"base": 0, "number": "0"}
    choise = r.get()

    if choise == 1:
        set["base"] = 10
        set["number"] = ent1.get()
    elif choise == 2:
        set["base"] = 2
        set["number"] = ent2.get()
    elif choise == 3:
        set["base"] = 8
        set["number"] = ent3.get()
    elif choise == 4:
        set["base"] = 16
        set["number"] = ent4.get()
    elif choise == 5:
        set["base"] = ent5.get()
        set["number"] = ent6.get()

    print("base is {0} number is {1}".format(set["base"], set["number"]))

#check before convertion
    err = Errs.checkInts(set["base"], set["number"])
    print(err)
    if err != 0:
        messagebox.showinfo("Error", err)

    else:
        res = mainCalc(set["base"], set["number"], ent5.get())

        clear()

        ent1.insert(0, res["dec"])
        ent2.insert(0, res["binary"])
        ent3.insert(0, res["octal"])
        ent4.insert(0, res["hex"])
        ent6.insert(0, res["special"])

#clear funct
def clear():
    ent1.delete(0, len(ent1.get()))
    ent2.delete(0, len(ent2.get()))
    ent3.delete(0, len(ent3.get()))
    ent4.delete(0, len(ent4.get()))
    ent6.delete(0, len(ent6.get()))


btn1 = Button(window, text="Convert", command=convert)
btn1.place(x=100, y=230)

btn1 = Button(window, text="Clear", command=clear)
btn1.place(x=200, y=230)


window.mainloop()