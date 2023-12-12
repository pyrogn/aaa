from keyword import iskeyword
from typing import Any, Protocol

Price = float | int


class Advert:
    """Object with dynamic attributes like in JavaScript.

    Methods
    -------
        check_root_level: Проверки первого уровня JSON
        price: property with price
    Attributes:
        json_dict: словарь с информацией
        _price: переменная для хранения цены
        is_root: флаг с указанием на корневой уровень JSON

    Можно изменить только price. Остальные атрибуты readonly,
    изменение возможно только при создании нового инстанса с новым аргументом json_dict
    """

    def __init__(self, json_dict: dict, *, is_root: bool = True):
        """Ицинциализация класса с динамическими атрибутами.

        Args:
        ----
            json_dict (dict): десериализованный JSON
            is_root (bool, optional): Флаг для проверки базового уровня JSON
                На более глубоких уровнях игнорируется проверка
                Defaults to True.
        """
        self.json_dict = json_dict
        self._price: Price
        self.is_root = is_root

        if is_root:
            self.check_root_level()

    def check_root_level(self) -> None:
        """Проверки первого уровня JSON на атрибуты price и title.

        При ошибке выбрасывает ValueError с текстом ошибки и атрибутом
        """
        try:
            self.price = self.json_dict["price"]
        except KeyError:
            self.price = 0
        except ValueError:
            raise

        try:
            self.json_dict["title"]
        except KeyError:
            raise ValueError("title is not present")

    @property
    def price(self) -> Price:
        return self._price

    @price.setter
    def price(self, value: Price):
        if not isinstance(value, Price):
            raise TypeError("price should have type int or float")
        if value < 0:
            raise ValueError("price cannot be less than 0")
        self._price = value

    def __getattr__(self, key: str) -> Any:
        if iskeyword(key[:-1]):
            key = key[:-1]

        value = self.json_dict[key]
        if isinstance(value, dict):
            return self.parse(value)
        elif isinstance(value, list):
            return [self.parse(json_obj) for json_obj in value]
        return value

    @classmethod
    def parse(cls, json_dict: dict) -> "Advert":
        """Create new instance on a subset of json_dict"""
        return cls(json_dict, is_root=False)

    def __str__(self) -> str:
        if not self.is_root:
            raise ValueError("It is neither root level of Advert nor value")
        return f"{self.title} | {self.price:d} ₽"

    def __repr__(self) -> str:
        if not self.is_root:
            raise ValueError("It is neither root level of Advert nor value")
        return f"Advert({self.json_dict})"


class HasReprColorProtocol(Protocol):
    repr_color_code: int


class ColorizeMixin:
    """Mixin for coloring output of __str__ method."""

    def __str__(self: HasReprColorProtocol):
        return f"\033[1;{self.repr_color_code};40m " + super().__str__()


class ColoredAdvert(ColorizeMixin, Advert):
    """Advert with colored std output.

    Attributes
    ----------
        repr_color_code (int): color code for coloring font
    """

    color_map: dict[str, int] = {
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
    }
    repr_color_code: int = color_map["yellow"]


if __name__ == "__main__":
    import json

    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 0,
        "class": "Programming Language",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.class_)
    print(lesson_ad.location.address)

    iphone_ad = ColoredAdvert({"title": "iPhone X", "price": 100})
    print(iphone_ad)
