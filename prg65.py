# GUI
# PyQt6
import tkinter
from PIL import Image, ImageTk

class App:
    def __init__(self):
         #  корневой элемент
        self.root = tkinter.Tk()

        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        # Добавляем ярлык
        self.label = tkinter.Label(self.frame, text='-->').grid(row=1,column=1)




        # добавим кнопку
        self.but = tkinter.Button(self.frame, text='Заменить', command=self.change).grid(row=1, column=2)

     # добавляем изображение на холст
        self.canvas = tkinter.Canvas(self.root, height=300, width=400)
        self.image = Image.open('images\картинка_2.jpg')
        self.photo = ImageTk.PhotoImage(self.image)
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)
        self.root.mainloop() # Ожидание действий


    #Метод change
    def change(self):
         print('Кнопка нажата')
         self.image = Image.open('images\картинка_3.jpg')
         self.photo = ImageTk.PhotoImage(self.image)
         image = self.canvas.create_image(0, 0, anchor='nw', image= self.photo)
         self.canvas.grid(row=2, column=1)


app = App()