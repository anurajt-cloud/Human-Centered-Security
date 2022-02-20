import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        self.passwords = []
        self.pins = []
        self.num_enteries = len(self.passwords)
        self.window = tkinter.Tk()
        self.min_tap_len = 8
        self.pin_len = 4
    # Function to clear the text in the entry field    
    def clear_tp(self, event):
        self.password_field.delete(0, END)
    
    def clear_pin(self, event):
        self.pin_field.delete(0, END)

    # Runs the main tk window
    def tap_passwords(self):
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

    # Validates the password with respect to its length.
    def tap_password_validation(self, event):
        password = self.password_field.get()
        msg = ''
        if len(password)==0:
            msg = 'Password can\'t be empty'
        else:
            try:
                # If the password is smaller than the min length then report
                if len(password)<self.min_tap_len:
                    msg = 'Password too short.'
                    self.password_field.delete(0, END)
                # If not then append the password to the list and show success message
                else:
                    if self.tap_password_char_check(password):
                        self.passwords.append(password)
                        self.password_field.delete(0, END)
                        msg = 'Success!'
                    else:
                        msg = 'Password characters incorrect. Only Tap keys F,G,H,J.'
                        self.password_field.delete(0, END)
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)

    def pins_passwords(self):
        self.window = tkinter.Tk()
        self.window.title("PIN PASSWORDS")
        self.window.geometry("1000x700")
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        # label2 = Label(self.window, "Tap Passwords", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center')
        self.pin_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.pin_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.pin_field.bind("<Return>", self.pin_validation)
        self.pin_field.bind("<BackSpace>", self.clear_pin)
        self.window.mainloop()

    # Validates the password with respect to its length.
    def pin_validation(self, event):
        pin = self.pin_field.get()
        msg = ''
        if len(pin)==0:
            msg = 'Password can\'t be empty'
        else:
            try:
                if not pin.isdigit():
                    msg = 'It should be a digit.' 
                elif len(pin)!=4:
                    msg = 'Has to be of length 4.'
                    self.pin_field.delete(0, END)
                else:
                    self.pins.append(pin)
                    self.pin_field.delete(0, END)
                    msg = 'Success!'
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)

    def get_pins(self):
        return self.pins


pr = PasswordRetriever()
pr.tap_passwords()
print(pr.get_passwords())
pr.pins_passwords()
print(pr.get_pins())
