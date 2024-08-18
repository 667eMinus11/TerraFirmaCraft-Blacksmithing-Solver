

from tkinter import *
import tkinter as tk
import winsound
from tkinter import ttk
target = 65
hits = {"hit 1": -3, "hit 2": -6, "hit 3": -9, "draw": -
        15, "key": 2, "bend": 7, "axe": 13, "syth": 16}
_any = ["hit 1", "hit 2", "hit 3", "draw", "key", "bend", "axe", "syth"]
_hit = ["hit 1", "hit 2", "hit 3"]
# requirmentLast=_any
# requirmentSecondtoLast=_any
# requirmentThirdtoLast=_any
requirmentLast = ["bend"]
requirmentSecondtoLast = ["bend"]
requirmentThirdtoLast = ["draw"]
preCombo = []
requirmentThirdtoLast.reverse()
total = 0
moves = []


def trimTarget(val):
    global preCombo
    while val > 60:
        preCombo.append("syth")
        val -= 16
    if (not requirmentLast == _any):
        val -= hits[requirmentLast[0]]
    if (not requirmentSecondtoLast == _any):
        val -= hits[requirmentSecondtoLast[0]]
    if (not requirmentThirdtoLast == _any):
        val -= hits[requirmentThirdtoLast[0]]
    if val<=0:
        val=2
    return val


tree = [["hit 1"], ["hit 2"], ["hit 3"], [
    "draw"], ["key"], ["bend"], ["axe"], ["syth"]]
_tree = tree


def verify(branch):
    if eval(branch) == target:
        return True


def eval(branch):
    total = 0
    for i in branch:
        total += hits[i]
    return total


def Shouldkeep(branch, _itr):
    if len(branch) < _itr:
        return 0

    if eval(branch) <= 0 or eval(branch) > 200:
        return 0

    if len(branch) > 15:
        return 0

    if verify(branch):
        return -1
    return 1


def treeSearch(_itr):
    print("started solving")
    processed = 0
    while True:
        _tree = tree.copy()
        print("processed "+str(processed)+" combantions")
        for i in _tree:
            should = Shouldkeep(i, _itr)

            if (should == 1):
                # print(i)
                # print(eval(i))
                i1 = i.copy()
                i1.append("hit 1")

                i2 = i.copy()
                i2.append("hit 2")

                i3 = i.copy()
                i3.append("hit 3")

                i4 = i.copy()
                i4.append("draw")

                i5 = i.copy()
                i5.append("key")

                i6 = i.copy()
                i6.append("bend")

                i7 = i.copy()
                i7.append("axe")

                i8 = i.copy()
                i8.append("syth")

                tree.append(i1)
                tree.append(i2)
                tree.append(i3)
                tree.append(i4)
                tree.append(i5)
                tree.append(i6)
                tree.append(i7)
                tree.append(i8)
            if should == 0:
                tree.remove(i)
            if should == -1:
                if (not requirmentThirdtoLast == _any):
                    i.append(requirmentThirdtoLast[0])
                if (not requirmentSecondtoLast == _any):
                    i.append(requirmentSecondtoLast[0])
                if (not requirmentLast == _any):
                    i.append(requirmentLast[0])
                preCombo.extend(i)
                return preCombo
            processed += 1
            _tree = tree.copy()
        _itr = _itr+1


def movesToText(moves):
    outp = ""
    for move in moves:
        pass
    return outp


# this is a function to get the selected list box value


def getListboxValue():
    itemSelected = listBoxOne.curselection()
    return itemSelected


def getListboxText():
    index = getListboxValue()
    itemSelected = listBoxOne.get(index)

    return itemSelected

# this is a function to get the user input from the text input box


def getInputBoxValue():
    userInput = Target.get()
    return userInput


root = Tk()
currentSelected = -1

# This is the section of code which creates the main window
root.geometry('729x394')
root.configure(background='#F0F8FF')
root.title('Blacksmithing solver')

global val1, val2, val3, sol
# This is the section of code which creates the a label
val1 = Label(root, text='any action', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), borderwidth=2, relief="groove",)


# This is the section of code which creates the a label
val2 = Label(root, text='any action', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), borderwidth=2, relief="groove",)


# This is the section of code which creates the a label
val3 = Label(root, text='any action', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), borderwidth=2, relief="groove",)


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def getCoraspondingActionValue(val):
    if val == "any hit":
        return _hit
    elif val == "any action":
        return _any
    elif val in _any:
        return [val]
    return "hit 1"


