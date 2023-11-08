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
     bookInventory[ISBN] = {
        "title": title,
        "author": author,
        "ISBN": ISBN,
        "price": price,
        "quantity": quantity
     }
     return


def removeBook (ISBN):
     if ISBN in bookInventory:
        del bookInventory[ISBN]
     return

def searchBookByISBN (ISBN):
    if ISBN in bookInventory:
        return bookInventory[ISBN]
    return 

def seacrhBookByTitleOrAuthor (query):
    matchingBooks = []
    for book in bookInventory.values():
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower():
            matchingBooks.append(book)
    return matchingBooks

def displayBook (ISBN):
    print(f"ISBN: {ISBN['ISBN']}")
    print(f"Title: {ISBN['title']}")
    print(f"Author: {ISBN['author']}")
    print(f"Price: {ISBN['price']}")
    print(f"Quantity: {ISBN['quantity']}")

def validateISBN (ISBN):
    while not ISBN.isdigit():
        print("Invalid ISBN. Please enter a numeric value.")
        ISBN = input("ISBN: ")
    return ISBN

def validateTitle (title):
    while not title:
        print("Title cannot be empty. Please enter a title.")
        title = input("Title: ")
    return title

def validateAuthor (author):
    while not author:
        print("Author cannot be empty. Please enter an author name.")
        author = input("Author: ")
    return author

def validatePrice (price):
    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("Price cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
        return price

def validateQuantity (quantity):
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a numeric value.")
    return quantity

def validateQuery (query):
    while not query:
        print("Query cannot be empty. Please enter an author or title.")
        query = input("query: ")
    return query
