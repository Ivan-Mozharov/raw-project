# Обработчик изображений

from tkinter import  * # подключаем все элементы Tkinter

class App:

    def __init__(self):

        self.root = Tk()
        self.root.title('Обработка изображений')
        self.root.geometry('800x600') # Размеры окна
        self.root.resizable(False, False) # Фиксируем габариты
        self.label = Label(text='Работаем с картинками')
        self.label.pack() # размещение надписи
        self.btn = Button(text='Заменить')
        self.btn.pack()
        self.btn.bind('<ButtonPress-1>', self.click)
        self.root.mainloop()

    def click(self, event):
       self.btn['text'] = 'Заменено'
       self.label['text'] = 'Здесь будет картинка'




app = App()