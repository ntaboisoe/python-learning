# Base class
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Pages: {self.pages}"

# Subclass for E-Book (Inheritance)
class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        super().__init__(title, author, genre, pages)
        self.file_size = file_size  # Additional attribute

    def description(self):
        return super().description() + f", File Size: {self.file_size}MB"

# Creating objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 180)
ebook1 = EBook("Sapiens", "Yuval Noah Harari", "Non-Fiction", 500, 2.5)

# Display descriptions
print(book1.description())
print(ebook1.description())



# Base class
class Mover:
    def move(self):
        pass  # Abstract method (to be overridden)

# Subclass for Animal
class Animal(Mover):
    def move(self):
        return "Running 🦌"

# Subclass for Car
class Car(Mover):
    def move(self):
        return "Driving 🚗"

# Subclass for Plane
class Plane(Mover):
    def move(self):
        return "Flying ✈️"

# Function to demonstrate polymorphism
def demonstrate_movement(objects):
    for obj in objects:
        print(f"{obj.__class__.__name__}: {obj.move()}")

# Create objects
deer = Animal()
sedan = Car()
jet = Plane()

# Show polymorphic behavior
demonstrate_movement([deer, sedan, jet])

