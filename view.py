
from tkinter import Frame, Tk, Button, Label, Canvas, NW, CENTER
from random_numbers import GetRandomValues
from PIL import Image, ImageTk

class ViewGame(Frame):

    def create_random_number(self):
        randomNumber = GetRandomValues()
        return randomNumber.test()
        
    def throw_dice(self):
        number = self.create_random_number()
        if number==1:
            self.img = ImageTk.PhotoImage(Image.open("img/1.jpg"))
            self.createWidgetsImg(self.img)
        elif number==2:
            self.img = ImageTk.PhotoImage(Image.open("img/2.jpg"))
            self.createWidgetsImg(self.img)
        elif number==3:
            self.img = ImageTk.PhotoImage(Image.open("img/3.jpg"))
            self.createWidgetsImg(self.img)
        elif number==4:
            self.img = ImageTk.PhotoImage(Image.open("img/4.jpg"))
            self.createWidgetsImg(self.img)
        elif number==5:
            self.img = ImageTk.PhotoImage(Image.open("img/5.jpg"))
            self.createWidgetsImg(self.img)
        elif number==6:
            self.img = ImageTk.PhotoImage(Image.open("img/6.jpg"))
            self.createWidgetsImg(self.img)

        
    
    def createWidgetsButton(self):
        btn = Button(root, text="Lanzar Dados", width=20, command=self.throw_dice)
        btn.grid(row=0, column=2)

   
    def createWidgetsImg(self, img):
        canvas = Canvas(root, width=150, height = 150, bg="#F3F3F3")
        canvas.pack()
        
        canvas.create_image(20, 20, anchor=NW, image=img)
        canvas.grid(row=1, column=2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgetsButton()

root = Tk()
app = ViewGame(master=root)
root.wm_title("Lanzar Dados")
root.geometry("200x200")
root.wm_resizable(False, False)
root.mainloop()