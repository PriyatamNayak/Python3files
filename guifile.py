from tkinter import * 
from tkinter import filedialog

def callback():
     name= "\n"+ filedialog.askopenfilename(initialdir = "/", title ="select file")
     print (name)
     txt.insert(END,name)

def callback1():
     name= filedialog.asksaveasfilename(initialdir = "/", title ="select file")
     print (name)


def show_data():
     txt.delete(1.0, END)
     txtname = e1.get()
     print(str(txtname))
     output = 'Hello, ' + str(txtname)+ '\nHow are you? '
     txt.insert(0.0, output)


          

root= Tk()
root.title("gui")
root.geometry("300x400")
name = Label(root, text = "name")
name.grid(row= 0)

e1 = Entry(root, bd = 5)
e1.grid(row= 0, column = 1)

b1 = Button(root, text = "submit" , highlightcolor="blue", command= show_data)
b1.grid(row = 1,  column=0, pady= 4)

b2 = Button(root, text = 'File Open', command= callback)
b2.grid(row = 1, column =1, pady= 4 ,sticky = W)

b3 = Button(root, text = 'Save File', command= callback1)
b3.grid(row = 1, column =1, pady= 4, sticky = E)

txt = Text(root, width=25, height = 10, wrap = WORD)
txt.grid(row = 2, columnspan = 2, sticky = W)

root.mainloop()
