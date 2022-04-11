from DataBase import DatabaseManager
import tkinter as tk
from tkinter import Button, ttk
from tkinter import Grid, Label, StringVar, Variable, font
from tkinter.constants import *
from typing import Collection, Text
import PIL.ImageTk as ITK
from PIL import Image

class AddWindow():
    def __init__(self,master,title,maxNbOfStd,addFunc,entrydata):
        self.window = tk.Toplevel(master = master,background="White")
        self.window.title(title)
        self.window.wm_iconbitmap('images\LUlogo.ico')
        WINDOWWIDTH=350
        WINDOWHEIGHT = (maxNbOfStd+8)*30
        SCREENWIDTH = int(self.window.winfo_screenwidth())
        SCREENHEIGHT = int(self.window.winfo_screenheight())
        BUTTONSWIDTH = 15
        PADDING = 7

        self.window.geometry("{}x{}+{}+{}".format(
            WINDOWWIDTH,
            WINDOWHEIGHT,
            SCREENWIDTH//2-WINDOWWIDTH//2,
            SCREENHEIGHT//2-WINDOWHEIGHT//2))

        style1=ttk.Style()
        style1.configure("TLabel",background="White")
        style2=ttk.Style()
        style2.configure("TRadiobutton",background="White")
        style2=ttk.Style()
        style2.configure("TEntry",width = 20)
        superVisorLabel = ttk.Label(self.window,text="Supervisor Name :")
        superVisorLabel.grid(row=0,column=0,sticky="W",padx=5,pady=5)
        self.superVisorNameVar = tk.StringVar()
        if not entrydata==None:
            self.superVisorNameVar.set(entrydata[1])
        self.superVisorName = ttk.Entry(self.window,textvariable=self.superVisorNameVar,width=35)
        self.superVisorName.grid(row=0,column=1,sticky="E",padx=5,pady=5)
        self.superVisorVal = tk.StringVar()
        superVisorValLabel = ttk.Label(self.window,textvariable=self.superVisorVal,background="White",foreground="Red")
        superVisorValLabel.grid(row = 1,column = 0,sticky = "W",padx=5,columnspan = 2)
        titleLabel = ttk.Label(self.window,text="Title :")
        titleLabel.grid(row=2,column=0,sticky="W",padx=5,pady=5)
        self.titleVar = tk.StringVar()
        if not entrydata==None:
            self.titleVar.set(entrydata[2])
        title = ttk.Entry(self.window,textvariable=self.titleVar,width=35)
        title.grid(row=2,column=1,sticky="E",padx=5,pady=5)
        self.titleVal = tk.StringVar()
        titleValLabel = ttk.Label(self.window,textvariable=self.titleVal,background="White",foreground="Red")
        titleValLabel.grid(row = 3,column = 0,sticky = "W",padx=5,columnspan = 2)
        gradeLabel = ttk.Label(self.window,text="Grade :")
        gradeLabel.grid(row=4,column=0,sticky="W",padx=5,pady=5)
        self.gradeVar = tk.DoubleVar()
        if not entrydata==None:
            self.gradeVar.set(float(entrydata[4]))
        grade = ttk.Entry(self.window,textvariable=self.gradeVar,width=35)
        grade.grid(row=4,column=1,sticky="E",padx=5,pady=5)
        self.gradeVal = tk.StringVar()
        gradeValLabel = ttk.Label(self.window,textvariable=self.gradeVal,background="White",foreground="Red")
        gradeValLabel.grid(row = 5,column = 0,sticky = "W",padx=5,columnspan = 2)
        self.stdsInfos = []
        for i in range(maxNbOfStd):
            superVisorLabel = ttk.Label(self.window,text="Student "+str(i+1)+" Infos : ")
            superVisorLabel.grid(row=i+6,column=0,sticky="W",padx=5,pady=5)
            self.stdsInfos.append(tk.StringVar())
            if not entrydata==None and i+5<len(entrydata):
                self.stdsInfos[i].set(entrydata[i+5])
            superVisorName = ttk.Entry(self.window,textvariable=self.stdsInfos[i],width=35)
            superVisorName.grid(row=i+6,column=1,sticky="E",padx=5,pady=5)
        self.stdVal = tk.StringVar()
        stdValLabel = ttk.Label(self.window,textvariable=self.stdVal,background="White",foreground="Red")
        stdValLabel.grid(row = i+7,column = 0,sticky = "W",padx=5,columnspan = 2)
        createButton = tk.Button(
            master = self.window , 
            text = "Done" ,width=15,
            background="Red",
            foreground="White", 
            command=addFunc)
        createButton.grid(column=0,row=i+8,columnspan=2,pady=5)
        pass
    pass