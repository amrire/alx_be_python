class Book:

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
        
    def __del__(self):
        """Print message when a Book instance is deleted."""
        print(f"Deleting {self.title}")
        
    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Return a string that can be used to recreate the Book object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"