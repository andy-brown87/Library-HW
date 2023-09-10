from flask import render_template, Blueprint, request, redirect
from models.books_list import books_list, add_new_book
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books_index():
    return render_template('index.jinja', title='My Book List', 
    books=books_list)

@books_blueprint.route('/books', methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre, False)
    add_new_book(new_book)
    return redirect("/books")