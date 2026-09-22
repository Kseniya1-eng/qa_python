# BooksCollector Test Suite

Проект содержит Unit-тесты для класса `BooksCollector` с использованием `pytest`.

## Обзор тестов

Все тесты находятся в одном классе `TestBooksCollector`.

### Тесты для add_new_book (4 теста)

- `test_add_new_book` — `add_new_book`: Добавление новой книги
- `test_add_new_book_duplicate_fails` — `add_new_book`: Попытка добавить уже существующую книгу
- `test_add_new_book_name_too_long_fails` — `add_new_book`: Попытка добавить книгу с именем > 40 символов
- `test_add_new_book_empty_name_fails` — `add_new_book`: Попытка добавить книгу с пустым именем

### Тесты для set_book_genre (3 теста)

- `test_set_book_genre` — `set_book_genre`: Установка жанра для книги
- `test_set_book_genre_invalid_genre_fails` — `set_book_genre`: Установка несуществующего жанра
- `test_set_book_genre_unknown_book_fails` — `set_book_genre`: Установка жанра для несуществующей книги

### Тесты для get_books_with_specific_genre (4 теста)

- `test_get_books_with_specific_genre` — `get_books_with_specific_genre`: **Параметризованный тест** — проверка для жанров "Фантастика", "Комедии", "Ужасы"
- `test_get_books_with_unknown_genre_returns_empty` — `get_books_with_specific_genre`: Запрос несуществующего жанра

### Тесты для get_books_for_children (2 теста)

- `test_get_books_for_children_excludes_age_rated` — `get_books_for_children`: Возврат книг без возрастного рейтинга
- `test_get_books_for_children_empty_without_genre` — `get_books_for_children`: Книги без жанра не попадают в список

### Тесты для избранного (5 тестов)

- `test_add_book_in_favorites` — `add_book_in_favorites`: Добавление книги в избранное
- `test_add_book_in_favorites_not_in_collection_fails` — `add_book_in_favorites`: Добавление несуществующей книги
- `test_add_book_in_favorites_duplicate_fails` — `add_book_in_favorites`: Повторное добавление в избранное
- `test_delete_book_from_favorites` — `delete_book_from_favorites`: Удаление из избранного
- `test_delete_book_from_favorites_not_in_favorites` — `delete_book_from_favorites`: Удаление несуществующей книги
- `test_get_list_of_favorites_books` — `get_list_of_favorites_books`: Получение списка избранного

## Итого

- **Всего тестов:** 19
- **Параметризованные тесты:** 1 (3 варианта данных)
- **Покрываются методы:** все 8 методов класса

## Запуск

```bash
pytest -v tests.py
```
