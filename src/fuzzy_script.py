"""
Modul Logika Fuzzy - Tugas 2 Kecerdasan Buatan (EE255271)
"""


def fuzzy_suhu(suhu: float, a: float, b: float, c: float) -> float:
    """Menghitung derajat keanggotaan suhu menggunakan fungsi segitiga.

    Parameter:
        suhu (float): Nilai suhu yang akan dihitung derajat keanggotaannya.
        a (float): Batas bawah fungsi keanggotaan (titik awal naik).
        b (float): Titik puncak fungsi keanggotaan (derajat keanggotaan = 1).
        c (float): Batas atas fungsi keanggotaan (titik akhir turun).

    Kembalian:
        float: Derajat keanggotaan bernilai antara 0 dan 1.
    """
    # Kasus khusus: a == b == c (titik tunggal), hindari pembagian nol total.
    if a == b == c == suhu:
        return 1.0

    # Left shoulder: a == b, bernilai 1 untuk semua suhu di sisi kiri puncak.
    elif suhu <= a == b:
        return 1.0

    # Sisi naik hanya valid saat b > a, sehingga aman dari pembagian nol.
    elif a < suhu <= b:
        return (suhu - a) / (b - a)

    # Right shoulder: b == c, bernilai 1 untuk semua suhu di sisi kanan puncak.
    elif b == c <= suhu:
        return 1.0

    # Sisi turun hanya valid saat c > b, sehingga aman dari pembagian nol.
    elif b <= suhu < c:
        return (c - suhu) / (c - b)

    else:
        return 0.0
