from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bookConnection = sqlite3.connect('books.db', check_same_thread=False)
bookConnection.row_factory = sqlite3.Row
app.config['JSON_SORT_KEYS'] = False
bookCursor = bookConnection.cursor()

bookCursor.execute('''CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, author TEXT, title TEXT, year_published INT)''')
bookConnection.commit()


@app.route("/api/books", methods=["POST"])
def addBook():
    author = request.json.get('author')
    title = request.json.get('title')
    yearPublished = request.json.get('yearPublished')

    bookCursor.execute('INSERT INTO Books (author, title, year_published) VALUES (?,?,?)', (author, title, yearPublished))
    bookConnection.commit()
    
    bookCursor.execute('SELECT * FROM Books ORDER BY id DESC LIMIT 1')
    for row in bookCursor:
        newBookId = row['id']
        newBookAuthor = row['author']
        newBookTitle = row['title']
        newBookYear = row['year_published']

    return jsonify({'id':newBookId, 'author':newBookAuthor, 'title':newBookTitle, 'yearPublished':newBookYear}), 201


@app.route("/api/books", methods=["GET"])
def getAllBooksAlphOrder():
    bookList = []
    bookCursor.execute('SELECT * FROM Books ORDER BY title')

    for row in bookCursor:
        newBookId = row['id']
        newBookAuthor = row['author']
        newBookTitle = row['title']
        newBookYear = row['year_published']

        currentBook = {
            "id":newBookId,
            "author":newBookAuthor,
            "title":newBookTitle,
            "yearPublished":newBookYear
        }

        bookList.append(currentBook)

    return jsonify(bookList)


@app.route("/api/books", methods=["DELETE"])
def deleteAllBooks():
    bookList = []
    bookCursor.execute('DELETE FROM Books')
    bookConnection.commit()

    return jsonify(), 204


if __name__ == "__main__":
    app.run()