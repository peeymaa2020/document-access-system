from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(
        max_length=255
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='documents'
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to="documents/"
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    version = models.IntegerField(
        default=1
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title