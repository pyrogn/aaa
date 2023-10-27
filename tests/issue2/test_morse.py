from ..morse import decode
import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        ("... --- ...", "SOS"),
        (".... . .-.. .-.. --- | - .... . .-. .", "HELLO THERE"),
    ],
)
def test_decode(input, output):
    """Testing correct messages"""
    assert decode(input) == output


@pytest.mark.parametrize(
    "input",
    [
        ", --- ...",
        "...... . .-.. .-.. --- | - .... . .-. .",
    ],
)
def test_decode_fail(input):
    """Should fail on broken messages"""
    with pytest.raises(KeyError):
        decode(input)
