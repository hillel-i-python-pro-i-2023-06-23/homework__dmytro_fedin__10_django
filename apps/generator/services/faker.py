import string

from faker import Faker


def get_credentials():
    current_faker = Faker()

    # Set templates for items
    characters = string.ascii_letters + string.digits + "_"
    password_characters = string.ascii_letters + string.digits + "!@#$^()"

    login_template = current_faker.lexify(text="?" * 8, letters=characters)
    text_template = current_faker.lexify(text="?" * 3, letters=characters)
    password_template = current_faker.lexify(
        text="?" * 12, letters=password_characters
    )

    def get_login():
        return login_template

    def get_text():
        return text_template

    def get_password():
        return password_template

    current_login = get_login()
    current_text = get_text()
    current_password = get_password()
    domain_name = current_faker.unique.domain_name()
    current_email = f"{current_login}{current_text}@{domain_name}"

    return current_login, current_email, current_password
