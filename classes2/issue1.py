from keyword import iskeyword
from collections import abc
import json


class Advert:
    def __init__(self, json_dict: dict):
        self.json_dict = json_dict
        if "price" in json_dict:
            self.price = json_dict["price"]

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float | int):
        if value < 0:
            raise ValueError("price cannot be less than 0")
        self._price = value

    def __getattr__(self, key):
        if iskeyword(key.strip("_")):
            key = key.strip("_")
        if isinstance(self.json_dict[key], abc.Mapping):
            return self.parse(self.json_dict[key])
        else:
            return self.json_dict[key]

    @classmethod
    def parse(cls, json_dict):
        return cls(json_dict)


if __name__ == "__main__":
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"],
            "assert": "I am keyword"
            }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    assert lesson_ad.location.assert_ == "I am keyword"

    lesson_ad.price = 23
    assert lesson_ad.price == 23

    try:
        Advert({"price": -2})
    except ValueError:
        print("avoided")
