from src.bookInventory import *

print("**********Book Invenrory Managment System************")

validActions = ["add", "remove", "search", "display"]
action = input("Choose an action (Add, Remove, Search, Display): ").lower()

while action not in validActions:
    print("Invalid action. Please choose from Add, Remove, Search, or Display.")
    action = input("Choose an action: ").lower()

if action.lower() == "add":
    ISBN = input("ISBN: ")
    while not ISBN.isdigit():
        print("Invalid ISBN. Please enter a numeric value.")
        ISBN = input("ISBN: ")

    title = input("Title: ")
    while not title:
        print("Title cannot be empty. Please enter a title.")
        title = input("Title: ")

    author = input("Author: ")
    while not author:
        print("Author cannot be empty. Please enter an author name.")
        author = input("Author: ")

    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("Price cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a numeric value.")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a numeric value.")

    if ISBN not in bookInventory:
        addBook(ISBN, title, author, price, quantity)
        print("Book successfully added.")

    else:
        print(f"Book with an ISBN of {ISBN} already exists.")


if action == "remove":
    ISBN = input("ISBN of the book you want to remove: ")

    if ISBN not in bookInventory:
        print(f"Book with an ISBN of {ISBN} doesn't exist.")
    else:
        removeResult = removeBook(ISBN)
        print("Book succesfully removed.")

if action == "search":
    validSearchTypes = ["isbn", "title", "author"]
    searchType = input("search by (ISBN or Title/author): ").lower()
    
    while searchType not in validSearchTypes:
        print("Invalid search type. Please choose from ISBN, Title or Author.")
        searchType = input("Choose an search type: ").lower()

    if searchType == "isbn":
        ISBN = input("ISBN of the book you are loking for: ")
        searchResult = searchBookByISBN(ISBN)
        if not searchResult: 
            print(f"Book with an ISBN of {ISBN} was not found.")
        else:
            print(searchResult)

    elif searchType == "title":
        query = input("Title or Author of the book you are loking for: ")
        searchResult = seacrhBookByTitleOrAuthor(query)
        if not searchResult: 
            print(f"The book you are looking for was not found.")
        else:
            print(searchResult)

if action.lower() == "display":
    if not bookInventory:
        print("There are no books to display.")
    else:
        print("Book Inventory:")
        for ISBN, book in bookInventory.items():
            print(f"ISBN: {ISBN}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}")
            print("\n")

print(bookInventory)