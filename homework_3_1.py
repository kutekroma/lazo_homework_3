# ### Задание 1
#
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на печать Газировка и
# {ДОБАВКА} в случае наличия добавки, а иначе отобразится следующая фраза: Обычная газировка.

#Выполнил Лазо Александр
from dataclasses import dataclass

@dataclass
class Soda:
    additive: str = ""

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print(f"Обычная газировка")

if __name__ == '__main__':
    #Сода с добавкой
    limonad_with_add = Soda("zucker")
    limonad_with_add.show_my_drink()
    # Сода без добавки
    limonad_without_add = Soda()
    limonad_without_add.show_my_drink()



