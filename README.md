# Bookstore Inventory System

This is a Python CLI application for managing a bookstore's inventory, including books and categories, using SQLAlchemy (SQLite) and Click for the CLI interface.

## Features
- Manage categories (create, delete, list, find)
- Manage books (create, delete, list, find)
- View books in a category
- Filter books by category (in-place, at most two per category)
- Input validation and informative error messages
- User-friendly CLI with main menu

## Project Structure
```
bookstore_inventory/
├── models/
│   ├── __init__.py
│   ├── category.py
│   ├── book.py
├── cli.py
├── database.py
├── main.py
├── Pipfile
├── README.md
```

## Setup Instructions
1. **Install pipenv** (if not already):
   ```bash
   pip install pipenv
   ```
2. **Install dependencies:**
   ```bash
   pipenv install
   ```
3. **Run the application:**
   ```bash
   pipenv run python main.py
   ```

## Usage
- Follow the CLI prompts to create, delete, list, or find categories and books.
- Use the filter_books command to show at most two books per category (in-place filtering).
- All input is validated; errors are shown for invalid or duplicate entries.

## Testing Guidelines
- Try to create a category with a name shorter than 3 characters (should fail).
- Try to create a book with a negative quantity (should fail).
- Try to create a category with a duplicate name (should fail).
- Try to delete or find a non-existent category or book (should show error).
- Use the filter_books command to verify in-place filtering logic.

## Pyodide Compatibility
- Uses SQLite and avoids complex file I/O for compatibility with Pyodide environments.

## Requirements
- Python 3.8+
- Only `sqlalchemy` and `click` are required dependencies.

---

**Note:** No automated tests are included, but the CLI is robust against bad inputs and provides clear error messages.