📌 Project Description – E-Library Book Management

The E-Library Book Management System is a Python-based project that allows users to borrow and return books while keeping track of the library’s inventory. It uses a linked list to store book records and a stack to implement undo functionality, so the most recent borrow/return action can be reversed.

✅ Why Use It?

Libraries often need to manage borrowing and returning of books in an organized way.

Mistakes happen (like borrowing/returning the wrong book), so an undo feature is very useful.

Provides an easy way to search and filter books by title or author.

🌟 Advantages

Efficient storage – Linked list makes it easy to add/remove books dynamically.

Undo support – Stack allows quick reversal of the last action.

Easy searching – Books can be quickly searched by title or author.

User-friendly – Clear menu-based system.

📍 Where It Can Be Used

School or college digital libraries

Small community libraries to track book lending

E-learning platforms that need basic book tracking

🎯 Usefulness

This project is useful for practicing data structures in real-world scenarios:

Linked list → managing a dynamic collection of books

Stack → supporting undo (LIFO) for borrow/return operations

Search/filter → making the system practical for users

#OUTPUT
📚 Book '1984' by George Orwell added to library.
📚 Book 'To Kill a Mockingbird' by Harper Lee added to library.
📚 Book 'The Great Gatsby' by F. Scott Fitzgerald added to library.

==== E-Library Book Management ====
1. View Books
2. Borrow Book
3. Return Book
4. Undo Last Action
5. Search Book
6. Exit
Enter your choice: 1

--- Library Inventory ---
3: The Great Gatsby by F. Scott Fitzgerald [Available]
2: To Kill a Mockingbird by Harper Lee [Available]
1: 1984 by George Orwell [Available]

Enter your choice: 2
Enter Book ID to borrow: 2
✅ You borrowed 'To Kill a Mockingbird'.

Enter your choice: 1

--- Library Inventory ---
3: The Great Gatsby by F. Scott Fitzgerald [Available]
2: To Kill a Mockingbird by Harper Lee [Borrowed]
1: 1984 by George Orwell [Available]

Enter your choice: 4
↩️ Undo: 'To Kill a Mockingbird' is now available again.

Enter your choice: 5
Enter title/author to search: Orwell

🔍 Search Results for 'Orwell':
   1: 1984 by George Orwell [Available]

Enter your choice: 6
👋 Exiting E-Library. Goodbye!
