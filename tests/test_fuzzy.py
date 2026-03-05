"""
Test untuk fungsi fuzzy_suhu menggunakan struktur folder `src/`.

Test ini menambahkan `src/` ke `sys.path` agar modul yang dipindahkan
dapat diimport tanpa pemasangan paket.
"""


import unittest
from src.fuzzy_script import fuzzy_suhu


class TestFuzzySuhu(unittest.TestCase):
    """Kelas pengujian untuk fungsi fuzzy_suhu."""

    def test_di_luar_rentang(self):
        """Nilai suhu di luar rentang harus menghasilkan 0."""
        self.assertEqual(fuzzy_suhu(32.5, 0, 10, 25), 0)

    def test_sisi_turun(self):
        """Nilai suhu pada sisi turun segitiga harus menghasilkan nilai benar."""
        self.assertAlmostEqual(fuzzy_suhu(32.5, 10, 25, 35), 0.25)

    def test_sisi_naik(self):
        """Nilai suhu pada sisi naik segitiga harus menghasilkan nilai benar."""
        self.assertAlmostEqual(fuzzy_suhu(32.5, 25, 35, 35), 0.75)


if __name__ == "__main__":
    unittest.main()
