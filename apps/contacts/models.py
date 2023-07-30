from django.db import models


# Create model of contact.
class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)
    phone_number = models.EmailField(unique=True)
    # been_created :TODO: add field
    # been_changed

    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )

    def __str__(self):
        return f"{self.name}"
