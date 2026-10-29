from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-5, 5, 1200)
    functions = [
        ("y = x²", x, x**2),
        ("y = x³", x, x**3),
        ("y = sin(x)", x, np.sin(x)),
        ("y = cos(x)", x, np.cos(x)),
        ("y = eˣ", x, np.exp(x)),
        ("y = |x|", x, np.abs(x)),
        ("y = √x", x[x >= 0], np.sqrt(x[x >= 0])),
        ("y = ln(x)", x[x > 0], np.log(x[x > 0])),
        ("y = 1/x", x[np.abs(x) > 0.1], 1 / x[np.abs(x) > 0.1]),
        (
            "y = tan(x)",
            x[np.abs(np.cos(x)) > 0.08],
            np.tan(x[np.abs(np.cos(x)) > 0.08]),
        ),
    ]

    figure, axes = plt.subplots(5, 2, figsize=(12, 16))
    for axis, (title, function_x, function_y) in zip(axes.flat, functions):
        axis.plot(function_x, function_y, color="#2563eb", linewidth=2)
        axis.set_title(title)
        axis.set_xlabel("x")
        axis.set_ylabel("y")
        axis.grid(True, alpha=0.3)
        axis.axhline(0, color="black", linewidth=0.7, alpha=0.5)
        axis.axvline(0, color="black", linewidth=0.7, alpha=0.5)

    figure.suptitle("Graphs of 10 Different Functions", fontsize=18)
    figure.tight_layout(rect=(0, 0, 1, 0.98))
    output_path = Path(__file__).with_name("functions.png")
    figure.savefig(output_path, dpi=160)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
