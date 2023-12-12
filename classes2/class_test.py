"Basic tests for Advert class and ColoredAdvert"
import json

import pytest

from class_hw import Advert, ColoredAdvert


@pytest.fixture()
def lesson_basic():
    return {
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"],
        },
    }


@pytest.fixture()
def lesson_keyword():
    return {
        "title": "python",
        "class": "I am keyword",
    }


@pytest.fixture()
def lesson_nested():
    return {
        "title": "flora",
        "listings": [
            {"flower": "dandelion"},
            {"flower": "for Algernon"},
        ],
    }


def test_select(lesson_basic):
    lesson_ad = Advert(lesson_basic)
    assert lesson_ad.location.address == "город Москва, Лесная, 7"
    with pytest.raises(KeyError, match="hello"):
        lesson_ad.hello
    with pytest.raises(
        ValueError, match="It is neither root level of Advert nor value"
    ):
        str(lesson_ad.location)


def test_price(lesson_basic):
    lesson_ad = Advert(lesson_basic)

    lesson_ad.price = 23
    assert lesson_ad.price == 23

    assert Advert({"title": "hello there"}).price == 0

    with pytest.raises(ValueError, match="price cannot be less than 0"):
        Advert({"title": "1", "price": -2})

    with pytest.raises(TypeError, match="price should have type int or float"):
        Advert({"title": "a", "price": {"level": 1}})


def test_title():
    with pytest.raises(ValueError, match="title is not present"):
        Advert({})
    assert Advert({"title": "titleName"}).title == "titleName"


def test_keywords(lesson_keyword):
    lesson_ad = Advert(lesson_keyword)
    assert lesson_ad.class_ == "I am keyword"


def test_nested(lesson_nested):
    ad = Advert(lesson_nested)
    assert ad.listings[1].flower == "for Algernon"


def test_colored():
    dog_str = """{
    "title": "Вельш-корги", "price": 1000,
    "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = ColoredAdvert(dog)
    assert str(dog_ad) == "\033[1;33;40m Вельш-корги | 1000 ₽"
