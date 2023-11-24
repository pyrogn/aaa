from collections import abc
import json
from keyword import iskeyword
from typing import Any

Price = float


class Advert:
    """_summary_

    Данное решение не создаёт внутренние структуры, но и не даёт
    ничего изменить, кроме цены - property
    """

    def __init__(self, json_dict: dict, *, is_root: bool = True):
        self.json_dict = json_dict  # атрибут, но можно ли его убрать?
        if is_root:
            self.checks_root_branch()

    def checks_root_branch(self) -> None:
        try:
            self.price = self.json_dict["price"]
        except KeyError:
            self.price = 0
        except ValueError:
            raise
        try:
            self.json_dict["title"]
        except KeyError:
            raise ValueError("Title is not present")

    @property
    def price(self) -> Price:
        return self._price

    @price.setter
    def price(self, value: Price):
        if value < 0:
            raise ValueError("price cannot be less than 0")
        self._price = value

    def __getattr__(self, key: str) -> Any:
        if iskeyword(key.strip("_")):
            key = key.strip("_")
        if isinstance(self.json_dict[key], abc.Mapping):
            return self.parse(self.json_dict[key])
        else:
            return self.json_dict[key]

    @classmethod
    def parse(cls, json_dict: dict) -> "Advert":
        return cls(json_dict, is_root=False)

    def __str__(self) -> str:
        return f"{self.title} | {self.price:d} ₽"

    def __repr__(self) -> str:
        return f"Advert({self.json_dict})"


class ColorizeMixin:
    def __init_subclass__(cls, repr_color_code=32) -> None:
        super().__init_subclass__()
        if repr_color_code != 32:
            cls.repr_color_code = repr_color_code

    def __str__(self):
        return f"\033[1;{self.repr_color_code};40m " + super().__str__()


class ColoredAdvert(ColorizeMixin, Advert):
    repr_color_code = 33


if __name__ == "__main__":
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    iphone_ad = ColoredAdvert({"title": "iPhone X", "price": 100})
    print(iphone_ad)
