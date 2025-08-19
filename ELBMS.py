# Node class for Linked List
class BookNode:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
        self.next = None


# Linked List for Inventory
class Library:
    def __init__(self):
        self.head = None
        self.action_stack = []  # Stack to store last actions

    # Add new book to inventory
    def add_book(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        new_book.next = self.head
        self.head = new_book
        print(f"📚 Book '{title}' by {author} added to library.")

    # Borrow book
    def borrow_book(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                if current.available:
                    current.available = False
                    self.action_stack.append(("borrow", current))
                    print(f"✅ You borrowed '{current.title}'.")
                    return
                else:
                    print("❌ Book already borrowed.")
                    return
            current = current.next
        print("❌ Book not found.")

    # Return book
    def return_book(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                if not current.available:
                    current.available = True
                    self.action_stack.append(("return", current))
                    print(f"✅ You returned '{current.title}'.")
                    return
                else:
                    print("❌ Book was not borrowed.")
                    return
            current = current.next
        print("❌ Book not found.")

    # Undo last action
    def undo_action(self):
        if not self.action_stack:
            print("⚠️ No actions to undo.")
            return

        action, book = self.action_stack.pop()
        if action == "borrow":
            book.available = True
            print(f"↩️ Undo: '{book.title}' is now available again.")
        elif action == "return":
            book.available = False
            print(f"↩️ Undo: '{book.title}' is marked as borrowed again.")

    # Search by title or author
    def search_book(self, keyword):
        current = self.head
        found = False
        print(f"\n🔍 Search Results for '{keyword}':")
        while current:
            if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                status = "Available" if current.available else "Borrowed"
                print(f"   {current.book_id}: {current.title} by {current.author} [{status}]")
                found = True
            current = current.next
        if not found:
            print("   No books found.")

    # View all books
    def view_books(self):
        if not self.head:
            print("📂 Library is empty.")
            return
        print("\n--- Library Inventory ---")
        current = self.head
        while current:
            status = "Available" if current.available else "Borrowed"
            print(f"{current.book_id}: {current.title} by {current.author} [{status}]")
            current = current.next


# Main Program
def main():
    library = Library()

    # Preload some books
    library.add_book(1, "1984", "George Orwell")
    library.add_book(2, "To Kill a Mockingbird", "Harper Lee")
    library.add_book(3, "The Great Gatsby", "F. Scott Fitzgerald")

    while True:
        print("\n==== E-Library Book Management ====")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Undo Last Action")
        print("5. Search Book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.view_books()
        elif choice == "2":
            book_id = int(input("Enter Book ID to borrow: "))
            library.borrow_book(book_id)
        elif choice == "3":
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)
        elif choice == "4":
            library.undo_action()
        elif choice == "5":
            keyword = input("Enter title/author to search: ")
            library.search_book(keyword)
        elif choice == "6":
            print("👋 Exiting E-Library. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
