import tkinter as tk
from tkinter import ttk
from tkinter import Grid, Label, StringVar, Variable, font
from tkinter.constants import HORIZONTAL, LEFT, RIGHT
from typing import Text
import PIL.ImageTk as ITK
from PIL import Image

class CreateWindow():
    def __init__(self,master,CreateFunc,CancelFunc):
        self.window = tk.Toplevel(master = master,background="White" )
        self.window.title('Create New Projects Collection')
        self.window.wm_iconbitmap('images\LUlogo.ico')
        WINDOWWIDTH=370
        WINDOWHEIGHT = 230
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
        style1.configure("TMenubutton",background="White")
        style2=ttk.Style()
        style2.configure("TRadiobutton",background="White")
        
        branchLabel = ttk.Label(self.window ,text = "Branch Number :" ,background="White",foreground="Black")
        branchLabel.grid(column =0,row=0,sticky="W",padx=10)

        options_list = ["Select Value","1 Hadath", "2 Fanar", "3 Tripoli", "4 Beqaa","5 Nabatyeh"]
        self.branchVar = tk.StringVar()
        branch = ttk.OptionMenu(self.window,self.branchVar,*options_list)
        branch.grid(column=1,row=0,sticky="E",padx=10)

        self.branchVal = tk.StringVar()
        branchValidation = ttk.Label(self.window,textvariable=self.branchVal,background="White",foreground="Red")
        branchValidation.grid(column=0,row=1,sticky="W",padx=10)

        yearLabel = ttk.Label(self.window ,text = "Education Year :" ,background="White")
        yearLabel.grid(column=0,row=2,sticky="W",padx=10)

        self.firstYear = ttk.Entry(self.window ,width=20 )
        self.firstYear.grid(column=1,row=2,sticky="E",padx=10)

        self.yearVal = StringVar()
        self.yearVal.set("")
        yearValidation = ttk.Label(master = self.window,textvariable=  self.yearVal,background="White",foreground="Red")
        yearValidation.grid(column=0,row=3,sticky="W",padx=10)

        groupLabel = ttk.Label(self.window ,text = "Max Number Of Students In Group :" ,  background= "White")
        groupLabel.grid(column=0,row=4,sticky="W",padx=10)

        s=ttk.Style()
        s.configure("Horizontal.TScale",background="White",foreground="Red")
        self.groupVar = tk.IntVar()
        self.groupVar.set(1)
        groupFrame = tk.Frame(master= self.window,background="White")
        text = tk.StringVar()
        text.set("1")
        groupTextLabel = tk.Label(master =groupFrame,background="White",textvariable=text)
        groupTextLabel.pack(side="top")
        def change(n):
            text.set(str(self.groupVar.get()))
        self.group = ttk.Scale(master = groupFrame ,from_=1, to=10 , variable=self.groupVar,command=change)
        self.group.pack(side="bottom")
        groupFrame.grid(column=1,row=4,sticky="E",padx=10)
        empty1=ttk.Label(self.window,background="White",text=" ")
        empty1.grid(column=0,row=5,sticky="W",padx=10)
        languageLabel = ttk.Label(master = self.window ,text = "Class Language :" ,background="White")
        languageLabel.grid(column=0,row=6,sticky="W",padx=10)
        langFrame = ttk.Frame(master = self.window )
        langFrame.grid(column=1,row=6,sticky="E",padx=10)
        self.lang = tk.StringVar()
        self.lang.set("EN")
        eng = ttk.Radiobutton(master = langFrame  , text = "English" , variable=self.lang , value = "EN")
        eng.pack(side = LEFT)
        fr = ttk.Radiobutton(master = langFrame , text = "French" , variable=self.lang , value="FR")
        fr.pack(side = RIGHT)
        empty2=ttk.Label(self.window,background="White",text=" ")
        empty2.grid(column=0,row=7,sticky="W",padx=10)
        buttonFrame = tk.Frame(self.window,background="White")
        createButton = tk.Button(
            master = buttonFrame , 
            text = "Create" ,width=15,
            background="Red",
            foreground="White", 
            command=CreateFunc)
        createButton.pack(side="left",padx=5)
        cancelButton = tk.Button(
            master = buttonFrame ,
            text = "Cancel" ,width=15,
            background="Red",
            foreground="White", 
            command=CancelFunc)
        cancelButton.pack(side="right",padx=5)
        buttonFrame.grid(column=0,row=8,columnspan=2)
        pass
    pass