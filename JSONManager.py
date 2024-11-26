from typing import Dict, List, Union
import json

#Путь к JSON-файлу
LIBRARY_PATH = "library.json"

def getAllBooks() -> List[Dict[str, Union[str, int]]]:
    
    #Проверка существования JSON-файла и создание оного, в случае отсутствия
    checkFile()

    #Считывание JSON-файла
    with open(LIBRARY_PATH, 'r') as file:
        data: Dict[str, List[Dict[str, Union[str, int]]]] = json.load(file)
    
    #Получение списка книг
    books: List[Dict[str, Union[str, int]]] = data["books"]

    return books

def updateFile(books: Dict[str, List[Dict[str, Union[str, int]]]]) -> None:

    #Запись в JSON-файл
    with open(LIBRARY_PATH, 'w') as file:
        json.dump(books, file)

def get_books_quantity() -> int:
    return len(getAllBooks())

def checkFile() -> None:
    from os.path import isfile
    if not isfile(LIBRARY_PATH):
        with open(LIBRARY_PATH, 'w') as file:
            file.write('{"books": []}')