from django.contrib import admin

from apps.library.models import (Audio, AudioBook, AudioUnit, Author,
                                 AuthorCountry, Book, LibraryCategory,
                                 LibraryCategoryView, UserAudioListenTracker,
                                 UserBookReadTracker, UserSearchLibrary)


@admin.register(AuthorCountry)
class AuthorCountryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(LibraryCategory)
class LibraryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")


@admin.register(LibraryCategoryView)
class LibraryCategoryViewAdmin(admin.ModelAdmin):
    list_display = ("user", "category")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "category",
        "publication_year",
        "language",
        "is_mandatory",
    )


@admin.register(UserBookReadTracker)
class UserBookReadTrackerAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "page")


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(AudioUnit)
class AudioUnitAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(AudioBook)
class AudioBookAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "language")


@admin.register(UserAudioListenTracker)
class UserAudioListenTrackerAdmin(admin.ModelAdmin):
    list_display = ("user", "audio", "length")


@admin.register(UserSearchLibrary)
class UserSearchLibraryAdmin(admin.ModelAdmin):
    list_display = ("keyword",)
