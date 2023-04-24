from tkinter import *


# you create one class for GUI generally
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
        self.title("Class and Obj in GUI")

# root is replaced by self

    def status (self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var,
                               anchor="w", relief=SUNKEN)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button Clicked")

    def createbutton(self, inptext):
        Button( text=inptext , command= self.click ).pack()

if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click Me")

    window.mainloop( )

#this program implements obj oriented programming concepts
#the main class is kept clean - only four lines of code
#the gui class takes care of all func and everything in the program
#this gui class enables feature of reusability and sharing
#each team member can crete various classes and then later it is only few stmt to put them together
