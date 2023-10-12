from tkinter import *
import random
class Application:
    def __init__(self, root):
        self.root = root
        root.title("idk")
        root.geometry("200x200")
        #now widgets
        self.label = Label(text=("Button clicks"))
        self.label.pack()
        self.label2 = Label(text=(""))
        self.label2.pack()
        self.bttn = Button(text="click", command=self.onbttnclick)
        self.bttn.pack()
        self.x= int(0)
        self.y = random.randint(1,10)
    def onbttnclick(self):
        self.label.config(text=("clicks :",self.x))
        self.x +=1
        if self.x == self.y:
            self.label2.config(text="You are lucky if you get this number in your lottery ticket.")
        elif self.x !=self.y:
            self.label2.config(text="")
            
root = Tk()
app = Application(root)
root.mainloop()