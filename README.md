# Tugas 2 — Logika Fuzzy

## Deskripsi

Proyek ini mengimplementasikan fungsi keanggotaan fuzzy segitiga (*triangular membership function*) untuk variabel suhu. Terdapat tiga kategori linguistik:

| Kategori | Titik (a, b, c) |
|----------|-----------------|
| Dingin   | (15, 15, 25)    |
| Sedang   | (15, 25, 35)    |
| Panas    | (25, 35, 35)    |

Rentang temperatur yang digunakan untuk visualisasi adalah $t \in [10, 40]$.

Derajat keanggotaan dihitung dengan rumus:

$$
\mu(t) =
\begin{cases}
1 & \text{jika } t = a = b = c \\
1 & \text{jika } t \leq a = b \\
\dfrac{t - a}{b - a} & \text{jika } a < t \leq b \\
\dfrac{c - t}{c - b} & \text{jika } b \leq t < c \\
1 & \text{jika } b = c \leq t \\
0 & \text{lainnya}
\end{cases}
$$

---

## Struktur Proyek

```
.
├── run.py              # Entrypoint: generate plot keanggotaan
├── pyproject.toml      # Konfigurasi tools (black, isort)
├── .env                # PYTHONPATH untuk keperluan pengujian di VS Code
├── src/
│   ├── fuzzy_script.py # Implementasi fungsi keanggotaan fuzzy
│   └── plot_fuzzy.py   # Plot fungsi keanggotaan (matplotlib + seaborn)
├── tests/
│   └── test_fuzzy.py   # Unit test (unittest)
├── plots/              # Hasil plot (di-generate oleh run.py)
└── report/             # Laporan LaTeX
```

---

## Cara Menjalankan

### Prasyarat

Pastikan dependensi sudah terpasang:

```bash
pip install numpy matplotlib seaborn
```

### Generate Plot

```bash
python run.py
```

Hasil plot disimpan di `plots/memberships.png`.

### Menjalankan Unit Test

```bash
python -m unittest discover -s tests
```

---

## Lisensi

Proyek ini dibuat untuk keperluan tugas akademik.
