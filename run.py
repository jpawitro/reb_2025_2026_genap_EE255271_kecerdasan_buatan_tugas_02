"""
Pembantu untuk menghasilkan plot dari root proyek.

Cara pakai:
    python run.py

Skrip ini memanggil fungsi `plot_memberships` dari `src.plot_fuzzy` dan
menyimpan keluaran ke `plots/memberships.png` (membuat direktori `plots/`
jika belum ada).
"""

import os
from src.plot_fuzzy import plot_memberships


def main() -> None:
    """
    Fungsi entrypoint untuk menghasilkan plot keanggotaan.
    """
    os.makedirs("plots", exist_ok=True)
    out = os.path.join("plots", "memberships.png")
    plot_memberships(save_path=out, show=False)
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
