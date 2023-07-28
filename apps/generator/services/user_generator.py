from typing import NamedTuple
from collections.abc import Iterator

from . import get_credentials


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
    concurrent_credentials = get_credentials()

    return User(
        login=concurrent_credentials[0],
        email=concurrent_credentials[1],
        password=concurrent_credentials[2],
    )


def generate_users(amount=20) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
