from typing import Dict, List, Union
import JSONManager

def showBooksAsTable(books: List[Dict[str, Union[str, int]]]) -> None:
    print()
    #Получение максимальной длины каждого столбца таблицы, для красивого отображения списка книг
    max_id_len: int = max(len(str(books[-1]["id"])), 2)
    max_author_len: int = 6
    max_title_len: int = 5
    max_year_len: int = 5
    for book in books:
        author_len: int = len(book["author"])
        title_len: int = len(book["title"])
        max_author_len = max(author_len, max_author_len)
        max_title_len = max(title_len, max_title_len)

    #Составление заголовка таблицы
    table_header: str = "id" + " "*(max_id_len+1-2) + "| author" + " "*(max_author_len+1-6) + "| title" + " "*(max_title_len+1-5) + "| year" + " "*(max_year_len+1-4) + "| status"
    print(table_header)
    print("-"* (len(table_header) + 2))
    #Отображение книг
    for book in books:
        book_id: str = str(book["id"])
        author: str = book["author"]
        title: str = book["title"]
        year: str = str(book["year"])
        status: str = book["status"]
        row: str = book_id + " "*(max_id_len+1-len(book_id)) + "| " + author + " "*(max_author_len+1-len(author)) + "| " + title + " "*(max_title_len+1-len(title)) + "| " + year + " "*(max_year_len+1-len(year)) + "| " + status
        print(row)

def showAllBooks() -> None:

    #Получение всех книг
    books: List[Dict[str, Union[str, int]]] = JSONManager.getAllBooks()

    #Проверка, на случай если книг не загружено
    if len(books) == 0:
        print("Не загружено ни одной книги")
        return

    #Отображение книг в таблице
    showBooksAsTable(books)

def getBooksByKey(key: str) -> None:

    #Получение всех книг
    books: List[Dict[str, Union[str, int]]] = JSONManager.getAllBooks()
    matched_books: List[Dict[str, Union[str, int]]] = []
    #Поиск совпадений по автору, названию или году
    for book in books:
        author: str = book["author"]
        title: str = book["title"]
        year: str = str(book["year"])
        if (author == key) or (title == key) or (year == key):
            matched_books.append(book)

    #Результат если книг не найдено
    if len(matched_books) == 0:
        print("Не найдено совпадений")
        return

    #Отображение найденных книг в таблице
    showBooksAsTable(matched_books)

def addBook(author: str, title: str, year: int) -> None:
    book_id: int = JSONManager.get_books_quantity() + 1
    status: str = "in stock"

    #Получение всех книг
    books: List[Dict[str, Union[str, int]]] = JSONManager.getAllBooks()
    #Присваивание значений
    book: Dict[str, Union[str, int]] = {"id": book_id, "author": author, "title": title, "year": year, "status": status}
    #Добавление книги
    books.append(book)
    JSONManager.updateFile({"books": books})

def removeBook(book_id: int) -> None:
    #Получение всех книг
    books: List[Dict[str, Union[str, int]]] = JSONManager.getAllBooks()
    #Удаление книги из списка по id
    del books[book_id-1]
    for i in range(book_id-1, JSONManager.get_books_quantity() - 1):
        books[i]["id"] -= 1
    #Обновление списка книг
    JSONManager.updateFile({"books": books})

def changeStatus(book_id: int, status: str) -> None:
    #Получение всех книг
    books: List[Dict[str, Union[str, int]]] = JSONManager.getAllBooks()
    #Замена статуса книги
    books[book_id-1]["status"] = status
    #Обновление списка книг
    JSONManager.updateFile({"books": books})