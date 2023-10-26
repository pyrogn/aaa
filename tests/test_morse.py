from morse import decode
import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        ("... --- ...", "SOS"),
        (".... . .-.. .-.. --- | - .... . .-. .", "HELLO THERE"),
    ],
)
def test_decode(input, output):
    assert decode(input) == output


@pytest.mark.parametrize(
    "input",
    [
        ", --- ...",
        "...... . .-.. .-.. --- | - .... . .-. .",
    ],
)
def test_decode_fail(input):
    with pytest.raises(KeyError):
        decode(input)
