from typing import Optional
from pydentic import BaseModel


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id=int, name=str, pages=int):
        if not isinstance(id, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Названиет книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")
        self.pages = pages


class Library(BaseModel):
    books: Optional[List[Book]]

    def get_next_book_id(self, ):
        books_dict = {}

        for id in Book:
            if id in books_dict:
                graders_dict[grade] += 1  # оценку уже встречали, поэтому увеличиваем количество
            else:
                graders_dict[grade] = 1  # оценку встретили 1 раз

    def get_index_by_book_id(self):
        book_dict = {}
        
        for index in books:
            if not books:
                print("Книги с запрашиваемым id не существует")
            else:







if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
