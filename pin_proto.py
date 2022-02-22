import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PINRetriever():
    
    def __init__ (self):
        
        
        self.pins = []
        self.setting_pin = False
        self.des = True
        self.window = None
        self.pin = ''
        self.pin_len = 4
        self.pin_test_count = 6

    # Method to Clear a pin   
    def clear_pin(self, event):
        self.pin_field.delete(0, END)

    # Method to create a window with a particular title
    def create_window(self, title):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.geometry(self.geometry)

    # Method to ask for confirmation for password creation
    def confirm_creation(self):
        return tk.messagebox.askyesno(title='Confirmation',message='Are you satisfied with the PIN?')

    # Method for creating a PIN
    def create_pin(self):
        self.window = tkinter.Tk()
        self.window.title("Setting PIN Window")
        self.window.geometry("1000x700")
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        tk.messagebox.showinfo("Instructions", "You are now going to create a PIN\n\n***You will have one attempt to create the PIN***\n\nAfter creating if not satisfied you can create it again.\n\nPress Ok to create the PIN..")
        l1 = tk.Label(self.window, text='STATUS: Creating PIN', fg='Red').pack(side=TOP, anchor=NW)
        self.pin_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.pin_field.focus_force()
        self.pin_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.setting_pin = True
        self.pin_field.bind("<Return>", self.pin_validation)
        self.pin_field.bind("<BackSpace>", self.clear_pin)
        self.window.mainloop()
        

    # Method for testing for PINs
    def testing_pins(self):
        self.des = False
        self.window = tkinter.Tk()
        self.window.title("PIN PASSWORDS")
        self.window.geometry("1000x700")
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        tk.messagebox.showinfo("Instructions", "You are going to enter the created PIN 6 times\n\nOnces entered you will not have a chance to change it\n\nA count for number of attempts left will be displayed after every entry\n\nGood Luck, press Ok to start test.")
        l1 = tk.Label(self.window, text='STATUS: Testing PINs', fg='Red').pack(side=TOP, anchor=NW)
        self.pin_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.pin_field.focus_force()
        self.pin_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.pin_field.bind("<Return>", self.pin_validation)
        self.pin_field.bind("<BackSpace>", self.clear_pin)
        self.window.mainloop()

    # Method for PIN validation
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
                elif self.setting_pin:
                    if self.confirm_creation():
                        self.pin = pin
                        msg = 'PIN set successfully!'
                        self.setting_pin = False
                        self.des = True
                    else:
                        msg = 'Press Ok to set PIN again.'
                else:
                    self.pin_test_count-=1
                    self.pins.append(pin)
                    msg = "***CONGRATULATIONS***\n\n6 attempts completed! Thank you" if self.pin_test_count==0 else 'Attempts left = '+str(self.pin_test_count) 
                self.pin_field.delete(0, END)
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)

        if not self.setting_pin and self.des:
            self.window.destroy()
        elif self.pin_test_count==0:
            self.window.destroy()
    # Method to get test PINs
    def get_pins(self):
        return self.pins
    # Method to get true PIN
    def get_pin(self):
        return self.pin

pr = PINRetriever()

pr.create_pin()
print(pr.get_pin())
pr.testing_pins()
print(pr.get_pins())
