import pytest
from class_hw import Advert
import json

lesson_str = """{
    "title": "python",
    "price": 0,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"],
        "assert": "I am keyword"
        }
}"""


def test_price():
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    assert lesson_ad.location.assert_ == "I am keyword"

    lesson_ad.price = 23
    assert lesson_ad.price == 23

    assert Advert({"title": "hello there"}).price == 0

    with pytest.raises(ValueError):
        Advert({"title": "1", "price": -2})


def test_keywords():
    pass
