from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample database
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

@app.route('/')
def homepage():
    return render_template('books.html', books=books)

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else ('Not Found', 404)

# POST new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# PUT update book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return ('Not Found', 404)

# DELETE book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return ('Deleted', 204)

if __name__ == '__main__':
    app.run(debug=True)
