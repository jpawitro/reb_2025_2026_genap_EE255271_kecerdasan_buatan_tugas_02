"""
Test untuk fungsi fuzzy_suhu menggunakan struktur folder `src/`.
"""


import unittest
from src.fuzzy_script import fuzzy_suhu


class TestFuzzySuhu(unittest.TestCase):
    """Kelas pengujian untuk fungsi fuzzy_suhu."""

    def test_dingin(self):
        """Suhu di luar rentang fungsi keanggotaan Dingin harus menghasilkan 0."""
        self.assertEqual(fuzzy_suhu(30.0, 15, 15, 25), 0)

    def test_sedang(self):
        """Nilai suhu pada sisi turun fungsi keanggotaan Sedang harus menghasilkan nilai benar."""
        self.assertAlmostEqual(fuzzy_suhu(32.5, 15, 25, 35), 0.25)

    def test_panas(self):
        """Nilai suhu pada sisi naik fungsi keanggotaan Panas harus menghasilkan nilai benar."""
        self.assertAlmostEqual(fuzzy_suhu(32.5, 25, 35, 35), 0.75)


if __name__ == "__main__":
    unittest.main()