def solve():
    global target, preCombo, tree
    preCombo = []
    tree = [["hit 1"], ["hit 2"], ["hit 3"], [
        "draw"], ["key"], ["bend"], ["axe"], ["syth"]]
    target = safe_cast(getInputBoxValue(), int, 2)
    global requirmentLast, requirmentSecondtoLast, requirmentThirdtoLast
    requirmentLast = getCoraspondingActionValue(val1["text"])
    requirmentSecondtoLast = getCoraspondingActionValue(val2["text"])
    requirmentThirdtoLast = getCoraspondingActionValue(val3["text"])
    target = trimTarget(target)
    Text = treeSearch(0)
    num = 1
    print_ = ""
    for item in Text:
        print_ += " "+str(num)+". "+item+"  "
        if num % 5 == 0:
            print_ += '\n'
        num += 1
    global sol
    sol["text"] = print_
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


regularColor = "#F0F8FF"
activeColor = "#4294FF"


def SelectTextInput(event):
    global currentSelected, val1B, val2B, val3B
    currentSelected = -1
    val1B["bg"] = regularColor
    val2B["bg"] = regularColor
    val3B["bg"] = regularColor


def SelectLast():
    global currentSelected, val1B, val2B, val3B
    currentSelected = 1
    val1B["bg"] = activeColor
    val2B["bg"] = regularColor
    val3B["bg"] = regularColor


def Select2ndLast():
    global currentSelected, val1B, val2B, val3B
    currentSelected = 2
    val1B["bg"] = regularColor
    val2B["bg"] = activeColor
    val3B["bg"] = regularColor


def Select3rdLast():
    global currentSelected, val1B, val2B, val3B
    currentSelected = 3
    val1B["bg"] = regularColor
    val2B["bg"] = regularColor
    val3B["bg"] = activeColor


def selectedListbox(event):
    if currentSelected == 1:
        global val1
        val1["text"] = getListboxText()
    if currentSelected == 2:
        global val2
        val2["text"] = getListboxText()
    if currentSelected == 3:
        global val3
        val3["text"] = getListboxText()


# This is the section of code which creates a button
val1B = Button(root, text='Last', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), command=SelectLast)
val1B.place(x=395, y=126)

# This is the section of code which creates a button
val2B = Button(root, text='2nd to Last', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), command=Select2ndLast)
val2B.place(x=465, y=126)

# This is the section of code which creates a button
val3B = Button(root, text='3rd to Last', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), command=Select3rdLast)
val3B.place(x=585, y=126)

val1.place(x=378, y=176)
val2.place(x=485, y=176)
val3.place(x=605, y=176)


# This is the section of code which creates a listbox
listBoxOne = Listbox(root, bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), width=0, height=0)
listBoxOne.insert('0', 'hit 1')
listBoxOne.insert('1', 'hit 2')
listBoxOne.insert('2', 'hit 3')
listBoxOne.insert('3', 'draw')
listBoxOne.insert('4', 'key')
listBoxOne.insert('5', 'bend')
listBoxOne.insert('6', 'axe')
listBoxOne.insert('7', 'syth')
listBoxOne.insert('8', 'any hit')
listBoxOne.insert('9', 'any action')
listBoxOne.place(x=15, y=66)


# This is the section of code which creates the a label
Label(root, text='Solution:', bg='#F0F8FF', font=(
    'ariel', 12, 'normal')).place(x=195, y=266)


# This is the section of code which creates a text input box
Target = Entry(root, font=('ariel', 12, 'normal'))
Target.bind('<Button-1>', SelectTextInput)
Target.place(x=150, y=176)


# This is the section of code which creates a button
Button(root, text='Solve', bg='#F0F8FF', font=(
    'ariel', 15, 'bold'), command=solve).place(x=195, y=220)

listBoxOne.bind('<<ListboxSelect>>', selectedListbox)
# This is the section of code which creates the a label
Label(root, text='Target Value:', bg='#F0F8FF',
      font=('ariel', 12, 'bold')).place(x=150, y=126)

Label(root, text='Enter value needed (red arrow in anvil gui), then select one of the move restriction buttons, \nwhen it is highlighted select a move from the left. when done press solve ',
      bg='#F0F8FF', font=('ariel', 11, 'normal'), justify="left").place(x=10, y=10)

# This is the section of code which creates the a label
sol = Label(root, text='', bg='#F0F8FF', font=(
    'ariel', 12, 'normal'), justify="left")

sol.place(x=195, y=286)

root.mainloop()
