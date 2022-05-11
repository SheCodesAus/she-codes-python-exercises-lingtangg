class Book:

    # properties of the Book object
    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1

    # methods of the Book object 
    def bookmark_page(self):
        self.bookmark = self.current_page

    # method takes in one argument -> direction which can be True or False (or anything else)
    def turn_page(self, direction):
        if direction:
            self.current_page += 1
        else:
            self.current_page -=1

    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"

    # determines the length of the Book object
    def __len__(self):
        return self.pages

my_book = Book("A great book", "me", 198, 1)
# print(my_book)

# my_book.bookmark_page()
# print(my_book.bookmark)
# my_book.turn_page(False)
# my_book.bookmark_page()
# print(my_book.bookmark)

class Employee:

    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone_number)

employee_1 = Employee("Fran", 78000, "0472028842", "1st June 2020")
print(employee_1.get_employment_details())