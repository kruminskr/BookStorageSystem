from src.bookInventory import *

print("**********Book Invenrory Managment System************")

while True:
    validActions = ["add", "remove", "search", "display", "exit"]
    action = input("Choose an action (Add, Remove, Search, Display, Exit): ").lower()

    while action not in validActions:
        print("Invalid action. Please choose from Add, Remove, Search, Display or Exit.")
        action = input("Choose an action: ").lower()

    if action.lower() == "add":
        ISBN =  validateISBN(input("ISBN: "))
        title = validateTitle(input("Title: "))
        author = validateAuthor(input("Author: "))
        price = validatePrice(input)
        quantity = validateQuantity(input)

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
            ISBN = validateISBN(input("ISBN of the book you are loking for: "))
            searchResult = searchBookByISBN(ISBN)
            if not searchResult: 
                print(f"Book with an ISBN of {ISBN} was not found.")
            else:
                displayBook(searchResult)

        elif searchType in ["title", "author"]:
            query = validateQuery(input("Title or Author of the book you are loking for: "))
            searchResult = seacrhBookByTitleOrAuthor(query)
            if not searchResult: 
                print(f"The book you are looking for was not found.")
            else:
                for book in searchResult:
                    displayBook(book)
                    print("\n")

    if action.lower() == "display":
        if not bookInventory:
            print("There are no books to display.")
        else:
            print("Book Inventory:")
            for ISBN, book in bookInventory.items():
                displayBook(book)
                print("\n")
    
    if action == "exit":
        print("Exiting the system. Goodbye!")
        break


