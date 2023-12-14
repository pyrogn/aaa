from collections.abc import Callable, Iterable
from itertools import islice
from typing import Any


class Seq:
    def __init__(self, seq: Iterable):
        self.seq = seq

    def filter(self, f: Callable[[Any], bool]) -> "Seq":
        return Seq(filter(f, self.seq))

    def map(self, f: Callable[[Any], Any]) -> "Seq":
        return Seq(map(f, self.seq))

    def take(self, n: int) -> tuple:
        return tuple(islice(self.seq, 0, n))


if __name__ == "__main__":
    # numbers = [1, 2, 3, 4, 5]
    numbers = range(1, int(1e100))  # подтверждаем ленивость
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(2)
    assert res == tuple([12, 14])
