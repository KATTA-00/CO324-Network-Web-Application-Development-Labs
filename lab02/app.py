# E/19/129
# K.H. Gunawardana

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data as a dictionary keyed by book ID
books = {
    1: {"id": 1, "title": "Book 1", "author": "Author 1"},
    2: {"id": 2, "title": "Book 2", "author": "Author 2"},
    3: {"id": 3, "title": "Book 3", "author": "Author 3"},
}

# Sample data as a dictionary keyed by user ID
members = {
    123: {"id": 123, "name": "User 1", "email": "user1@example.com"},
    456: {"id": 456, "name": "User 2", "email": "user2@example.com"},
}

# Sample data as a dictionary keyed by loan ID
loans = {}

# Generate unique IDs for new items
def generate_id(dictionary):
    return max(dictionary.keys(), default=0) + 1

# CRUD operations for books

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values()))

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book_id = generate_id(books)
    new_book = {
        "id": new_book_id,
        "title": data["title"],
        "author": data["author"]
    }
    books[new_book_id] = new_book
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book is None:
        return "Book not found", 404
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = books.get(book_id)
    if book is None:
        return "Book not found", 404
    book["title"] = data["title"]
    book["author"] = data["author"]
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = books.pop(book_id, None)
    if book is None:
        return "Book not found", 404
    return "Book deleted", 204

# CRUD operations for members
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(list(members.values()))

@app.route('/members', methods=['POST'])
def create_members():
    # Extract JSON data from the request
    data = request.get_json()
    
    # Generate a new unique ID for the member
    new_members_id = generate_id(members)
    
    # Create a new member with the provided data
    new_members = {
        "id": new_members_id,
        "name": data["name"],
        "email": data["email"]
    }
    
    # Add the new member to the data structure
    members[new_members_id] = new_members
    
    # Return the newly created member with HTTP status code 201
    return jsonify(new_members), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    # Retrieve the member with the specified ID
    member = members.get(member_id)
    
    # Check if the member exists
    if member is None:
        return "Member not found", 404
    
    # Return the member information
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    # Extract JSON data from the request
    data = request.get_json()
    
    # Retrieve the member with the specified ID
    member = members.get(member_id)
    
    # Check if the member exists
    if member is None:
        return "Member not found", 404
    
    # Update the member information with the new data
    member["name"] = data["name"]
    member["email"] = data["email"]
    
    # Return the updated member information
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # Remove the member with the specified ID from the data structure
    member = members.pop(member_id, None)
    
    # Check if the member exists
    if member is None:
        return "Member not found", 404
    
    # Return a success message with HTTP status code 204 (No Content)
    return "Member deleted", 204


if __name__ == '__main__':
    app.run(debug=True)
