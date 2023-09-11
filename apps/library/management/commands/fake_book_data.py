import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.library.models import Book  # Import your Book model


class Command(BaseCommand):
    help = "Generates fake books and saves them to the database"

    def handle(self, *args, **kwargs):
        num_books = 1000  # Number of fake books to create
        fake = Faker()

        for _ in range(num_books):
            name = fake.sentence(nb_words=3)
            publication_year = random.randint(1900, 2023)
            language = random.choice(["eng", "uz", "ru"])
            description = fake.paragraph(nb_sentences=3)
            is_mandatory = random.choice([True, False])

            # Create a Book instance and save it
            book = Book(
                name=name,
                type="book",  # You can set the type as needed
                category_id=1,  # Replace with the actual category ID
                cover="book_file_covers/2023-01-30_1.jpeg",  # Replace with the actual image path
                publication_year=publication_year,
                language=language,
                description=description,
                is_mandatory=is_mandatory,
            )
            book.save()

            self.stdout.write(self.style.SUCCESS(f"Created book: {name}"))
