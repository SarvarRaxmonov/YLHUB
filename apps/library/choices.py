from django.db import models


class BookType(models.TextChoices):
    BOOK = "book", "Book"
    LEGISLATIVE_DOCUMENT = "legislative_document", "Legislative Document"


class Language(models.TextChoices):
    ENGLISH = "eng", "English"
    UZBEK = "uz", "Uzbek"
    RUSSIAN = "ru", "Russian"
