from tkinter import *

#We have to define the principal screen
root = Tk()
root.title("Hello World!")
#To upload an image as icon (up-left part)
root.iconbitmap("icono.ico")
root.geometry("960x540")

#Defining the principal frame in the screen
my_frame = Frame()
my_frame.pack()
my_frame.config(width="900",height="500")
my_frame.config(background="pink")
my_frame.config(cursor="hand2")

""" #Defining the labels
label1 = Label(my_frame,text="Hello World!", font=("Comic Sans MS",20))
label1.place(x=100,y=200)


#Uploading an image
im = PhotoImage(file="ima.png")
label2 = Label(my_frame,image=im)
label2.place(x=200,y=100)
 """



label3 = Label(my_frame,text="Name:")
#Grid divide the screen in squares, in each one 
# is possible to define one label
#Sticky allows locate the label in the frame (e.j. e = "east")
#padx allows create borders
label3.grid(row=0,column=0, sticky="e", padx=10,pady=10)

my_name = StringVar() 

inp = Entry(my_frame, textvariable=my_name)
inp.grid(row=0,column=1,sticky="e", padx=10,pady=10)

label4 = Label(my_frame,text="Text:")
label4.grid(row=1,column=0,sticky="e", padx=10,pady=10)

text = Text(my_frame,width=15,height=5)
text.grid(row=1,column=1,sticky="e", padx=10,pady=10)

scroll = Scrollbar(my_frame,command=text.yview)
scroll.grid(row=1,column=2, sticky="nsew")

text.config(yscrollcommand=scroll.set)

def button_code():
    my_name.set("Pepe")

button = Button(my_frame, text = "Check", command=button_code)
button.grid(row=2,column=0,sticky="e",padx=10,pady=10)


#!For password for example when we write characters, we see *****
# cin.config(show="*")


root.mainloop()

