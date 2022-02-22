from tkinter import *
def quit():
    global root
    root.quit()

root = Tk()
while True:
    Button(root, text="Quit", command=quit).pack()
    root.mainloop()
    #do something
