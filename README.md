1. Тест `test_add_new_book_add_two_books`
Добавляет две книги и проверяет, что количество книг соответствует ожидаемому.
2-4. Тест `test_add_new_book_add_three_books`
Добавление новой книги с разными валидными названиями в коллекцию.
5. Тест `test_add_new_book_add_duplicate_book`
Повторное добавление книги с тем же названием в коллекцию.
6-12. Тест `test_add_new_book_boundary_values_of_the_input_data`
Добавление новой книги с граничными значениями входных данных.
 Граничные значения:
    - Пустое название книги (длина названия = 0)
    - Название книги длиной в 41 символ (максимальное значение)
    - Название книги длиной в 42 символа (превышение максимальной длины)
    - Название книги длиной в 1 символ (минимальное значение)
    - Название книги длиной в 2 символа
    - Название книги длиной в 39 символов
    - Название книги длиной в 40 символов (максимальное значение)
13. Тест `test_set_book_genre_the_genre_is_correctly_saved_in_the_dict`
Жанр книги правильно сохраняется в словаре books_genre.
14. Тест `test_set_book_genre_genre_is_missing`
Жанр книги не устанавливается, если выбранного жанра нет в списке genre.
15. Тест `test_set_book_genre_genre_is_not_set`
Жанр книги не устанавливается, если книги не существует в коллекции.
16. Тест `test_get_book_genre_existing_book`
Возвращается правильный жанр книги, если задана существующая книга.
17. Тест `test_get_book_genre_nonexistent_book`
Жанр книги возвращается None т.к. книга в списке отсутствует.
18. Тест `test_get_book_genre_empty_genre`
Возвращается пустой жанр книги, если у книги не указан жанр.
19. Тест `test_get_books_with_specific_genre_one_genre`
Возвращаются все книги заданного жанра.
20. Тест `test_get_books_with_specific_genre_no_result`
При отсутствии книг заданного жанра, возвращается пустой список.
21. Тест `test_get_books_with_specific_genre_invalid_genre`
При указании недопустимого жанра возвращается пустой список книг.
22. Тест `test_get_books_genre_correct_value`
Метод возвращает правильное значение жанра для добавленной книги.
23. Тест `test_get_books_for_children_no_books_for_children_with_horror_and_detective_genre`
Метод get_books_for_children() возвращает список книг без жанров "Ужасы" и "Детективы".
24. Тест `test_add_book_in_favorites_book_added_to_favorites`
После добавления книги в избранное она действительно находится в списке избранных книг.
25. Тест `test_add_book_in_favorites_book_not_in_genre`
Метод add_book_in_favorites() не добавляет в избранное книгу, которой нет в списке books_genre.
26. Тест `test_delete_book_from_favorites_should_remove_book`
Метод delete_book_from_favorites() удаляет из избранного книгу, которая там находилась.
27. Тест `test_delete_book_from_favorites_new_should_not_remove_nonexistent_book`
Метод delete_book_from_favorites() не удаляет из избранного (не меняет список) книгу, которой там не было.
28. Тест `test_get_list_of_favorites_books`
Тестирование что метод get_list_of_favorites_books возвращает список всех книг из списка избранных.
