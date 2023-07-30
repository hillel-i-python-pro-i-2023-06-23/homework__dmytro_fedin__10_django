# Get faker
from faker import Faker


# Get contact fields
def get_contact():
    current_faker = Faker()

    current_name = current_faker.name()
    current_phone = current_faker.phone_number()

    return current_name, current_phone
