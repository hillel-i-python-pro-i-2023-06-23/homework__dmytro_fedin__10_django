from typing import NamedTuple
from collections.abc import Iterator
from . import fake_user


class User(NamedTuple):
    login: str
    email: str
    password: str

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(**data)


def generate_user() -> User:
    return User(
        login=fake_user.get_login(),
        email=fake_user.get_password(),
        password=fake_user.get_email(),
    )


def generate_users(amount=20) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
