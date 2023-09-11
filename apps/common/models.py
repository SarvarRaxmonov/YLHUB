from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"), blank=True, null=True)

    class Meta:
        abstract = True
