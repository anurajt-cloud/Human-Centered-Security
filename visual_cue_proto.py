import tkinter as tk
from tkinter import *
import tkinter
from turtle import width

class PasswordRetriever():
    
    def __init__ (self):
        
        self.passwords = []
        self.num_enteries = len(self.passwords)
        self.window = tkinter.Tk()
        self.min_tap_len = 8
        self.label_box_1 = tkinter.Label()
        self.label_box_2 = tkinter.Label()
        self.label_box_3 = tkinter.Label()
        self.label_box_4 = tkinter.Label()
    # Function to clear the text in the entry field    
    def clear_tp(self, event):
        self.password_field.delete(0, END)

    # Runs the main tk window
    def tap_passwords(self):

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
        img = PhotoImage(file="./bg.png")
        label = Label(
            self.window,
            image=img
        )
        label.place(x=0, y=0,relwidth=1, relheight=1)
        self.label_box_1 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_1.place(relx=0.35, rely=0.70, anchor=CENTER)        
        self.label_box_2 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_2.place(relx=0.45, rely=0.70, anchor=CENTER)
        self.label_box_3 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_3.place(relx=0.55, rely=0.70, anchor=CENTER)
        self.label_box_4 = tk.Label(self.window, background='#BDBDBD', width=5, height=2)
        self.label_box_4.place(relx=0.65, rely=0.70, anchor=CENTER)
        string_var = StringVar()
        string_var.trace("w", lambda name, index, mode, sv=string_var: callback(string_var))
        self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center', textvariable=string_var) #second input-field is placed on position 11 (row - 1 and column - 1)
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
                        msg = 'Password characters incorrect. Only Tap the specified keys.'
                        self.password_field.delete(0, END)
            except Exception as ep:
                tkinter.messagebox.showerror('error', ep)
        tkinter.messagebox.showinfo('message', msg)


pr = PasswordRetriever()
pr.tap_passwords()
print(pr.get_passwords())