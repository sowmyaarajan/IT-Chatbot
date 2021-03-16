#Basic chatbot
from tkinter import *

root = Tk()


def send():
    send = "You: " + e.get()
    txt.insert(END, "\n" + send)
    if(e.get()=="hello" or e.get()=="Hello"):
        txt.insert(END, "\n"+"QualiBot: Hi")
    elif(e.get()=="hi"):
        txt.insert(END, "\n"+ "QualiBot: Hello")
    elif(e.get()=="how are you?" or e.get()=="How are you?"):
        txt.insert(END, "\n"+"QualiBot: I am fine and what about you?")
    elif(e.get()=="fine" or e.get()=="good"):
        txt.insert(END, "\n"+ "QualiBot: Nice to Hear")
    else:
        txt.insert(END, "\n"+ "QualiBot: Sorry, I did not get that")
    e.delete(0, END)
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root, text="Send",command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("QualiBot")
root.mainloop()
