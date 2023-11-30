from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __mul__(self, other):
        ...

    @abstractmethod
    def __rmul__(self, other):
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...


END = "\033[0"
START = "\033[1;38;2"
MOD = "m"
ConstrastMult = float | int


class Color(ComputerColor):
    def __init__(self, r, g, b) -> None:
        self.rgb = (r, g, b)

    def __str__(self) -> str:
        red_level, green_level, blue_level = self.rgb
        return f"{START};{red_level};{green_level};{blue_level}{MOD}●{END}{MOD}"

    def __repr__(self) -> str:
        return f"Color{self.rgb}"

    def __eq__(self, other: "Color") -> bool:
        if not isinstance(other, Color):
            return NotImplemented
        return self.rgb == other.rgb

    def __hash__(self) -> int:
        return hash(self.rgb)

    def __add__(self, other: "Color") -> "Color":
        def clipped_sum(x):
            return min(sum(x), 255)

        new_color = map(clipped_sum, zip(self.rgb, other.rgb))
        return Color(*new_color)

    def __mul__(self, other: ConstrastMult) -> "Color":
        if not isinstance(other, ConstrastMult):
            return NotImplemented

        cl = -256 * (1 - other)
        F = (259 * (cl + 255)) / (255 * (259 - cl))

        def decrease_contrast(pixel_intensity):
            return int(F * (pixel_intensity - 128) + 128)

        new_color = map(decrease_contrast, self.rgb)
        return Color(*new_color)

    def __rmul__(self, other: ConstrastMult) -> "Color":
        return self * other


def print_a(color: ComputerColor) -> None:
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == "__main__":
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    print("red:", red)
    print("red equal green:", red == green)
    print("red equal red:", red == red)
    print("red+green:", red + green)

    color_list = [orange1, red, green, orange2]
    print("non unique colors:", *list(map(str, color_list)))
    print("unique colors:", *map(str, set(color_list)))

    print("red, half constrast:", 0.5 * red)

    hlsColor = Color(255, 0, 0)
    print_a(hlsColor)
