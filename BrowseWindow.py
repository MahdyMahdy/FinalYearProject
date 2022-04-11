import tkinter as tk
from tkinter import Button, ttk
from tkinter import Grid, Label, StringVar, Variable, font
from tkinter.constants import *
from typing import Collection, Text
import PIL.ImageTk as ITK
from PIL import Image

class BrowseWindow():
    def __init__(self,master,cols,data,removeFunc,openFunc):
        self.window = tk.Toplevel(master=master,bg="White")
        self.window.configure(bg="white")
        self.window.title('Browse Projects Collections')
        self.window.wm_iconbitmap('images\LUlogo.ico')
        WINDOWWIDTH=600
        WINDOWHEIGHT = 400
        SCREENWIDTH = int(self.window.winfo_screenwidth())
        SCREENHEIGHT = int(self.window.winfo_screenheight())
        BUTTONSWIDTH = 30
        PADDING = 15

        self.window.geometry("{}x{}+{}+{}".format(
            WINDOWWIDTH,
            WINDOWHEIGHT,
            SCREENWIDTH//2-WINDOWWIDTH//2,
            SCREENHEIGHT//2-WINDOWHEIGHT//2))

        style2=ttk.Style()
        style2.configure("TRadiobutton",background="White")
        searchByVar = tk.IntVar()
        searchByVar.set(0)
        searchByFrame = tk.Frame(master = self.window,background="White")
        searchByFrame.pack(pady=5)
        searchByLabel = ttk.Label(master=searchByFrame,background="White",text="Search By:")
        searchByLabel.grid(row=0,column=0,padx=5)
        for i in range(0,len(cols)-1):
            radio = ttk.Radiobutton(master = searchByFrame,text=cols[i],value=i,variable=searchByVar)
            radio.grid(row = 0,column=i+1,padx=5)
            pass
        searchFrame = tk.Frame(master = self.window,background="White")
        searchFrame.pack(pady=5)
        searchVar = tk.StringVar()
        searchEntry = ttk.Entry(master = searchFrame,textvariable=searchVar)
        searchEntry.grid(row = 0, column=0,padx=5)
        self.data=data
        self.searchedData = data
        def searchFunc():
            for item in self.collections.get_children():
                self.collections.delete(item)
                pass
            self.searchedData = []
            for i in range(0,len(data)):
                if searchVar.get() in str(self.data[i][searchByVar.get()]):
                    self.collections.insert(parent='', index=i, iid=i, text='',values=list(self.data[i]))
                    self.searchedData.append(self.data[i])
                    pass 
            pass
        searchButton = tk.Button(master=searchFrame,text="Search",background="Red",foreground="White",command=searchFunc)
        searchButton.grid(row = 0, column=1,padx=5)
        frame = tk.Frame(self.window,background="White")
        frame.pack(padx=10,pady=10)
        scrollbar = ttk.Scrollbar(master=frame)
        scrollbar.pack(side="right",fill="y")
        self.collections = ttk.Treeview(master = frame,yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.collections.yview)
        self.collections.pack(side="left")
        self.collections['columns']=cols
        self.collections.column('#0', width=0,stretch=NO)
        self.collections.heading('#0', text='', anchor=CENTER)
        self.reverse = FALSE
        def sort(n):
            sortedData = sorted(self.searchedData,key=lambda x:x[n],reverse=self.reverse)
            self.reverse = not self.reverse
            for item in self.collections.get_children():
                self.collections.delete(item)
                pass
            for i in range(0,len(sortedData)):
                self.collections.insert(parent='', index=i, iid=i, text='',values=list(sortedData[i]))
                pass 
            pass
        for i in range(len(cols)):
            self.collections.column(cols[i], anchor=CENTER, width=int(WINDOWWIDTH/len(cols)))
        self.collections.heading(cols[0], text=cols[0], anchor=CENTER,command=lambda :sort(0))
        self.collections.heading(cols[1], text=cols[1], anchor=CENTER,command=lambda :sort(1))
        self.collections.heading(cols[2], text=cols[2], anchor=CENTER,command=lambda :sort(2))
        self.collections.heading(cols[3], text=cols[3], anchor=CENTER,command=lambda :sort(3))
        self.collections.heading(cols[4], text=cols[4], anchor=CENTER,command=lambda :sort(4))
        for i in range(len(data)):
            self.collections.insert(parent='', index=i, iid=i, text='',values=list(data[i]))
        buttonFrame = tk.Frame(master = self.window,bg="White")
        buttonFrame.pack(pady=10)
        removeButton = tk.Button(master = buttonFrame,text="Remove",width=15,background="Red",foreground="White",command=removeFunc)
        removeButton.grid(row=0,column=0,padx=5)
        openButton = tk.Button(master = buttonFrame,text="Open",width=15,background="Red",foreground="White",command=openFunc)
        openButton.grid(row=0,column=1,padx=5)
        pass
    pass
