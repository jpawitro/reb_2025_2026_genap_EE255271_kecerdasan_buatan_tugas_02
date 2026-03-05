"""
Modul Logika Fuzzy - Tugas 2 Kecerdasan Buatan (EE255271)

File ini identik dengan implementasi sebelumnya tetapi diletakkan di bawah
`src/` agar struktur proyek lebih rapi.
"""


def fuzzy_suhu(suhu, a, b, c):
    """Menghitung derajat keanggotaan suhu menggunakan fungsi segitiga.

    Parameter:
        suhu (float): Nilai suhu yang akan dihitung derajat keanggotaannya.
        a (float): Batas bawah fungsi keanggotaan (titik awal naik).
        b (float): Titik puncak fungsi keanggotaan (derajat keanggotaan = 1).
        c (float): Batas atas fungsi keanggotaan (titik akhir turun).

    Kembalian:
        float: Derajat keanggotaan bernilai antara 0 dan 1.
    """
    # Tangani segitiga degenerate untuk menghindari pembagian dengan nol.
    # Jika sisi kiri vertikal (b == a) maka derajat keanggotaan 1 hanya pada b.
    if b == a:
        if suhu < b:
            return 1.0
    else:
        if a <= suhu <= b:
            return (suhu - a) / (b - a)

    # Jika sisi kanan vertikal (c == b) maka derajat keanggotaan 1 hanya pada b.
    if c == b:
        if suhu >= c:
            return 1.0
        return 0.0
    else:
        if b <= suhu <= c:
            return (c - suhu) / (c - b)

    return 0.0
