# For python
from collections.abc import Iterator

# Get app model
from apps.contacts.models import Contact
from apps.contacts.services.faker import get_contact


def generate_contact() -> Contact:
    concurrent_credentials = get_contact()

    return Contact(
        name=concurrent_credentials[0],
        phone_number=concurrent_credentials[1],
        # password=concurrent_credentials[2], :TODO: add fields
    )


def generate_contacts(amount: int) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
