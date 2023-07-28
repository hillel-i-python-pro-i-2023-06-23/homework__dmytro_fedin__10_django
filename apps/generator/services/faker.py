import string

from faker import Faker


def get_credentials():
    current_faker = Faker()
    characters = string.ascii_letters + string.digits + "_"
    login_template = current_faker.lexify(text="????????", letters=characters)
    text_template = current_faker.lexify(text="???", letters=characters)

    def get_login():
        return login_template

    def get_text():
        return text_template

    def get_password():
        return current_faker.unique.password()

    def get_email():
        current_login = get_login()
        current_text = get_text()
        current_password = get_password()
        domain_name = current_faker.unique.domain_name()

        current_email = f"{current_login}{current_text}@{domain_name}"

        return current_login, current_email, current_password

    return get_email()
