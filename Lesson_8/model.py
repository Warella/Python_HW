def read_phone_book(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary