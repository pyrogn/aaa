"""
Написать в функциональном стиле функции get_names и get_object_names
реализующие (x['name'] for x in users) и (x.name for x in users).

Попробуйте сделать максимально переиспользуюемую реализацию:
1) Хотелось бы переиспользовать код, для работы со словарями и объектами
2) Что если нужно будет возвращать не names, а что-то другое?


Помогут:
1) from operator import itemgetter, attrgetter
2) from functools import partial
"""
from collections.abc import Sequence
from dataclasses import dataclass
from operator import itemgetter, attrgetter


@dataclass
class User:
    name: str
    age: int


users_objects = [User(name="Paul", age=28), User(name="Liz", age=18)]

users = [
    {"name": "Paul", "age": 28},
    {"name": "Liz", "age": 18},
]

name_key_getter = itemgetter("name")
name_attr_getter = attrgetter("name")


def get_names(users: Sequence[dict]) -> map:
    return map(name_key_getter, users)


def get_object_names(users: Sequence[User]) -> map:
    return map(name_attr_getter, users)


assert list(get_names(users)) == ["Paul", "Liz"]
assert list(get_object_names(users_objects)) == ["Paul", "Liz"]
