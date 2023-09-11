from django.contrib.auth.models import User
from django.db import models
from django.db.models import DurationField

from apps.library.choices import BookType, Language


class AuthorCountry(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LibraryCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="library_category_icons/")

    def __str__(self):
        return self.name


class LibraryCategoryView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(LibraryCategory, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="author_images/")
    birth_date = models.DateTimeField()
    country = models.ForeignKey(AuthorCountry, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class FileInfo(models.Model):
    name = models.CharField(max_length=500)
    cover = models.ImageField()
    category = models.ForeignKey(LibraryCategory, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    publication_year = models.PositiveIntegerField(blank=True)
    language = models.CharField(max_length=3, choices=Language.choices, default=Language.UZBEK)
    description = models.TextField()

    class Meta:
        abstract = True


class Book(FileInfo):
    cover = models.ImageField(upload_to="book_file_covers/")
    type = models.CharField(max_length=20, choices=BookType.choices)
    file = models.FileField(upload_to="book_files/")
    is_mandatory = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserBookReadTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField()

    def __str__(self):
        return self.user.username


class Audio(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="audio_files/")
    url = models.URLField()

    def __str__(self):
        return self.name


class AudioUnit(models.Model):
    name = models.CharField(max_length=255)
    audios = models.ManyToManyField(Audio)

    def __str__(self):
        return self.name


class AudioBook(FileInfo):
    cover = models.ImageField(upload_to="audio_book_file_covers/")
    units = models.ManyToManyField(AudioUnit)

    def __str__(self):
        return self.name


class UserAudioListenTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    length = DurationField()

    def __str__(self):
        return self.user.username


class UserSearchLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)

    def __str__(self):
        return self.keyword
