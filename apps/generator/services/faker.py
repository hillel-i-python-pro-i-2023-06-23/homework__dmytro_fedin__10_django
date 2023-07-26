import string

# Get faker
from faker import Faker

faker = Faker()
faker.lexify(letters=string.ascii_letters + string.digits + "_")
