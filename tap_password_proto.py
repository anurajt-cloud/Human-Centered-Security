import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        self.passwords = []
        self.password = ''
        self.num_enteries = len(self.passwords)
        self.window = None
        self.min_tap_len = 8
        
    # Function to clear the text in the entry field    
    def clear_tp(self, event):
        self.password_field.delete(0, END)
    
    
    # Runs the main tk window
    def tap_passwords(self):
        self.window = tkinter.Tk()
        self.window.title("TAP PASSWORDS")
        self.window.geometry("1000x700")
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.password_field.bind("<Return>", self.tap_password_validation)
        self.password_field.bind("<BackSpace>", self.clear_tp)
        self.window.mainloop()

    # Function to get the list of passwords
    def get_passwords(self):
        return self.passwords

    # Validates the characters of the password
    def tap_password_char_check(self, password):
        char_list = ["f", "g", "h", "j"]
        matched_char_list = [characters in char_list for characters in password]
        return all(matched_char_list)

    def password_val(self, password):
        if len(password)==0:
            return False, 'Password can\'t be empty'
        elif len(password)<self.min_tap_len:
            return False, 'Password too short.'
        elif self.tap_password_char_check(password):
            return True, 'Success!'
        else:
            return False, 'Password characters incorrect. Only Tap keys F,G,H,J.'


    # Validates the password with respect to its length.
    def tap_password_validation(self, event):
        password = self.password_field.get()
        self.password_val(password)
        try:
            the_con, msg = self.password_val(password)
            if the_con:
                self.passwords.append(password)
            self.password_field.delete(0, END)
        except Exception as ep:
            tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)


pr = PasswordRetriever()
pr.tap_passwords()
print(pr.get_passwords())
