import click
from models import Category, Book

def display_categories(categories):
    if not categories:
        click.echo('No categories found.')
    else:
        for c in categories:
            click.echo(f"ID: {c.id}, Name: {c.name}")

def display_books(books):
    if not books:
        click.echo('No books found.')
    else:
        for b in books:
            click.echo(f"ID: {b.id}, Title: {b.title}, Quantity: {b.quantity}, Category ID: {b.category_id}")

def main_menu():
    while True:
        click.echo("\nBookstore Inventory System Main Menu:")
        click.echo("1. Create Category")
        click.echo("2. Delete Category")
        click.echo("3. List Categories")
        click.echo("4. Find Category by ID")
        click.echo("5. Create Book")
        click.echo("6. Delete Book")
        click.echo("7. List Books")
        click.echo("8. Find Book by ID")
        click.echo("9. Filter Books by Category")
        click.echo("10. Exit")
        choice = click.prompt('Select an option', type=int)
        try:
            if choice == 1:
                name = click.prompt('Enter category name')
                category = Category.create(name)
                click.echo(f"Category created: {category}")
            elif choice == 2:
                id = click.prompt('Enter category ID to delete', type=int)
                Category.delete(id)
                click.echo('Category deleted.')
            elif choice == 3:
                categories = Category.get_all()
                display_categories(categories)
            elif choice == 4:
                id = click.prompt('Enter category ID to find', type=int)
                category = Category.find_by_id(id)
                if not category:
                    click.echo('Category not found.')
                else:
                    click.echo(category)
                    if category.books:
                        click.echo('Books in this category:')
                        display_books(category.books)
                    else:
                        click.echo('No books in this category.')
            elif choice == 5:
                title = click.prompt('Enter book title')
                quantity = click.prompt('Enter quantity', type=int)
                category_id = click.prompt('Enter category ID', type=int)
                book = Book.create(title, quantity, category_id)
                click.echo(f"Book created: {book}")
            elif choice == 6:
                id = click.prompt('Enter book ID to delete', type=int)
                Book.delete(id)
                click.echo('Book deleted.')
            elif choice == 7:
                books = Book.get_all()
                display_books(books)
            elif choice == 8:
                id = click.prompt('Enter book ID to find', type=int)
                book = Book.find_by_id(id)
                if not book:
                    click.echo('Book not found.')
                else:
                    click.echo(book)
                    category = Category.find_by_id(book.category_id)
                    if category:
                        click.echo(f"Category: {category.name}")
            elif choice == 9:
                category_id = click.prompt('Enter category ID to filter', type=int)
                books = Book.get_all()
                filtered, length = Book.filter_by_category(books, category_id)
                click.echo(f"Filtered books (at most 2 in category {category_id}):")
                display_books(filtered)
                click.echo(f"Total: {length}")
            elif choice == 10:
                click.echo('Exiting Bookstore Inventory System.')
                break
            else:
                click.echo('Invalid option. Please select a number from 1 to 10.')
        except Exception as e:
            click.echo(f"Error: {e}")

if __name__ == '__main__':
    main_menu()
