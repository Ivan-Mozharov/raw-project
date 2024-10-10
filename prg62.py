# Объктно - ориентировачный подход
class Ball:
    # Спец. методы
    def __init__(self, diametr, color):
        # Поля класса (члены класса)
        self.diametr = diametr
        self.color = color

# Метод класса

        def info(self):
            print('Мячь имеет цвет:', self.color)
            print('Размер мяча:', self.diametr)


ball1 = Ball(5, 'красный')
ball2 = Ball(10, 'синий')
ball3 = Ball( 20, 'зеленый')
ball4 = ball3

print(id(ball1))
print(id(ball2))
print(id(ball3))
print(id(ball4))

#print(ball1.color, ball1.diametr)
#print(ball2.color, ball2.diametr)

# ball1.diametr = 5
#
# print(ball1.diametr)