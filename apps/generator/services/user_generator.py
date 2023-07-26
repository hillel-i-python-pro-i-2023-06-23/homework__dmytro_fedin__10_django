from typing import NamedTuple
from collections.abc import Iterator
from . import faker


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
        login=faker.unique.user_name(),
        email=faker.unique.email(),
        password=faker.unique.password(),
    )


def generate_users(amount=20) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
