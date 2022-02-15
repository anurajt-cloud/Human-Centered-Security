import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        self.passwords = []
        self.num_enteries = len(self.passwords)
        
        self.window = tkinter.Tk()
        

        
    def clear_text(self, event):
        self.password_field.delete(0, END)

    def add_pd(self, event):
        self.passwords.append(self.password_field.get())
        self.password_field.delete(0, END)

    def take_passwords(self):
        self.window.title("GUI")
        self.window.geometry("1000x700")
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.password_field.bind("<Return>", self.add_pd)
        self.password_field.bind("<BackSpace>", self.clear_text)
        self.window.mainloop()

    def get_passwords(self):
        return self.passwords

    def get_window(self):
        return self.window
# window.mainloop()

pr = PasswordRetriever()
pr.take_passwords()
print(pr.get_passwords())