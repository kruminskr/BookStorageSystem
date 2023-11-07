from src.bookInventory import *

print("**********Book Invenrory Managment System************")

action = input("Choose an action (Add, Remove, Search, Display)")

if action.lower() == "add":
    ISBN = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    price = int(input("Price: "))
    quantity = input("Quantity: ")

    addResult = addBook(ISBN, title, author, price, quantity)

    if not addResult:
        print(f"Book with an ISBN of {ISBN} already exists.")
    else:
        print("Book succesfully added.")

if action.lower() == "remove":
    ISBN = input("ISBN of the book you want to remove: ")

    removeResult = removeBook(ISBN)

    if not removeResult:
        print(f"Book with an ISBN of {ISBN} doesn't exist.")
    else:
        print("Book succesfully removed.")

if action.lower() == "search":
    ISBN = input("ISBN of the book you are loking for: ")
    searchResult = searchBookByISBN(ISBN)
    if not searchResult: 
        print(f"Book with an ISBN of {ISBN} was not found.")
    else:
        print(searchResult)
    
if action.lower() == "display":
    if not bookInventory:
        print("There are no books to display.")
    else:
        print(bookInventory)

print(bookInventory)