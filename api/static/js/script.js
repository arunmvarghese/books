document.addEventListener('DOMContentLoaded', function() {
    const bookList = document.getElementById('book-list');
    const addBookForm = document.getElementById('add-book-form');

    // Function to fetch and display books
    function fetchBooks() {
        fetch('/api/books/')
            .then(response => response.json())
            .then(data => {
                bookList.innerHTML = '';
                data.forEach(book => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `<strong>${book.title}</strong> - ${book.author}`;
                    bookList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching books:', error));
    }

    // Function to add a new book
    function addBook(event) {
        event.preventDefault();
        const title = document.getElementById('title').value;
        const author = document.getElementById('author').value;
        const published_date = document.getElementById('published_date').value;
        const isbn = document.getElementById('isbn').value;
        const amount = document.getElementById('amount').value;

        const data = {
            title: title,
            author: author,
            published_date: published_date,
            isbn: isbn,
            amount: amount
        };

        fetch('/api/books/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            fetchBooks(); // Refresh the book list after adding a new book
            addBookForm.reset(); // Reset the form fields
        })
        .catch(error => console.error('Error adding book:', error));
    }

    function updateBook(bookId, data) {
        fetch(`/api/books/${bookId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            fetchBooks(); // Refresh the book list after updating a book
        })
        .catch(error => console.error('Error updating book:', error));
    }
    
    // Function to delete a book
    function deleteBook(bookId) {
        if (confirm('Are you sure you want to delete this book?')) {
            fetch(`/api/books/${bookId}/`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.status === 204) {
                    fetchBooks(); // Refresh the book list after deleting a book
                } else {
                    console.error('Error deleting book:', response.status);
                }
            })
            .catch(error => console.error('Error deleting book:', error));
        }
    }
    
    // Event listener for the "Edit" and "Delete" buttons in the book list
    bookList.addEventListener('click', function(event) {
        if (event.target.classList.contains('edit-btn')) {
            const listItem = event.target.closest('li');
            const bookId = listItem.dataset.bookId;
            const title = listItem.querySelector('.title').textContent;
            const author = listItem.querySelector('.author').textContent;
            const publishedDate = listItem.querySelector('.published-date').textContent;
            const isbn = listItem.querySelector('.isbn').textContent;
            const amount = listItem.querySelector('.amount').textContent;
    
            // Fill the form fields with the book data for editing
            document.getElementById('edit-title').value = title;
            document.getElementById('edit-author').value = author;
            document.getElementById('edit-published_date').value = publishedDate;
            document.getElementById('edit-isbn').value = isbn;
            document.getElementById('edit-amount').value = amount;
    
            // Event listener for the "Save" button in the edit form
            document.getElementById('edit-book-form').addEventListener('submit', function(event) {
                event.preventDefault();
                const editedData = {
                    title: document.getElementById('edit-title').value,
                    author: document.getElementById('edit-author').value,
                    published_date: document.getElementById('edit-published_date').value,
                    isbn: document.getElementById('edit-isbn').value,
                    amount: document.getElementById('edit-amount').value
                };
                updateBook(bookId, editedData);
            });
        } else if (event.target.classList.contains('delete-btn')) {
            const listItem = event.target.closest('li');
            const bookId = listItem.dataset.bookId;
            deleteBook(bookId);
        }
    });

    // Event listener for the "Add Book" form submit
    addBookForm.addEventListener('submit', addBook);

    // Fetch and display books when the page loads
    fetchBooks();
});
