from typing import List
from InputManager import menuInput

def showMenu() -> None:
    #Список функций программы
    menu: List[str] = ["1. Отобразить книги", "2. Добавить книгу", "3. Найти книгу", "4. Удалить книгу", "5. Изменение статуса книги", "0. Выход"]
    print()
    for option in menu:
        print(option)


#Отображение меню
showMenu()
while menuInput():
    #Отображение меню
    showMenu()