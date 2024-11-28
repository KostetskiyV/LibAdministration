from typing import Union
from LibraryController import showAllBooks, getBooksByKey, addBook, removeBook, changeStatus
from JSONManager import get_books_quantity

def addBookInput() -> None:
    title: str = input("Введите название: ")
    #Проверка ввода на пустоту
    if len(title) == 0:
        print("Пустой ввод")
        return
    author: str = input("Введите автора книги: ")
    if len(author) == 0:
        print("Пустой ввод")
        return

    year: Union[str, int] = input("Введите год написания книги: ")
    #Проверка введённого года написания
    if year.isdigit():
        year = int(year)
        if year > 2024 or year < -9999:
            print("Введён несуществующий год.")
            return
    else:
        print("Некорректный ввод.")
        return
    addBook(author, title, year)

def findBookInput() -> None:
    key: str = input("Введите название искомой книги, автора или год написания: ")
    if len(key) == 0:
        print("Пустой ввод")
        return
    #Поиск книги по указанному ключу
    getBooksByKey(key)

def removeBookInput() -> None:
    
    #Получение количества книг
    books_quantity: int = get_books_quantity()
    #Проверка наличия хотя бы одной книги в базе
    if books_quantity == 0:
        print("Нет книг для удаления")
        return
    
    book_id: Union[str, int] = input(f"Введите id книги (1-{get_books_quantity()}): ")
    #Проверка введённого id
    if not book_id.isdigit():
        print("Некорректный ввод.")
        return
    book_id = int(book_id)
    if book_id <= 0 or book_id > get_books_quantity():
        print("Введён несуществующий id.")
        return

    #Удаление книги по id
    removeBook(book_id)

def changeStatusInput() -> None:
    #Получение количества книг
    books_quantity: int = get_books_quantity()
    #Проверка наличия хотя бы одной книги в базе
    if books_quantity == 0:
        print("Нет книг для изменения статуса")
        return

    book_id: Union[str, int] = input(f"Введите id книги (1-{books_quantity}): ")
    #Проверка введённого id
    if not book_id.isdigit():
        print("Некорректный ввод.")
        return
    book_id = int(book_id)
    if book_id <= 0 or book_id > books_quantity:
        print("Введён несуществующий id.")
        return

    status: str = input("Введите новый статус книги ('in stock' или 'issued'): ")
    #Проверка введённого статуса
    if status != "in stock" and status != 'issued':
        print("Некорректный ввод.")
        return

    #Присвоение нового статуса книге с указанным id
    changeStatus(book_id, status)

def menuInput() -> bool:
    inp: str = input()
    if inp == "1":
        showAllBooks()
    elif inp == "2":
        addBookInput()
    elif inp == "3":
        findBookInput()
    elif inp == "4":
        removeBookInput()
    elif inp == "5":
        changeStatusInput()
    elif inp == "0":
        return False
    else:
        print("Некорректный ввод.")
    return True
