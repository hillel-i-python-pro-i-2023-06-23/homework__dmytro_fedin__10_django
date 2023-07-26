import string

from faker import Faker

# Get faker instance
faker = Faker()

# Lexify faker
faker.lexify(letters=string.ascii_letters + string.digits + "_")
