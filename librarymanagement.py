books = []

def add_book(title, author, year):
    books.append((title, author, year))

def search_books(title):
    matching_books = []
    for book in books:
        if title in book[0]:
            matching_books.append(book)
    return matching_books

def sort_books():
    books.sort(key=lambda book: book[0])

def track_borrowed_book(year):
    for book in books:
        if book[2] == "C PROGRAMMING":
            book[2] = "borrowed"
def display_books():
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}, year: {book[2]}")

def main():
    add_book("PYTHON", "GUIDO VAN ROSSUM", "1991")
    add_book("C PROGRAMMING", "DENNIS RITCHIE", "1970")
    add_book("JAVA", "JAMES GOSLING", "1995")

    print("Books in the library:")
    for book in books:
        print(book[0])

    print("Searching for books by title:")
    matching_books = search_books("DATA SCIENE")
    for book in matching_books:
        print(book[0])

    print("Sorting books by title:")
    sort_books()
    for book in books:
        print(book[0])

    print("Check a book as borrowed:")
    track_borrowed_book("1995")
    for book in books:
        if book[2] == "borrowed":
            print(book[0], "is borrowed")

if __name__ == "__main__":
    main()