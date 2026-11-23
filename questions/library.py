from enum import Enum

class Status(Enum):

    BORROWED = 'borrowed'
    AVAILABLE = 'available'


class Book:

    def __init__(self, name, id: int, status: Status):
        self.name = name
        self.author_id : int = id
        self.status: Status = status


    def __repr__(self):
        return (f"Book(id:{self.author_id}:{self.name}:{self.status})")


class Member:

    def __init__(self, name, id:int):
        self.name = name
        self.member_id : int = id


    def __str__(self):
            return f"{self.name}" 


    def __repr__(self):
            return (f"Member(id:{self.member_id}:{self.name})")
        
class Library:

    def __init__(self, books: list[Book], members: list[Member]):
        self.books: list[Book] = books
        self.members: list[Member] = members

       
    def add_book(self, name, id):
         for book in self.books:
            if book.author_id == id:
                return f'ALREDY A BOOK WITH SAME ID USE ANOTHER ID'

            new_book = Book(name, id, Status.AVAILABLE)
            self.books.append(new_book)
            return f"{new_book.author_id}{new_book.name} ADDED WITH CURRENT STATUS {new_book.status}"


    def add_member(self, name, id):
         for member in self.members:
            if member.member_id == id:
                return f'YOU ARE ALREADY A MEMBER OF LIBRARY'

            new_member = Member(name, id)
            self.members.append(new_member)
            return f"ADDED NEW MEMBER WITH ID {new_member.member_id}:{new_member.name} "
            


if __name__ == "__main__":

    book_1 = Book('wonderland', 1, Status.AVAILABLE)
    book_2 = Book('tarzan', 2, Status.AVAILABLE)
    member = Member('max', 1)
    library = Library([book_1, book_2], [member])
    library.add_book('Lion-King', 3)
    library.add_member('jack', 2)

    print(library.books)
    print(library.members)
    print()


    

        