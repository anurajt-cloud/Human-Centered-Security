import tkinter as tk
from tkinter import *
import tkinter
from turtle import width
import os.path
import csv

class PasswordRetrieverVisual():
    
    def __init__ (self):
        
        self.passwords = []
        self.set_passwords = []
        self.set_password = None
        self.password = None
        self.num_enteries = len(self.passwords)
        self.window = tkinter.Tk()
        self.min_tap_len = 8
        self.count = 0
        self.attempt = 0
        self.label_box_1 = tkinter.Label()
        self.label_box_2 = tkinter.Label()
        self.label_box_3 = tkinter.Label()
        self.label_box_4 = tkinter.Label()
        self.command_label = tkinter.Label()
        self.filename = "visual_cue_tp_data"

    # Function to clear the text in the entry field    
    def clear_tp(self, event):
        self.password_field.delete(0, END)
        
    # Runs the main tk window
    def create_tap_passwords(self):

        # Function to reset the background color of the labels
        def reset():
            self.label_box_1.config(bg='#BDBDBD')
            self.label_box_2.config(bg='#BDBDBD')
            self.label_box_3.config(bg='#BDBDBD')
            self.label_box_4.config(bg='#BDBDBD')

        # Function to change the color of the label based on character
        def callback(string_var):
            reset()
            password_string = str(string_var.get())
    
            if password_string=="":
                return None
            last_char = password_string[-1]
            if(last_char == 'f'):
                self.label_box_1.config(bg='#006400')
            elif (last_char == 'g'):
                self.label_box_2.config(bg='#006400')
            elif (last_char == 'h'):
                self.label_box_3.config(bg='#006400')
            elif (last_char == 'j'):
                self.label_box_4.config(bg='#006400')
    

        self.window.title("TAP PASSWORDS")
        self.window.geometry("1000x700")
        img = PhotoImage(master=self.window,file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        
        if self.set_password is None:
            tk.messagebox.showinfo("Instructions", "You are now going to create a tap password\n\n***You will have one attempt to create the password***\n\nAfter creating if not satisfied you can create it again.\n\nPress Ok to create the tap password.")
        elif self.password is not None and (len(self.passwords) == 0):
             tk.messagebox.showinfo("Instructions", "You are going to enter the created tap password 6 times\n\nOnces entered you will not have a chance to change it\n\nA count for number of attempts left will be displayed after every entry\n\nGood Luck, press Ok to start test.")
        
        self.label_box_1 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_1.place(relx=0.35, rely=0.70, anchor=CENTER)        
        self.label_box_2 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_2.place(relx=0.45, rely=0.70, anchor=CENTER)
        self.label_box_3 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_3.place(relx=0.55, rely=0.70, anchor=CENTER)
        self.label_box_4 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_4.place(relx=0.65, rely=0.70, anchor=CENTER)
        self.command_label = tkinter.Label(self.window, font=("Helvetica, 20"), background='#BDBDBD', bd=0)
        self.command_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        # Function to enter the password
        def enter_password():
            string_var = StringVar()
            string_var.trace("w", lambda name, index, mode, sv=string_var: callback(string_var))
            self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center', textvariable=string_var) #second input-field is placed on position 11 (row - 1 and column - 1)
            self.password_field.focus_force()
            self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
            self.password_field.bind("<Return>", self.processing_password)
            self.password_field.bind("<BackSpace>", self.clear_tp)
            
        if(self.password is not None):
            self.command_label.config(text='STATUS: Testing password')
        elif(self.set_password is not None):
            self.command_label.config(text='STATUS: Confirming password')
        else:
            self.command_label.config(text='STATUS: Creating password')
        enter_password()
        
        self.window.mainloop()
    
    def test_tap_passwords(self):
        self.window = tkinter.Tk()
        self.create_tap_passwords()
        
    # Validates the characters of the password
    def tap_password_char_check(self, password):
        char_list = ["f", "g", "h", "j"]
        matched_char_list = [characters in char_list for characters in password]
        return all(matched_char_list)

    # Validates the password with respect to its length.
    def tap_password_validation(self, password):
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
                        self.password_field.delete(0, END)
                        return True, msg
                    else:
                        msg = 'Password characters incorrect. Only Tap the specified keys.'
                        self.password_field.delete(0, END)
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        return False, msg

    # Function to confirm password
    def confirm_password_message(self):
        return tk.messagebox.askyesno(title='Confirmation',message='Are you satisfied with the password?')

    # Function to allow user to consecutively enter password 5 times
    def confirm_password(self, password):
        if(self.count == 4):
            msg = "PASSWORD CONFIRMED! 5 consecutive attempts reached."
            tkinter.messagebox.showinfo('message', msg)
            self.password = self.set_password
            self.window.destroy()
        else:
            validation_value, validation_msg = self.tap_password_validation(password) 
            if (validation_value):
                if (password == self.set_password):
                    self.count += 1
                    msg = 'CORRECT! Consecutive count = '+str(self.count) 
                else:
                    self.count = 0
                    msg = 'INCORRECT! Consecutive count RESET = '+str(self.count)  
            else:
                self.count = 0
                msg = 'INCORRECT! Consecutive count RESET = '+str(self.count) + "\n" + validation_msg 
            tkinter.messagebox.showinfo('message', msg)

    # Function to check the password for correctness
    def check_password(self, password):
        return self.password == password

    # Function for processing the password
    def processing_password(self, event):
        password = self.password_field.get()
        self.password_field.delete(0, END)
        if(self.set_password is None):
            if (self.tap_password_validation(password) and (self.confirm_password_message())):
                msg = 'Success!\nNOW enter the correct password 5 consecutive time to confirm the password.'
                tkinter.messagebox.showinfo('message', msg)
                self.set_password = password
                self.set_passwords.append(password)
            self.create_tap_passwords()
        elif(self.password is None):
                self.confirm_password(password)
                self.set_passwords.append(password)
        else:
            if(self.check_password(password)):
                self.attempt += 1
                msg = "Password is correct. Thank you for participating!"
                tkinter.messagebox.showinfo('message', msg)
                self.window.destroy()
            elif(not self.check_password(password) and self.attempt<6):
                self.attempt += 1
                msg = 'Password is incorrect. Attempts left = '+ str(6 - self.attempt)
            else:
                msg = 'Sorry! You are out of attempts.'
            tkinter.messagebox.showinfo('message', msg)
            self.passwords.append(password)            

    def get_filename(self):
        return self.filename+".csv"

    def create_csv(self):
        header = ["True_password", "Confirmation","Testing"]
        with open (self.filename+".csv",'a', newline='') as filedata:                             
            writer = csv.writer(filedata, dialect='excel')
            writer.writerow(header) 

    def save_data(self):
        data = [] + [self.password] + [self.set_passwords] + [self.passwords]
        with open (self.filename+".csv",'a', newline='') as filedata:                            
            writer = csv.writer(filedata, dialect='excel')
            writer.writerow(data) 
        print(data)

if __name__ == "__main__":
    pr = PasswordRetrieverVisual()
    
    pr.create_tap_passwords()
    
    pr.test_tap_passwords()

    # Creates a csv file is it does not already exist.
    if not os.path.exists(pr.get_filename()):
        pr.create_csv()
    pr.save_data()
    
