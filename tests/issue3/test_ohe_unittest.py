import unittest

from ..one_hot_encoder import fit_transform


class OHETestCase(unittest.TestCase):
    def test_fail(self):
        with self.assertRaises(TypeError):
            fit_transform()
