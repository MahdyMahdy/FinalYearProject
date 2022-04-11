import tkinter as tk
from tkinter import Grid, Label, StringVar, Variable, font
from tkinter.constants import HORIZONTAL, LEFT, RIGHT
from typing import Text
import PIL.ImageTk as ITK
from PIL import Image

#creating the start window
class StartWindow():
    def __init__(self,createButtonCommand,browseButtonCommand):
        self.window = tk.Tk()
        self.window.wm_iconbitmap('images\LUlogo.ico')
        #making white background
        self.window.configure(bg="white")
        #setting the title
        self.window.title('I3308 Managment System')
        #setting width and height
        STARTWINDOWWIDTH=450
        STARTWINDOWHEIGHT = 600
        #getting screen width and height
        SCREENWIDTH = int(self.window.winfo_screenwidth())
        SCREENHEIGHT = int(self.window.winfo_screenheight())
        BUTTONSWIDTH = 30
        PADDING = 15

        #centering the window
        self.window.geometry("{}x{}+{}+{}".format(
            STARTWINDOWWIDTH,
            STARTWINDOWHEIGHT,
            SCREENWIDTH//2-STARTWINDOWWIDTH//2,
            SCREENHEIGHT//2-STARTWINDOWHEIGHT//2))

        #making header for the window
        universityLabel=tk.Label(
            master = self.window,
            text='Lebanese University Faculty Of Science',
            font=font.Font(family='Helvetica'),
            bg="white")
        universityLabel.pack(pady = PADDING)

        image = Image.open('images\LUlogo.jpg')
        image.resize((50,50))
        lulogo = ITK.PhotoImage(master = self.window,image=image)
        logoLabel = tk.Label(master = self.window,image=lulogo,bg="white",width=200,height=200)
        logoLabel.image = lulogo
        logoLabel.pack(pady = PADDING)

        self.createButton = tk.Button(
            master = self.window,
            text='Create New Projects Collection' , 
            width=BUTTONSWIDTH ,
            command=createButtonCommand,
            bg="Red" , 
            fg="White" ,
            font=font.Font(family='Helvetica'))
        self.createButton.pack(pady = PADDING)

        self.browseButton = tk.Button(
            master = self.window,
            text='Browse Projets Collections' , 
            width=BUTTONSWIDTH,bg="Red" ,
            fg="White" ,
            command = browseButtonCommand,
            font=font.Font(family='Helvetica'))
        self.browseButton.pack(pady = PADDING)
        pass

    def show(self):
        self.window.mainloop()
        pass
    pass