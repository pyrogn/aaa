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
from dataclasses import dataclass
from operator import itemgetter, attrgetter
from functools import partial
from typing import Callable, Iterable, Literal


@dataclass
class User:
    name: str
    age: int


users_objects = [User(name="Paul", age=28), User(name="Liz", age=18)]

users = [
    {"name": "Paul", "age": 28},
    {"name": "Liz", "age": 18},
]


# Мне такой дизайн показался достаточно понятным.
# И через новую функцию или partial можно задефолтить key_name или obj_type
def get_getter(
    key_name: str,
    obj_type: Literal["dict", "class"],
) -> Callable[[Iterable], map]:
    # I use if-elif-else to evaluate only what is needed
    if obj_type == "dict":
        getter = itemgetter(key_name)
    elif obj_type == "class":
        getter = attrgetter(key_name)
    else:
        raise ValueError

    # я создаю closure, но если выносить функцию, надо добавить параметр getter
    def get_elems(data: Iterable) -> map:
        return map(getter, data)

    return get_elems


if __name__ == "__main__":
    get_names = get_getter("name", "dict")
    get_object_names = get_getter("name", "class")

    assert list(get_names(users)) == ["Paul", "Liz"]
    assert list(get_object_names(users_objects)) == ["Paul", "Liz"]
