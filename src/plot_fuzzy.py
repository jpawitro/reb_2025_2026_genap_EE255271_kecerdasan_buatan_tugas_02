"""
Plot fungsi keanggotaan fuzzy.
"""

from __future__ import annotations

import os
from typing import Iterable, Optional

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.fuzzy_script import fuzzy_suhu


def _membership_values(a: float, b: float, c: float, xs: Iterable[float]) -> np.ndarray:
    """Hitung derajat keanggotaan untuk sekumpulan nilai `xs`.
    """
    return np.array([fuzzy_suhu(float(x), a, b, c) for x in xs])


def plot_memberships(xmin: float = 10.0,
                     xmax: float = 40.0,
                     num: int = 401,
                     save_path: Optional[str] = None,
                     show: bool = True) -> None:
    """Buat plot 3 subplots (1 kolom x 3 baris) untuk ketiga case.
    """
    sns.set_theme(style="whitegrid")

    xs = np.linspace(xmin, xmax, num)

    cases = [
        ("Dingin", (15, 15, 25), r"$\mu_{tD}(t)$"),
        ("Sedang", (15, 25, 35), r"$\mu_{tS}(t)$"),
        ("Panas",  (25, 35, 35), r"$\mu_{tP}(t)$"),
    ]

    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(6, 9))

    palette = sns.color_palette("deep", n_colors=3)

    for i, ax in enumerate(axes):
        name, (a, b, c), ylabel_tex = cases[i]
        ys = _membership_values(a, b, c, xs)

        ax.plot(xs, ys, label=name, color=palette[i])
        ax.fill_between(xs, ys, color=palette[i], alpha=0.15)
        ax.set_ylabel(ylabel_tex)
        ax.legend(loc="upper right")
        ax.set_ylim(-0.05, 1.05)

    axes[-1].set_xlabel("Temperatur t")

    plt.tight_layout()

    if save_path:
        outdir = os.path.dirname(save_path)
        if outdir:
            os.makedirs(outdir, exist_ok=True)
        fig.savefig(save_path, dpi=150)

    if show:
        plt.show()
