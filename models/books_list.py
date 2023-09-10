from models.book import Book

book1 = Book("Trainspotting", "Irvine Welsh", "Dark Comedy")
book2 = Book("Knots & Crosses", "Ian Rankin", "Detective Fiction")
book3 = Book("The Wasp Factory", "Iain Banks", "Horror Fiction")
book4 = Book("The Hitchhiker's guide to the Galaxy", "Douglas Adams", "Sci Fi Comedy")

books_list = [book1, book2, book3, book4]

def add_new_book(book):
    books_list.append(book)