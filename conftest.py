@pytest.fixture
    def collector(self):
        collector = BooksCollector()
        collector.books_genre = {
            "Властелин Колец": "Фантастика",
            "Смерть Артемио Круса": "",
            "Ревизор": "Комедии",
            "Чайка": "Комедии",
            "Дом на холодном холме": "Ужасы",
            "Институт": "Ужасы",
            "Шерлок Холмс": "Детективы",
        }
        return collector