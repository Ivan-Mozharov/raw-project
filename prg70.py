# Обработчик изображений

from tkinter import *  # подключаем все элементы Tkinter
from tkinter import filedialog  # файловый диалог

from PIL import Image, ImageTk, ImageFilter, ImageEnhance


def photoImage(file):
    pass


class App:

    def __init__(self): # Конструктор
        self.root = Tk() #корневой элемент
        self.root.title('Обработка изображений')
        self.root.geometry('800x600') # Размеры окна
        self.root.resizable(False, False) # Фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.label = Label(text='Работаем с картинками',
                           background='#f0f',
                           foreground='green',
                           font=('Verdana', 16))
        self.label.pack() # размещение надписи
        self.canvas = Canvas(bg='black', width=600, height=400)
        self.canvas.pack(anchor=CENTER, pady=20)
        # кнопка загрузки
        self.btn = Button(text='Загрузить', command=self.load)
        self.btn.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)
        # кнопка отражения по горизонтали
        self.flp = Button(text='Отразить', command=self.flip)
        self.flp.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)
        # Резкость
        self.shrp = Button(text='Резкость', command=self.sharp)
        self.shrp.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)
        # Размыть
        self.blur = Button(text='Размыть', command=self.blur)
        self.blur.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)
        # Оригинал
        self.orig = Button(text='Оригинал', command=self.back)
        self.orig.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)
        # поменять фон
        self.rect_btn = Button(text='Поменять фон', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=30, fill=X, expand=True)

        # self.btn.bind('<ButtonPress-1>', self.load)
        self.left, self.top = 0, 0 # тщчки привязки к холсту
        self.image = None
        self.empty = Image.new('RGB',(600, 400), (255, 255, 255)) #пустышка
        self.root.mainloop()

    def load(self):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./',
                                                  filetypes=(
                                                      ('All', '*.*'),
                                                      ('JPEG', '*.jpg'),
                                                      ('PNG', '*.png')
                                                  )) # диалог открытия картинки
            self.empty = Image.open(fullpath)
            mode = self.empty.mode  # получаем цветовую схему
            if mode == 'P':  # 256-color index image
                self.empty = self.empty.convert('RGB')
            w,h = self.empty.size # Подгоняем картинку по ширине холсята
            self.left, self.top = 0, 0

            if w > 600:
                ratio = w / 600
                h = int(h/ratio)
                w = 600
                self.empty = self.empty.resize((w, h))
                if h < 400:
                    self.left, self.top = 0, (400 - h) // 2
                else:
                    self.left, self.top = 0, 0

            else:
                self.left = (600 - w) // 2
                self.top = (400 - h) // 2
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)
        except AttributeError:  # не удалось подгрузить
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0,0, anchor=NW, image=self.image)

    # Функционал кнопки отразить
    def flip(self):
        flp_img = self.empty.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.image = ImageTk.PhotoImage(flp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

    # Фунционал кнопки "Размытия"
    def blur(self):
        blur_img = self.empty.filter(ImageFilter.GaussianBlur(5))
        self.image = ImageTk.PhotoImage(blur_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

 # Фунционал кнопки "Резкость"
    def sharp(self):
        sharper = ImageEnhance.Sharpness(self.empty)
        sharp_img = sharper.enhance(5.0)
        self.image = ImageTk.PhotoImage(sharp_img)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

    # Функционал кнопки "к оригиналу"
    def back(self):
        self.image = ImageTk.PhotoImage(self.empty)
        self.canvas.create_image(self.left, self.top, anchor=NW, image=self.image)

    # Фунционал кнопки "поменять фон"
    def make_rect(self):
        self.canvas.create_rectangle(0, 0, 600, 400,
                                     outline='#004D40',
                                     fill='red',
                                     width=7)


app = App()