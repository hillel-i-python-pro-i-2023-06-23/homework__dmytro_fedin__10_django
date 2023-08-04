from django.db import models
from django.core.validators import RegexValidator


# Create model of contact.
class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?[-().\dx]{9,20}$",
        message="Phone number is invalid",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )

    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name}"

    # Get metadata from model (sort by newest record)
    class Meta:
        ordering = ["-modified_at", "name"]
