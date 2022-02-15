import tkinter as tk
from tkinter import *
import tkinter
from turtle import width
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")
window.geometry("600x400")

img = PhotoImage(file="b.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0,relwidth=1, relheight=1)
# You will create two text labels namely 'username' and 'password' and and two input labels for them

# tkinter.Label(window, text = "Username").grid(row = 0) #'username' is placed on position 00 (row - 0 and column - 0)

# # 'Entry' class is used to display the input-field for 'username' text label
# tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

# tkinter.Label(window, text = "Password").place(x=30,y=50) #'password' is placed on position 10 (row - 1 and column - 0)

password_field = tkinter.Entry(window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
password_field.place(relx=0.5, rely=0.40, anchor=CENTER)

enteries = []

def showPass(event):
    print(password_field.get())
    password_field.delete(0, END)
    enteries.append(password_field.get())

def clear_text(event):
   password_field.delete(0, END)

password_field.bind("<Return>", showPass)
password_field.bind("<BackSpace>", clear_text)

window.mainloop()


# class PasswordRetriever():
    
#     def __init__ (self):
        
#         self.passwords = []
#         self.num_enteries = len(self.passwords)
        
#         self.window = tkinter.Tk()
#         self.window.title("GUI")
#         self.window.geometry("600x400")
#         img = PhotoImage(file="./b.png")
#         label = Label(
#             self.window,
#             image=img
#         )
#         label.place(x=0, y=0,relwidth=1, relheight=1)
#         self.password_field = tkinter.Entry(self.window, show="\u2022", font=("Helvetica, 28"), background='#BDBDBD', bd=0, justify='center') #second input-field is placed on position 11 (row - 1 and column - 1)
#         self.password_field.place(relx=0.5, rely=0.40, anchor=CENTER)
#         self.password_field.bind("<Return>", self.add_pd())
#         self.window.mainloop()

        


#     def add_pd(self):
#         self.passwords.append(self.password_field.get())

#     def get_passwords(self):
#         return self.passwords

#     def get_window(self):
#         return self.window
# # window.mainloop()

# pr = PasswordRetriever()
# print(pr.get_passwords())