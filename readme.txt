# Book API

This is a simple Django REST framework project that provides API endpoints to manage books.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3
- Django
- Django REST framework

### Installation

1. Clone the repository to your local machine:

2. Change into the project directory:


3. Create a virtual environment (optional but recommended):


4. Activate the virtual environment :


5. Install the required dependencies:



### Database Setup

By default, this project uses SQLite as the database. To set up the database, run the following command:

python manage.py migrate


### Running the Development Server

To run the development server, use the following command:

python manage.py runserver


The API will be available at http://127.0.0.1:8000/api/api/books/.

## API Endpoints

### List and Create Books

- URL: /api/books/
- Method: GET, POST

### Retrieve, Update, and Delete Book

- URL: /api/books/<int:pk>/
- Method: GET, PUT, DELETE

## Running Tests

To run the tests for the API endpoints, use the following command:

pytest



