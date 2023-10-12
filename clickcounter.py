from tkinter import *
class Application:
    def __init__(self, root):
        self.root = root
        root.title("idk")
        root.geometry("200x200")
        #now widgets
        self.label = Label(text=("Button clicks"))
        self.label.pack()
        self.bttn = Button(text="click", command=self.onbttnclick)
        self.bttn.pack()
        self.x= int(0)
    def onbttnclick(self):
        self.label.config(text=("clicks :",self.x))
        self.x +=1
root = Tk()
app = Application(root)
root.mainloop()