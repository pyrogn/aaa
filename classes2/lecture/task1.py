class Pokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f"{self.name}/{self.poketype}"


class EmojiMixin:
    map_emoji = {
        "grass": "\N{herb}",
        "fire": "\N{fire}",
        "water": "\N{water wave}",
        "electric": "\N{HIGH VOLTAGE SIGN}",
    }

    def __str__(self):
        self.poketype = self.map_emoji[self.poketype]
        return super().__str__()


class Pokemon2(EmojiMixin, Pokemon):
    "Pokemon with emoji"


if __name__ == "__main__":
    bulbasaur = Pokemon2(name="Bulbasaur", poketype="electric")
    print(bulbasaur)
