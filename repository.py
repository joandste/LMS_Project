from typing import List, Optional

from PyQt5.QtCore.QUrl import query

from database import Database
from model import Book, Publisher, Member
from utils import logger


class Repository:
    """
    Repository class for handling database operations related to books, publishers, members, and loans.
    """

    def __init__(self) -> None:
        """Initializes the Repository class and connects to the database."""
        self.db = Database()
        try:
            self.db.connect()
        except Exception as e:
            logger.critical(f"Failed to connect to the database: {e}")
            raise RuntimeError("Database connection failed.")

    def fetchall_books(self) -> List[Book]:
        """
        Fetches all books from the database.

        Returns:
            List[Book]: A list of Book objects representing all books in the database.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        raise NotImplementedError("fetchall_books method is not implemented.")

        ### YOUR CODE ###
        try:
            results = self.db.fetch_results(query = query)
            return [Book(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch all books: {e}")
            return []

    def add_book(self, book: Book) -> None:
        """
        Adds a new book to the database.

        Args:
            book (Book): The book object to be added.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        raise NotImplementedError("add_book method is not implemented.")

        ### YOUR CODE ###
        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book '{book.title}' added successfully.")
        except Exception as e:
            logger.error(f"Failed to add book '{book.title}': {e}")
            raise RuntimeError("Failed to add book.")

    def delete_book_by_id(self, book_id: int) -> None:
        """
        Deletes a book by its ID.

        Args:
            book_id (int): The ID of the book to delete.
        """
        ### YOUR QUERY ###
        # query = ...
        # params =
        # remove the following line after your implementation
        raise NotImplementedError("delete_book_by_id method is not implemented.")

        ### YOUR CODE ###
        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book with ID {book_id} deleted successfully.")
        except Exception as e:
            logger.error(f"Failed to delete book with ID {book_id}: {e}")
            raise RuntimeError("Failed to delete book.")

    def update_book(self, book: Book) -> None:
        """
        Updates the details of a book in the database.

        Args:
            book (Book): The book object with updated information.
        """
        ### YOUR QUERY ###
        # query = ...
        # params
        # remove the following line after your implementation
        raise NotImplementedError("update_book method is not implemented.")

        ### YOUR CODE ###
        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book with ID {book.id} updated successfully.")
        except Exception as e:
            logger.error(f"Failed to update book with ID {book.id}: {e}")
            raise RuntimeError("Failed to update book.")

    def get_books_by_author_name(self, author_name: str) -> List[Book]:
        """
        Fetches books by author name.

        Args:
            author_name (str): The name of the author.

        Returns:
            List[Book]: A list of books by the given author.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_books_by_author_name method is not implemented.")

        ### YOUR CODE ###
        try:
            results = self.db.fetch_results(query = query, params = params)
            return [Book(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch books by author '{author_name}': {e}")
            return []

    def get_publishers(self) -> List[Publisher]:
        """
        Fetches all publishers from the database.

        Returns:
            List[Publisher]: A list of Publisher objects.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_publishers method is not implemented.")

        ### YOUR CODE ###
        try:
            results = self.db.fetch_results(query = query)
            return [Publisher(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch publishers: {e}")
            return []

    def get_all_members(self) -> List[Member]:
        """
        Fetches all members from the database.

        Returns:
            List[Member]: A list of Member objects.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_all_members method is not implemented.")

        ### YOUR CODE ###

        try:
            results = self.db.fetch_results(query = query)
            return [Member(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch members: {e}")
            return []

    def get_book_by_name(self, book_name: str) -> Optional[Book]:
        """
        Fetches a book by its title.

        Args:
            book_name (str): The title of the book.

        Returns:
            Optional[Book]: The Book object if found, otherwise None.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_book_by_name method is not implemented.")

        ### YOUR CODE ###
        try:
            result = self.db.fetch_results(query = query, params = params)
            return Book(*result[0]) if result else None
        except Exception as e:
            logger.error(f"Failed to fetch book '{book_name}': {e}")
            return None

    def get_all_members_by_book(self, book_name: str) -> List[tuple]:
        """
        Fetches all members who borrowed a specific book.

        Args:
            book_name (str): The title of the book.

        Returns:
            List[tuple]: A list of tuples containing member and loan information.
        """
        book = self.get_book_by_name(book_name)
        if not book:
            logger.warning(f"No book found with title '{book_name}'.")
            return []

        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_all_members_by_book method is not implemented.")

        ### YOUR CODE ###
        try:
            return self.db.fetch_results(query = query, params = params)
        except Exception as e:
            logger.error(f"Failed to fetch members for book '{book_name}': {e}")
            return []

    def get_all_loans(self) -> List[tuple]:
        """
        Fetches all loans from the database.

        Returns:
            List[tuple]: A list of tuples containing loan information.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        raise NotImplementedError("get_all_loans method is not implemented.")

        ### YOUR CODE ###
        try:
            return self.db.fetch_results(query = query)
        except Exception as e:
            logger.error(f"Failed to fetch loans: {e}")
            return []
