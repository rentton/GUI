from tkinter import *

#We have to define the principal screen
root = Tk()
root.title("Using radio buttons")

#Defining the principal frame in the screen
my_frame = Frame()
my_frame.pack()

option = IntVar()

def get():
    print(option.get())
    if option.get() == 1:
        result.config(text="hello, male")
    elif option.get() == 2:
        result.config(text="hello, female")
    
    
    

rb1 = Radiobutton(my_frame, text="Male", variable=option, value=1, command = get)
rb1.pack()
rb2 = Radiobutton(my_frame, text="Female", variable=option, value=2, command = get)
rb2.pack()

result = Label(my_frame,text="")
result.pack()

root.mainloop()

