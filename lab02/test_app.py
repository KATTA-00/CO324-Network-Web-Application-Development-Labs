# E/19/129
# K.H. Gunawardana

import unittest
import json
from app import app

class LibraryAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    # check /member GET
    def test_get_members(self):
        response = self.app.get('/members')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_get_nonexistent_book(self):
        response = self.app.get('/books/999')
        self.assertEqual(response.status_code, 404)

    # check /member GET for wrong
    def test_get_nonexistent_member(self):
        response = self.app.get('/members/999')
        self.assertEqual(response.status_code, 404)

    def test_create_and_delete_book(self):
        # Create a new book
        new_book_data = {"title": "Test Book", "author": "Test Author"}
        response = self.app.post('/books', json=new_book_data)
        self.assertEqual(response.status_code, 201)
        created_book = json.loads(response.get_data(as_text=True))

        # Retrieve the created book
        response = self.app.get(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 200)

        # Delete the created book
        response = self.app.delete(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 204)

        # Verify that the book is deleted
        response = self.app.get(f'/books/{created_book["id"]}')
        self.assertEqual(response.status_code, 404)


    # check for /member POST and DELETE methods
    def test_create_and_delete_member(self):
        # Create a new book
        new_member_data = {"name": "Kanishka Gunawardana", "email": "e19129@eng.pdn.ac.lk"}
        response = self.app.post('/members', json=new_member_data)
        self.assertEqual(response.status_code, 201)
        created_member = json.loads(response.get_data(as_text=True))

        # Retrieve the created book
        response = self.app.get(f'/members/{created_member["id"]}')
        self.assertEqual(response.status_code, 200)

        # Delete the created book
        response = self.app.delete(f'/members/{created_member["id"]}')
        self.assertEqual(response.status_code, 204)

        # Verify that the book is deleted
        response = self.app.get(f'/books/{created_member["id"]}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
