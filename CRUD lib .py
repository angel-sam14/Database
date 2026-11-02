books = [
    {"book_id": 101, "book_name": "Python Basics", "author": "John Smith",
     "category": "Programming", "price": 450, "copies": 5},

    {"book_id": 102, "book_name": "Web Development", "author": "David Miller",
     "category": "Technology", "price": 550, "copies": 3}
]


def add_book():
    book_id = int(input("Enter Book ID:"))

    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists")
            return

    name = input("Enter Book Name:")
    author = input("Enter Author:")
    category = input("Enter Category:")
    price = float(input("Enter Price:"))
    copies = int(input("Enter Copies:"))

    if price <= 0 or copies <= 0:
        print("Price and copies must be positive")
        return

    books.append({
        "book_id": book_id,
        "book_name": name,
        "author": author,
        "category": category,
        "price": price,
        "copies": copies
    })

    print("Book added successfully")



def view_books():
    if len(books) == 0:
        print("No books available")
    else:
        print(f"{'ID':<6}{'Name':<20}{'Author':<15}{'Category':<15}{'Price':<10}{'Copies':<10}")
        print("-" * 76)

        for book in books:
            print(f"{book['book_id']:<6}{book['book_name']:<20}{book['author']:<15}{book['category']:<15}{book['price']:<10}{book['copies']:<10}")

        print("-" * 76)
        print(f"Total count: {len(books)}")


def update_book():
    book_id = int(input("Enter Book ID to update:"))

    for book in books:
        if book["book_id"] == book_id:

            name = input("Enter New Name:")
            author = input("Enter New Author:")
            category = input("Enter New Category:")
            price = float(input("Enter New Price:"))
            copies = int(input("Enter New Copies:"))

            if price <= 0 or copies <= 0:
                print("Price and copies must be positive")
                return

            book["book_name"] = name
            book["author"] = author
            book["category"] = category
            book["price"] = price
            book["copies"] = copies

            print("Book updated successfully")
            return

    print("Book ID not found")

def delete_book():
    book_id = int(input("Enter Book ID to delete:"))

    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            print("Book deleted successfully")
            return

    print("Book ID not found")

def search_book():
    search = input("Enter Book ID or Book Name:")

    for book in books:
        if str(book["book_id"]) == search or book["book_name"].lower() == search.lower():
            print(book)
            return

    print("Book not found")


while True:
    Choice = int(input(
        "\n1. Add New Book\n"
        "2. View All Books\n"
        "3. Update Book Details\n"
        "4. Delete Book\n"
        "5. Search Book\n"
        "6. Exit\n"
        "Enter your choice:"
    ))

    match Choice:

        case 1:
            add_book()

        case 2:
            view_books()

        case 3:
            update_book()

        case 4:
            delete_book()

        case 5:
            search_book()

        case 6:
            break

        case _:
            print("Invalid Choice")