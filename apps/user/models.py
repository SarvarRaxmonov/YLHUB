from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile", verbose_name=_("User"))
    full_name = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Full name"))
    jshshir = models.IntegerField(null=True, blank=True, verbose_name=_("Jshshir"))
    password_seria = models.CharField(max_length=9, null=True, blank=True, verbose_name=_("Password Seria"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("Birth Date"))
    nation = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("Nation"))
    education = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("Education"))
    education_place = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Education place"))
    work_place = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Work place"))
    position = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Position"))
    image = models.ImageField(upload_to="users/photo", null=True, blank=True, verbose_name=_("Image"))
    score = models.IntegerField(default=0, verbose_name=_("Score"))
    kpi = models.IntegerField(default=0, verbose_name=_("KPI"))

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class SocialNetworkName(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    icon = models.ImageField(upload_to="users/social_network/icon", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Social Network Name")
        verbose_name_plural = _("Social Network Names")


class SocialNetwork(BaseModel):
    name = models.ForeignKey(
        "user.SocialNetworkName",
        on_delete=models.CASCADE,
        related_name="social_network",
        verbose_name=_("Social Network Name"),
    )
    profile = models.ForeignKey(
        "user.Profile", on_delete=models.CASCADE, related_name="social_network", verbose_name=_("Profile")
    )
    link = models.CharField(verbose_name=_("Link"))

    def __str__(self):
        return self.name.name

    class Meta:
        verbose_name = _("Social Network")
        verbose_name_plural = _("Social Networks")


class DocumentName(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Document name")
        verbose_name_plural = _("Document names")


class Document(BaseModel):
    profile = models.ForeignKey(
        "user.Profile", on_delete=models.CASCADE, related_name="documents", verbose_name=_("Profile")
    )
    name = models.ForeignKey(
        "user.DocumentName", on_delete=models.CASCADE, related_name="documents", verbose_name=_("Name")
    )
    file = models.FileField(upload_to="users/documents", null=True, blank=True, verbose_name=_("File"))

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
