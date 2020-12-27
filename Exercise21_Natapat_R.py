from tkinter import *
import math


def leftClickButton(event):
    result = round(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2), 2)
    if result >= 30:
        result = 'อ้วนมาก'
    elif 25 <= result <= 29.9:
        result = 'อ้วน'
    elif 23 <= result <= 24.9:
        result = 'น้ำหนักเกิน'
    elif 18.6 <= result <= 22.9:
        result = 'น้ำหนักปกติ เหมาะสม'
    elif result <= 18.5:
        result = 'ผอม'
    labelResult.configure(text=result)


MainWindow = Tk()

labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)

calculateButton = Button(MainWindow, text="คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)

MainWindow.mainloop()
