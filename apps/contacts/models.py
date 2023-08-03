from django.db import models
from django.core.validators import RegexValidator


# Create model of contact.
class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'",
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

    class Meta:
        ordering = ["modified_at", "name"]
