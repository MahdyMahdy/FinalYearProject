import tkinter as tk
from tkinter import Button, ttk
from tkinter import Grid, Label, StringVar, Variable, font
from tkinter.constants import *
from typing import Collection, Text
import PIL.ImageTk as ITK
from PIL import Image

class ProjectsWindow():
    def __init__(self,master,id,cols,data,maxNbOfStd,removeFunc,addFunc,editFunc):
        temp = []
        for i in range(len(data)):
            row = list(data[i])
            row.pop(-1)
            stds = row[-1]
            row.pop(-1)
            stds = stds.split("<->")
            for j in range(len(stds)):
                row.append(stds[j])
                pass
            temp.append(row)
            pass
        data = temp
        self.window = tk.Toplevel(master = master,background="White")
        self.window.wm_iconbitmap('images\LUlogo.ico')
        self.window.title(id)
        WINDOWWIDTH=600
        WINDOWHEIGHT = 400
        SCREENWIDTH = int(self.window.winfo_screenwidth())
        SCREENHEIGHT = int(self.window.winfo_screenheight())
        BUTTONSWIDTH = 15
        PADDING = 7

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
        for i in range(0,4):
            radio = ttk.Radiobutton(master = searchByFrame,text=cols[i],value=i,variable=searchByVar)
            radio.grid(row = 0,column=i+1,padx=5)
            pass
        gradeRadio = ttk.Radiobutton(master = searchByFrame,text="Grade",value=4,variable=searchByVar)
        gradeRadio.grid(row = 0,column=i+2,padx=5)
        stdRadio = ttk.Radiobutton(master = searchByFrame,text="Std Infos",value=5,variable=searchByVar)
        stdRadio.grid(row = 0,column=i+3,padx=5)
        searchFrame = tk.Frame(master = self.window,background="White")
        searchFrame.pack(pady=5)
        searchVar = tk.StringVar()
        searchEntry = ttk.Entry(master = searchFrame,textvariable=searchVar)
        searchEntry.grid(row = 0, column=0,padx=5)
        self.data=data
        self.searchedData = data
        def searchFunc():
            for item in self.projects.get_children():
                self.projects.delete(item)
                pass
            self.searchedData = []
            if searchByVar.get()==5:
                for i in range(0,len(data)):
                    for j in range(data[i][3]):
                        if searchVar.get() in str(self.data[i][j+5]):
                            self.projects.insert(parent='', index=-1, text='',values=list(self.data[i]))
                            self.searchedData.append(self.data[i])
                            break
                            pass
            else:
                for i in range(0,len(data)):
                    if searchVar.get() in str(self.data[i][searchByVar.get()]):
                        self.projects.insert(parent='', index=i, iid=i, text='',values=list(self.data[i]))
                        self.searchedData.append(self.data[i])
                        pass 
            pass
        searchButton = tk.Button(master=searchFrame,text="Search",background="Red",foreground="White",command=searchFunc)
        searchButton.grid(row = 0, column=1,padx=5)
        frame = tk.Frame(self.window,background="White")
        frame.pack(padx=10,pady=10)
        scrollbarVer = ttk.Scrollbar(master=frame)
        scrollbarVer.pack(side="right",fill="y")
        scrollbarHor = ttk.Scrollbar(master=frame,orient="horizontal")
        scrollbarHor.pack(side="bottom",fill="x")
        self.projects = ttk.Treeview(master = frame,yscrollcommand=scrollbarVer.set,xscrollcommand=scrollbarHor.set)
        scrollbarVer.config(command=self.projects.yview)
        scrollbarHor.config(command=self.projects.xview)
        self.projects.pack(side="left")
        self.projects['columns']=cols
        self.projects.column('#0', width=0,stretch=NO)
        self.projects.heading('#0', text='', anchor=CENTER)
        self.reverse = FALSE
        def sort(n):
            sortedData = sorted(self.searchedData,key=lambda x:x[n],reverse=self.reverse)
            self.reverse = not self.reverse
            for item in self.projects.get_children():
                self.projects.delete(item)
                pass
            for i in range(0,len(sortedData)):
                self.projects.insert(parent='', index=i, iid=i, text='',values=list(sortedData[i]))
                pass 
            pass
        for i in range(len(cols)):
            self.projects.column(cols[i], anchor=CENTER, width=int(WINDOWWIDTH/len(cols)))
        self.projects.heading(cols[0], text=cols[0], anchor=CENTER,command=lambda :sort(0))
        self.projects.heading(cols[1], text=cols[1], anchor=CENTER,command=lambda :sort(1))
        self.projects.heading(cols[2], text=cols[2], anchor=CENTER,command=lambda :sort(2))
        self.projects.heading(cols[3], text=cols[3], anchor=CENTER,command=lambda :sort(3))
        self.projects.heading(cols[4], text=cols[4], anchor=CENTER,command=lambda :sort(4))
        for i in range(5,5+maxNbOfStd):
            self.projects.heading(cols[i], text=cols[i], anchor=CENTER)
        for i in range(len(data)):
            self.projects.insert(parent='', index=i, iid=i, text='',values=list(data[i]))
        buttonFrame = tk.Frame(master = self.window,bg="White")
        buttonFrame.pack(pady=10)
        removeButton = tk.Button(master = buttonFrame,text="Remove",width=15,background="Red",foreground="White",command=removeFunc)
        removeButton.grid(row=0,column=0,padx=5)
        addButton = tk.Button(master = buttonFrame,text="Add",width=15,background="Red",foreground="White",command=addFunc)
        addButton.grid(row=0,column=1,padx=5)
        EditButton = tk.Button(master = buttonFrame,text="Edit",width=15,background="Red",foreground="White",command=editFunc)
        EditButton.grid(row=0,column=2,padx=5)
        pass