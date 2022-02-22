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
        # bool var to close the create password window
        self.created_tp = False
        # Var for confirming the password
        self.con_count = 0
        # Testing appempts count
        self.test_count = 6
        # Window params
        self.geometry = "1000x700"
        self.background_path = "./bg.png" 
    # Function to clear the text in the entry field    
    def clear_tp(self, event):
        self.password_field.delete(0, END)
    
    # Method to create a window with a particular title
    def create_window(self, title):
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.geometry(self.geometry)

    # Method to ask for confirmation for password creation
    def confirm_creation(self):
        return tk.messagebox.askyesno(title='Confirmation',message='Are you satisfied with the password?')

    # Method to check the password
    def check_password(self, pw):
        return self.password==pw
   
    # Validates the characters of the password.
    def tap_password_char_check(self, password):
        char_list = ["f", "g", "h", "j"]
        matched_char_list = [characters in char_list for characters in password]
        return all(matched_char_list)

    # Method to validate the password.
    def password_val(self, password):
        if len(password)==0:
            return False, 'Password can\'t be empty'
        elif len(password)<self.min_tap_len:
            return False, 'Password too short.'
        elif self.tap_password_char_check(password):
            return True, 'Press Ok to create password again!'
        else:
            return False, 'Password characters incorrect. Only Tap keys F,G,H,J.'


    # Validates the password.
    def tp_creation_validation(self, event):
        password = self.password_field.get()
        self.password_val(password)
        try:
            the_con, msg = self.password_val(password)
            
            if the_con and self.confirm_creation():
                self.password=password
                self.created_tp = True
                msg = 'Success!\nNOW enter the correct password 5 consecutive time to confirm the password.'

            self.password_field.delete(0, END)
        except Exception as ep:
            tkinter.messagebox.showerror('error', ep)   
        tkinter.messagebox.showinfo('message', msg)
        if self.created_tp:
            self.window.destroy()

    # Runs the main tk window
    def create_password(self):
        self.create_window("CREATING TAP PASSWORDS")
        img = PhotoImage(file=self.background_path)
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        tk.messagebox.showinfo("Instructions", "You are now going to create a tap password\n\n***You will have one attempt to create the password***\n\nAfter creating if not satisfied you can create it again.\n\nPress Ok to create the tap password..")
        l1 = tk.Label(self.window, text='STATUS: Creating Password', fg='Black').pack(side=TOP, anchor=NW)
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.password_field.focus_force()
        self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.password_field.bind("<Return>", self.tp_creation_validation)
        self.password_field.bind("<BackSpace>", self.clear_tp)
        self.window.mainloop()

    # Validates the password.
    def tp_confirmation_validation(self, event):
        password = self.password_field.get()
        self.password_val(password)
        try:
            the_con, msg = self.password_val(password)
            pass_check = self.check_password(password)
            if the_con:
                if pass_check:
                    self.con_count+=1
                    msg = "PASSWORD CONFIRMED! 5 consecutive attempts reached." if self.con_count==5 else 'CORRECT! Consecutive count = '+str(self.con_count) 

                else:
                    self.con_count=0
                    msg = 'INCORRECT! Consecutive count RESET = '+str(self.con_count)

            self.password_field.delete(0, END)
        except Exception as ep:
            tkinter.messagebox.showerror('error', ep)   

        tkinter.messagebox.showinfo('message', msg)
        
        if self.con_count==5:
            self.window.destroy()

    # Confirm password function
    def confirm_password(self):
        self.create_window("CONFIRMING TAP PASSWORDS")
        img = PhotoImage(file=self.background_path)
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        tk.messagebox.showinfo("Instructions", "Now you will confirm the password\n\nYou will need to get 5 consecutive correct enteries to confirm successfully\n\nPress Ok to create the Confirm password.")
        l1 = tk.Label(self.window, text='STATUS: Confirming Password', fg='Black').pack(side=TOP, anchor=NW)
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.password_field.focus_force()
        self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.password_field.bind("<Return>", self.tp_confirmation_validation)
        self.password_field.bind("<BackSpace>", self.clear_tp)
        self.window.mainloop()

    # Validates the password.
    def tp_testing_validation(self, event):
        password = self.password_field.get()
        self.password_val(password)
        try:
            the_con, msg = self.password_val(password)     
            if the_con:
                self.passwords.append(password)    
                self.test_count-=1
                msg = "***CONGRATULATIONS***\n\n6 attempts completed! Thank you" if self.test_count==0 else 'Attempts left = '+str(self.test_count) 
            self.password_field.delete(0, END)
        except Exception as ep:
            tkinter.messagebox.showerror('error', ep)   

        tkinter.messagebox.showinfo('message', msg)
        
        if self.test_count==0:
            self.window.destroy()

    # Confirm password function
    def testing_passwords(self):
        self.create_window("CONFIRMING TAP PASSWORDS")
        img = PhotoImage(file=self.background_path)
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        l1 = tk.Label(self.window, text='STATUS: Testing Passwords', fg='Black').pack(side=TOP, anchor=NW)
        tk.messagebox.showinfo("Instructions", "You are going to enter the created tap password 6 times\n\nOnces entered you will not have a chance to change it\n\nA couunt for number of attempts left will be displayed after every entry\n\nGood Luck, press Ok to start test.")
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
        self.password_field.focus_force()
        self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
        self.password_field.bind("<Return>", self.tp_testing_validation)
        self.password_field.bind("<BackSpace>", self.clear_tp)
        self.window.mainloop()

    # Function to get the list of passwords
    def get_passwords(self):
        return self.passwords

    # Function to get the set password:
    def get_password(self):
        return self.password




pr = PasswordRetriever()
pr.create_password()
print(pr.get_password())
pr.confirm_password()
print("Password confirmed")
pr.testing_passwords()
print("Passwords:",pr.get_passwords())