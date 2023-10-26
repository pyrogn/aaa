from .one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        ("Moscow", [("Moscow", [1])]),
        (["Moscow"], [("Moscow", [1])]),
    ],
)
def test_ok(input, output):
    assert fit_transform(input) == output


def test_fail():
    with pytest.raises(TypeError):
        fit_transform()
