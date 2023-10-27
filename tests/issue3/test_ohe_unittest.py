import unittest

from ..one_hot_encoder import fit_transform


class OHETestCase(unittest.TestCase):
    def test_fail_empty(self):
        with self.assertRaisesRegex(TypeError, "expected at least 1 arguments, got 0"):
            fit_transform()

    def test_fail_num(self):
        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            fit_transform(1)

    def test_fail_hash(self):
        with self.assertRaisesRegex(TypeError, "unhashable type: 'list'"):
            fit_transform("str", [1])

    def test_data_1(self):
        data = ("A", "a", "b")
        expected = [("A", [0, 0, 1]), ("a", [0, 1, 0]), ("b", [1, 0, 0])]
        out1 = fit_transform(data)
        out2 = fit_transform(*data)  # test that it can pack values back
        self.assertListEqual(expected, out1)
        self.assertListEqual(expected, out2)

    def test_data_2(self):
        data = ("A", "a", 1, (12,), "a")
        expected = [
            ("A", [0, 0, 0, 1]),
            ("a", [0, 0, 1, 0]),
            (1, [0, 1, 0, 0]),
            ((12,), [1, 0, 0, 0]),
            ("a", [0, 0, 1, 0]),
        ]
        self.assertGreater(len(fit_transform(data)), 0)  # sanity check
        self.assertEqual(expected, fit_transform(data))
