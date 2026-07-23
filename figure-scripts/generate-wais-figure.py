"""
WAIS-IV Higher-Order Factor Model Path Diagram
==============================================

Recreates the hierarchical factor model showing:
  - Level 1: Observed subtests (rectangles)
  - Level 2: First-order latent factors / broad abilities (ovals)
  - Level 3: Second-order factor = g / Full Scale IQ (oval)

Run: python wais_iv_path_diagram.py

Dependencies: matplotlib, numpy
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import numpy as np

# ============================================================
#  CONFIGURATION — Edit these values to customize the figure
# ============================================================

plt.rcParams["font.family"] = "Roboto Condensed"
FIG_WIDTH = 6
FIG_HEIGHT = 6
DPI = 150
TITLE = "WAIS-IV Higher-Order Factor Model"

# Colors (change to your liking)
COLOR_RECT = "#FFFFFF"       # Subtest boxes
COLOR_OVAL_FIRST = "#FFFFFF" # First-order factors
COLOR_OVAL_SECOND = "#FFFFFF" # g / Full Scale IQ
EDGE_COLOR = "black"
TEXT_COLOR = "black"
ARROW_COLOR = "black"

# Font sizes
FONT_SUBTEST = 11
FONT_FACTOR = 12
FONT_G = 13
FONT_LOADING = 10

# ============================================================
#  DATA STRUCTURE — The model specification
# ============================================================

# Subtests organized under their first-order factor
# Format: (subtest_name, loading_on_factor)
SUBTESTS = {
    "Verbal Comprehension": [
        ("Similarities",   0.77),
        ("Vocabulary",     0.90),
        ("Information",    0.74),
    ],
    "Perceptual Reasoning": [
        ("Block Design",      0.74),
        ("Matrix Reasoning",  0.66),
        ("Visual Puzzles",    0.73),
    ],
    "Working Memory": [
        ("Digit Span",   0.65),
        ("Arithmetic",   0.90),
    ],
    "Processing Speed": [
        ("Symbol Search", 0.73),
        ("Coding",        0.82),
    ],
}

# Second-order loadings (broad ability -> g)
SECOND_ORDER_LOADINGS = {
    "Verbal Comprehension":  0.82,
    "Perceptual Reasoning":  0.96,
    "Working Memory":        0.82,
    "Processing Speed":      0.76,
}


def draw_rectangle(ax, x, y, width, height, text, fontsize=FONT_SUBTEST):
    """Draw a rectangle (observed variable) with centered text."""
    rect = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="square,pad=0",
        facecolor=COLOR_RECT, edgecolor=EDGE_COLOR, linewidth=1.5,
        zorder=2,
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, color=TEXT_COLOR, zorder=3)


def draw_oval(ax, x, y, width, height, text, fontsize=FONT_FACTOR):
    """Draw an oval (latent variable) with centered text."""
    oval = Ellipse(
        (x, y), width, height,
        facecolor=COLOR_OVAL_FIRST, edgecolor=EDGE_COLOR, linewidth=1.5,
        zorder=2,
    )
    ax.add_patch(oval)
    
    # Handle multi-line text in ovals
    lines = text.split("\n")
    if len(lines) > 1:
        line_height = fontsize / 72 * 1.5  # approximate
        for i, line in enumerate(lines):
            offset = (i - (len(lines)-1)/2) * line_height
            ax.text(x, y + offset, line, ha="center", va="center",
                    fontsize=fontsize, color=TEXT_COLOR, zorder=3)
    else:
        ax.text(x, y, text, ha="center", va="center",
                fontsize=fontsize, color=TEXT_COLOR, zorder=3)


def draw_arrow(ax, start, end, label=None, label_offset=(0, 0),
               curved=False, color=ARROW_COLOR):
    """Draw an arrow from start to end, optionally with a loading label."""
    style = f"Simple,tail_width=0.5,head_width=4,head_length=8"
    if curved:
        conn = FancyArrowPatch(
            start, end,
            connectionstyle=f"arc3,rad={0.15}",
            arrowstyle=style, color=color, linewidth=1.2,
            zorder=1,
        )
    else:
        conn = FancyArrowPatch(
            start, end,
            connectionstyle="arc3,rad=0",
            arrowstyle=style, color=color, linewidth=1.2,
            zorder=1,
        )
    ax.add_patch(conn)

    # Add loading label near the middle of the arrow
    if label is not None:
        mid_x = (start[0] + end[0]) / 2 + label_offset[0]
        mid_y = (start[1] + end[1]) / 2 + label_offset[1]
        ax.text(mid_x, mid_y, f"{label:.2f}", ha="center", va="center",
                fontsize=FONT_LOADING, color=TEXT_COLOR,
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                          edgecolor="none", alpha=0.8),
                zorder=4)


def build_diagram():
    """Build the complete path diagram."""

    fig, ax = plt.subplots(1, 1, figsize=(FIG_WIDTH, FIG_HEIGHT), dpi=DPI)
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 11)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(TITLE, fontsize=16, fontweight="bold", pad=20)

    # ---- Layout coordinates ----
    
    # Column positions
    COL_SUBTESTS = 1.5     # x-position of observed variables (rectangles)
    COL_FACTORS  = 6.0     # x-position of first-order factors (ovals)
    COL_G        = 10.5    # x-position of g / Full Scale IQ (oval)

    # Vertical spacing
    SUBTEST_HEIGHT = 0.7
    SUBTEST_GAP = 0.35
    FACTOR_HEIGHT = 1.6
    FACTOR_WIDTH  = 3.0
    RECT_WIDTH  = 3.0
    G_WIDTH  = 2.8
    G_HEIGHT = 1.8

    # ---- Draw subtests (left column) ----
    y_sub = 10.0  # starting y position (top)
    subtest_positions = {}   # {name: (x, y)}
    factor_positions = {}    # {name: (x, y)}

    for factor_name, tests in SUBTESTS.items():
        factor_y_center = y_sub - (len(tests) - 1) * (SUBTEST_HEIGHT + SUBTEST_GAP) / 2
        factor_positions[factor_name] = (COL_FACTORS, factor_y_center)

        for test_name, loading in tests:
            draw_rectangle(ax, COL_SUBTESTS, y_sub, RECT_WIDTH, SUBTEST_HEIGHT, test_name)
            subtest_positions[test_name] = (COL_SUBTESTS, y_sub)
            
            # Arrow from factor to subtest
            draw_arrow(
                ax,
                start=(COL_FACTORS - FACTOR_WIDTH/2 + 0.1, factor_y_center),
                end=(COL_SUBTESTS + RECT_WIDTH/2, y_sub),
                label=loading,
                label_offset=(0.25, 0),
            )
            y_sub -= SUBTEST_HEIGHT + SUBTEST_GAP

        # Extra gap between factor groups
        y_sub -= 0.5

    # ---- Draw first-order factors (middle column) ----
    for factor_name, (fx, fy) in factor_positions.items():
        draw_oval(ax, fx, fy, FACTOR_WIDTH, FACTOR_HEIGHT, factor_name)

    # ---- Draw second-order factor g (right column) ----
    g_y = 5.5  # vertically center it
    draw_oval(ax, COL_G, g_y, G_WIDTH, G_HEIGHT, "Full Scale IQ",
              fontsize=FONT_G)

    # ---- Arrows from g to each first-order factor ----
    for factor_name, loading in SECOND_ORDER_LOADINGS.items():
        fx, fy = factor_positions[factor_name]
        
        # Determine label offset direction
        if fy > g_y + 0.5:
            loffset = (0.3, 0.2)   # above-right
        elif fy < g_y - 0.5:
            loffset = (0.3, -0.2)  # below-right
        else:
            loffset = (0.4, 0)     # straight right
        
        draw_arrow(
            ax,
            start=(COL_G, g_y),
            end=(fx + FACTOR_WIDTH/2 - 0.1, fy),
            label=loading,
            label_offset=loffset,
        )

    plt.tight_layout()
    return fig, ax


if __name__ == "__main__":
    fig, ax = build_diagram()
    
    # Save to file
    output_file = "../input/svg/wais_iv_path_diagram.svg"
    fig.savefig(output_file, dpi=DPI, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    print(f"✅ Figure saved to: {output_file}")
        
    plt.show()
