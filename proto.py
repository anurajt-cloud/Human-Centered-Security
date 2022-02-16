import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        self.passwords = []
        self.num_enteries = len(self.passwords)
        self.window = tkinter.Tk()
        self.min_len = 8
    # Function to clear the text in the entry field    
    def clear_text(self, event):
        self.password_field.delete(0, END)
    
    # Runs the main tk window
    def tap_passwords(self):
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
        self.password_field.bind("<Return>", self.validation)
        self.password_field.bind("<BackSpace>", self.clear_text)
        self.window.mainloop()
    # Function to get the list of passwords
    def get_passwords(self):
        return self.passwords
    
    # Validates the password with respect to its length.
    def tap_password_validation(self, event):
        password = self.password_field.get()
        msg = ''
        if len(password)==0:
            msg = 'Password can\'t be empty'
        else:
            try:
                # If the password is smaller than the min length then report
                if len(password)<self.min_len:
                    msg = 'Password to short.'
                    self.password_field.delete(0, END)
                # If not then append the password to the list and show success message
                else:
                    self.passwords.append(password)
                    self.password_field.delete(0, END)
                    msg = 'Success!'
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)


pr = PasswordRetriever()
pr.tap_passwords()
print(pr.get_passwords())