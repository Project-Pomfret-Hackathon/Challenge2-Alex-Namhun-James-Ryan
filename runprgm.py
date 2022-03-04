from tkinter import *
import os
class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self._button = Button(self, text = "Run Program", command = self._openFile)
        self._button.grid()


    def _openFile(self):
        os.startfile(r'C:\Users\yroh1\Desktop\PP hackathon\Challenge2-Alex-Namhun-James-Ryan')

root = Tk()
root.title("RUN PROGRAM")
root.geometry("200x50")

app = Application(root)

root.mainloop()