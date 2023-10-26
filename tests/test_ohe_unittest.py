from .one_hot_encoder import fit_transform
import unittest


class OHETestCase(unittest.TestCase):
    def test_fail(self):
        with self.assertRaises(TypeError):
            fit_transform()
