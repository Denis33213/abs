class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        return f'Название: {self.title}, автор: {self.author}, год выпуска: {self.year}'
start=Book('Война и Мир', 'Л.Н Толстой', 2005)
print(start.get_info())

