import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")
        
        # List to store books
        self.books = []

        # Creating labels and entry fields
        self.title_label = tk.Label(self.root, text="Book Title")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1)
        
        self.author_label = tk.Label(self.root, text="Author")
        self.author_label.grid(row=1, column=0)
        self.author_entry = tk.Entry(self.root)
        self.author_entry.grid(row=1, column=1)
        
        self.year_label = tk.Label(self.root, text="Year")
        self.year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.grid(row=2, column=1)
        
        self.isbn_label = tk.Label(self.root, text="ISBN")
        self.isbn_label.grid(row=3, column=0)
        self.isbn_entry = tk.Entry(self.root)
        self.isbn_entry.grid(row=3, column=1)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=4, column=0)

        self.view_button = tk.Button(self.root, text="View Books", command=self.view_books)
        self.view_button.grid(row=4, column=1)

        self.search_button = tk.Button(self.root, text="Search Book", command=self.search_book)
        self.search_button.grid(row=5, column=0)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=5, column=1)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        isbn = self.isbn_entry.get()

        if title and author and year and isbn:
            self.books.append({"Title": title, "Author": author, "Year": year, "ISBN": isbn})
            messagebox.showinfo("Success", "Book Added Successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def view_books(self):
        if not self.books:
            messagebox.showinfo("No Books", "No books in the library")
            return
        books_list = "\n".join([f"{book['Title']} by {book['Author']} ({book['Year']}) ISBN: {book['ISBN']}" for book in self.books])
        messagebox.showinfo("Books List", books_list)

    def search_book(self):
        search_title = self.title_entry.get().lower()
        search_author = self.author_entry.get().lower()

        results = [book for book in self.books if search_title in book['Title'].lower() or search_author in book['Author'].lower()]

        if results:
            results_list = "\n".join([f"{book['Title']} by {book['Author']} ({book['Year']}) ISBN: {book['ISBN']}" for book in results])
            messagebox.showinfo("Search Results", results_list)
        else:
            messagebox.showinfo("No Results", "No books found with the given title or author")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    library_system = LibraryManagementSystem(root)
    root.mainloop()
