from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.vebinar.choices import ComplainType, VEBINARStatus, VEBINARType


class Vebinar(models.Model):
    name = models.CharField(_("nomi"), max_length=500)
    url = models.URLField()
    speaker = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=VEBINARStatus.choices, default="coming")
    thumbnail = models.ImageField(_("Cover Photo"), upload_to="thumbnails/")
    type = models.CharField(max_length=100, choices=VEBINARType.choices, default="seminar")
    description = models.TextField()

    def __str__(self):
        return self.name


class UserSearchVebinar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=500)

    def __str__(self):
        return f'Search for "{self.keyword}" by {self.user.username}'


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Chat in "{self.vebinar.name}" by {self.user.username}'


class Complain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vebinar = models.ForeignKey(Vebinar, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=ComplainType.choices, default=ComplainType.OTHER)
    text = models.TextField()

    def __str__(self):
        return f'{self.get_type_display()} about "{self.vebinar.name}" by {self.user.username}'
