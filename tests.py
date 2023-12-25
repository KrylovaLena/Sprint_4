import pytest
from main import BooksCollector

class TestBooksCollector:

    '''Проверка добавления двух новых книг в коллекцию.'''
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    '''Добавление новой книги с разными валидными названиями в коллекцию.'''
    @pytest.mark.parametrize("name", ["Эпоха невинности", "I", "Палата №6"])
    def test_add_new_book_add_three_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()


    '''Повторное добавление книги с тем же названием в коллекцию.'''
    def test_add_new_book_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = "Смерть Артемио Круса"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    '''Добавление новой книги с граничными значениями входных данных.'''
    @pytest.mark.parametrize("book_title, expected_result", [
        ("", False),  # пустое название (длина названия = 0)
        ("А" * 41, False),  # название длиной в 41 символ
        ("А" * 42, False),  # название длиной в 42 символа
        ("А", True),  # название длиной в 1 символ
        ("А"*2, True),  # название длиной в 2 символа
        ("А" * 39, True),  # название длиной в 39 символов
        ("А" * 40, True),  # название длиной в 40 символов
    ])
    def test_add_new_book_boundary_values_of_the_input_data(self, book_title, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        assert (book_title in collector.get_books_genre()) == expected_result

    '''Жанр книги правильно сохраняется в словаре. books_genre.'''
    def test_set_book_genre_the_genre_is_correctly_saved_in_the_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин Колец")
        collector.set_book_genre("Властелин Колец", "Фантастика")
        assert collector.get_book_genre("Властелин Колец") == "Фантастика"

    '''Жанр книги не устанавливается, если выбранного жанра нет в списке genre.'''
    def test_set_book_genre_genre_is_missing(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин Колец")
        collector.set_book_genre("Властелин Колец", "Сказка")
        assert collector.get_book_genre("Властелин Колец") == ''

    '''Жанр книги не устанавливается, если книги не существует в коллекции.'''
    def test_set_book_genre_genre_is_not_set(self):
        collector = BooksCollector()
        collector.set_book_genre("Властелин Колец", "Фантастика")
        assert "Властелин Колец" not in collector.get_books_genre()

    '''Возвращается правильный жанр книги, если задана существующая книга.'''
    def test_get_book_genre_existing_book(self, collector):
        genre = collector.get_book_genre("Властелин Колец")
        assert genre == "Фантастика"

    '''Тестирование что жанр возвращается None т.к. книга в списке отсутствует.'''
    def test_get_book_genre_nonexistent_book(self, collector):
        genre = collector.get_book_genre("Дюна")
        assert genre is None

    '''Возвращается пустой жанр книги, если у книги не указан жанр.'''
    def test_get_book_genre_empty_genre(self, collector):
        genre = collector.get_book_genre("Смерть Артемио Круса")
        assert genre == ""

    '''Возвращаются все книги заданного жанра.'''
    def test_get_books_with_specific_genre_one_genre(self, collector):
        genre = "Комедии"
        expected_books = ["Ревизор", "Чайка"]
        actual_books = collector.get_books_with_specific_genre(genre)
        assert actual_books == expected_books

    '''При отсутствии книг заданного жанра, возвращается пустой список.'''
    def test_get_books_with_specific_genre_no_result(self, collector):
        genre = "Сказка"
        expected_books = []
        actual_books = collector.get_books_with_specific_genre(genre)
        assert actual_books == expected_books

    '''При указании недопустимого жанра возвращается пустой список книг.'''
    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        genre = "Мультфильмы"
        expected_books = []
        actual_books = collector.get_books_with_specific_genre(genre)
        assert actual_books == expected_books

    '''Метод возвращает правильное значение жанра для добавленной книги.'''
    def test_get_books_genre_correct_value(self, collector):
        books_genre = collector.get_books_genre()
        assert books_genre["Властелин Колец"] == "Фантастика"

    '''Метод get_books_for_children() возвращает список книг без жанров "Ужасы" и "Детективы".'''
    def test_get_books_for_children_no_books_for_children_with_horror_and_detective_genre(self, collector):
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ["Властелин Колец", "Ревизор", "Чайка"]

    '''После добавления книги в избранное она действительно находится в списке избранных книг.'''
    def test_add_book_in_favorites_book_added_to_favorites(self, collector):
        book_name = "Ревизор"
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()


    '''Метод add_book_in_favorites() не добавляет в избранное книгу, которой нет в списке books_genre.'''
    def test_add_book_in_favorites_book_not_in_genre(self, collector):
        book_name = "Палата №6"
        collector.add_book_in_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    '''Метод delete_book_from_favorites() удаляет из избранного книгу, которая там находилась.'''
    def test_delete_book_from_favorites_should_remove_book(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    '''Метод delete_book_from_favorites() не удаляет из избранного (не меняет список) книгу, которой там не было.'''
    def test_delete_book_from_favorites_new_should_not_remove_nonexistent_book(self, collector):
        collector.favorites = ["Властелин Колец", "Институт", "Чайка"]
        book_name = "Палата №6"
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites and len(collector.favorites) == 3

    '''Тестирование что метод get_list_of_favorites_books возвращает список всех книг из списка избранных.'''
    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ["Властелин Колец", "Институт", "Чайка"]
        expected_favorites = collector.favorites
        actual_favorites = collector.get_list_of_favorites_books()
        assert actual_favorites == expected_favorites
