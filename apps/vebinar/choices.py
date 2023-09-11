from django.db import models


class VEBINARStatus(models.TextChoices):
    COMING = "coming", "Coming"
    NOW = "now", "Now"
    FINISHED = "finished", "Finished"


class VEBINARType(models.TextChoices):
    SEMINAR = "seminar", "Seminar"
    LECTURE = "lecture", "Lecture"


class ComplainType(models.TextChoices):
    COMPLAINT = "zararli yoki noqonuniy", "Zararli yoki noqonuniy"
    CONFIDENTIAL = "shaxsiy malumot", "Shaxsiy malumot"
    ADS = "reklama", "Reklama"
    NOT_RELATED_TO_TRUTH = "haqiqatga mos kelmaydi", "Haqiqatga mos kelmaydi"
    OTHER = "boshqa", "Boshqa"
