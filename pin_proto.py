import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        
        self.pins = []
        self.setting_pin = False
        self.window = None
        self.pin = ''
        self.pin_len = 4
        self.pin_set_count = 0
        
    def clear_pin(self, event):
        self.pin_field.delete(0, END)

    def set_pin(self):
        self.window = tkinter.Tk()
        self.window.title("Setting PIN Window")
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
        self.setting_pin = True
        self.pin_field.bind("<Return>", self.pin_validation)
        self.pin_field.bind("<BackSpace>", self.clear_pin)
        self.window.mainloop()
        self.setting_pin = False


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
                elif self.setting_pin==True:
                    self.pin = pin
                    msg = 'PIN set successfully!'
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
    def get_pin(self):
        return self.pin

pr = PasswordRetriever()
# pr.tap_passwords()
# print(pr.get_passwords())
pr.set_pin()
print(pr.get_pin())
