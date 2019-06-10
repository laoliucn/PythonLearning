from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)
print(__name__)

books = [
    {
        'name': 'Green eggs and Ham',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'Green eggs and Ham',
        'price': 7.99,
        'isbn': 9782371000193
    }

]


def valid_book_object(book_object):
    if "name" in book_object and "price" in book_object and "isbn" in book_object:
        return True
    else:
        return False

#GET books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#Add_books
@app.route('/books', methods=['POST'])
def add_books():
    #return jsonify(request.get_json())
    request_data = request.get_json()
    if valid_book_object(request_data):
        new_book = {
            "name": request_data['name'],
            "price": request_data['price'],
            "isbn": request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['location'] = "books" + str(new_book['isbn'])
        return response
    else:
        invalid_book_object_error_msg = {
            "error": "Invalid book object passed in request",
            "help_string": "Data passed in similar to this: {'isbn':12321321312,'name':'Frankenstein','price':7.99}"
        }
        response = Response(json.dumps(invalid_book_object_error_msg), 400, mimetype='application/json')
        return response


@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)


app.run(port=5000)
