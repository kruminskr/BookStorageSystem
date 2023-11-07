bookInventory = {
    "123": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "ISBN": "123",
        "price": 10.99,
        "quantity": 25
    },
    "124": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "ISBN": "124",
        "price": 12.99,
        "quantity": 20
    },
    "125": {
        "title": "1984",
        "author": "George Orwell",
        "ISBN": "125",
        "price": 9.99,
        "quantity": 30
    }
}

def addBook (ISBN, title, author, price, quantity):
    if ISBN not in bookInventory:
        bookInventory[ISBN] = {
            "title": title,
            "author": author,
            "ISBN": ISBN,
            "price": price,
            "quantity": quantity
        }
        return True  
    return False

def removeBook (ISBN):
     if ISBN in bookInventory:
        del bookInventory[ISBN]
     return

def searchBookByISBN (ISBN):
    if ISBN in bookInventory:
        return bookInventory[ISBN]
    return 

def seacrhBookByTitleOrAuthor (query):
    matching_books = []
    for book in bookInventory.values():
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            matching_books.append(book)
    return matching_books

