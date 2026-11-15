
class Library:

    library_name = "SRM Central Library"
    all_books = []
    total_books = 0

    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author=author
        self.price = price
        Library.all_books.append(self)

    @property
    def book_name(self):
        return self.__book_name
    @book_name.setter
    def book_name(self,value):
        if not isinstance(value,str) or not value.strip():
            raise ValueError("Book name must be a non-empty string.")
        self.__book_name=value
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self,value):
        if not isinstance(value,str) or not value.strip():
            raise ValueError("Author name must be a non-empty string.")
        self.__author=value 
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if not isinstance(value,(int,float))or value<=0:
            raise ValueError("Price must be a positive number.")
        self.__price=value

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name
        return cls.library_name

    @classmethod
    def get_total_books(cls):
        cls.total_books = len(cls.all_books)
        return cls.total_books

    @staticmethod
    def validate_price(price):
        if isinstance(price, (int, float)) and price > 0:
            return True
        else:
            return False

    @staticmethod
    def validate_book_name(name):
        if isinstance(name, str) and name.strip():
            return True
        else:
            return False

    def display_details(self):
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Library Name: {Library.library_name}")


if __name__ == "__main__":

    book1 = Library("Python Basics", "John", 500)
    book2 = Library("Java Programming", "James", 600)

    book1.display_details()

    print(Library.get_total_books())

    Library.change_library_name("SRM Digital Library")

    print(Library.library_name)

    print(Library.validate_price(500))
    print(Library.validate_book_name(""))
