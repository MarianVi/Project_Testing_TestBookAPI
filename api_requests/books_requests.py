import requests

URL = 'https://simple-books-api.glitch.me'


def get_all_books(filter_type='', limit=''):
    return requests.get(f'{URL}/books?type={filter_type}&limit={limit}')


def get_book(book_id):
    return requests.get(f'{URL}/books/{book_id}')


# print(get_all_books().status_code)
# for book in get_all_books().json():
#     print(book['name'])

# print(get_book(7).status_code)
# print(get_book(1).json())

# print(get_all_books('fiction', '2').json())
# print(get_all_books('fiction').json())
# print(get_all_books(limit='2').json())
