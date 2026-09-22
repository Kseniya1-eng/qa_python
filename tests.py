import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покроем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # === Тесты для add_new_book ===

    def test_add_new_book(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Гарри Поттер')

        # проверяем, что книга добавлена
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_add_new_book_duplicate_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем одну и ту же книгу дважды
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')

        # проверяем, что в словаре только одна книга
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_too_long_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу с именем длиннее 40 символов
        long_name = 'A' * 41
        collector.add_new_book(long_name)

        # проверяем, что книга не добавлена
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # пытаемся добавить книгу с пустым именем
        collector.add_new_book('')

        # проверяем, что книга не добавлена
        assert '' not in collector.get_books_genre()

    # === Тесты для set_book_genre и get_book_genre ===

    def test_set_book_genre(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и устанавливаем жанр
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        # проверяем, что жанр установлен правильно
        assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_set_book_genre_invalid_genre_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и пытаемся установить несуществующий жанр
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Романтика')

        # проверяем, что жанр не изменился
        assert collector.get_book_genre('Гарри Поттер') == ''

    def test_set_book_genre_unknown_book_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # пытаемся установить жанр для несуществующей книги
        collector.set_book_genre('Неизвестная книга', 'Фантастика')

        # проверяем, что книга не появилась в словаре
        assert 'Неизвестная книга' not in collector.get_books_genre()

    # === Тесты для get_books_with_specific_genre (параметризованные) ===

    @pytest.mark.parametrize('genre,expected_count', [
        ('Фантастика', 2),
        ('Комедии', 1),
        ('Ужасы', 0),
    ])
    def test_get_books_with_specific_genre(self, genre, expected_count):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем и распределяем книги по жанрам
        collector.add_new_book('Дюна')
        collector.add_new_book('Интерстеллар')
        collector.add_new_book('Брильянтовая рука')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Интерстеллар', 'Фантастика')
        collector.set_book_genre('Брильянтовая рука', 'Комедии')

        # проверяем количество книг с заданным жанром
        assert len(collector.get_books_with_specific_genre(genre)) == expected_count

    def test_get_books_with_unknown_genre_returns_empty(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу с жанром
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        # запрашиваем несуществующий жанр
        books = collector.get_books_with_specific_genre('Романтика')

        # проверяем, что вернулся пустой список
        assert books == []

    # === Тесты для get_books_for_children ===

    def test_get_books_for_children_excludes_age_rated(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книги с разными жанрами
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Сияние')
        collector.add_new_book('Брильянтовая рука')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Брильянтовая рука', 'Мультфильмы')

        # получаем список книг для детей
        books = collector.get_books_for_children()

        # проверяем, что книги с возрастным рейтингом исключены
        assert 'Гарри Поттер' in books
        assert 'Брильянтовая рука' in books
        assert 'Сияние' not in books

    def test_get_books_for_children_empty_without_genre(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу без жанра
        collector.add_new_book('Неизвестная книга')

        # проверяем, что список книг для детей пуст
        assert collector.get_books_for_children() == []

    # === Тесты для избранного ===

    def test_add_book_in_favorites(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и добавляем в избранное
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_book_in_favorites('Дюна')

        # проверяем, что книга в избранном
        assert 'Дюна' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_collection_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # пытаемся добавить несуществующую книгу в избранное
        collector.add_book_in_favorites('Неизвестная книга')

        # проверяем, что книга не добавлена
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_fails(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и добавляем в избранное дважды
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        # проверяем, что книга в избранном только один раз
        assert collector.get_list_of_favorites_books().count('Дюна') == 1

    def test_delete_book_from_favorites(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу в избранное и удаляем
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')

        # проверяем, что книга удалена из избранного
        assert 'Дюна' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу, но не в избранное, и пытаемся удалить
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.delete_book_from_favorites('Дюна')

        # проверяем, что список избранного остался пустым
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книги и помещаем их в избранное
        collector.add_new_book('Дюна')
        collector.add_new_book('Брильянтовая рука')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Брильянтовая рука', 'Комедии')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Брильянтовая рука')

        # проверяем список избранного
        favorites = collector.get_list_of_favorites_books()
        assert 'Дюна' in favorites
        assert 'Брильянтовая рука' in favorites
