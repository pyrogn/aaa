"""Morse Code Translator"""

LETTER_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "|",  # В Морзе разделение между словами - 7 точек по длительности (факт)
}

MORSE_TO_LETTER = {morse: letter for letter, morse in LETTER_TO_MORSE.items()}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('HELLO THERE')
    '.... . .-.. .-.. --- | - .... . .-. .'

    Не все символы есть в словаре
    >>> encode('!HOLA')
    Traceback (most recent call last):
    ...
    KeyError: '!'

    А это мы пропустим
    >>> encode('please write your message in UPPERCASE') # doctest: +SKIP

    Абьюз точек и бесконечная любовь к функциям
    >>> list(map(encode, ['AB', 'TEXT', 'CD'])) # doctest: +ELLIPSIS
    ['.- -...',\t...,        '-.-. -..']

    Надеюсь, не пригодится, но лучше знать
    >>> encode('SOS')
    '... --- ...'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [MORSE_TO_LETTER[letter] for letter in morse_message.split(" ")]

    return "".join(decoded_letters)


if __name__ == "__main__":  # haven't touched this part
    morse_msg = "-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----."
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
