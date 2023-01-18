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


class Library:
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.

        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.

        :return: Идентификатор для добавления новой книги в библиотеку.
        """

        if not self.books:
            return 1

        last_book = self.books[-1]
        next_id = last_book.id + 1
        return next_id

    def get_index_by_book_id(self, id_: int):
        """
            Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.

            Если книга существует, то вернуть индекс из списка.
            Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"

            :param id_: Идентификатор запрашиваемой книги.

            :raise ValueError: Ошибка, если запрашиваемой книги нет.

            :return: Индекс, по которому можно получить доступ к книге
            """
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")







if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
