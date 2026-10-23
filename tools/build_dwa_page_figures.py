#!/usr/bin/env python3
"""Redraw the project-page WEAR figures from the bundled release tables.

Run with Python, numpy and matplotlib. TGIF and official WEAR assets stay unchanged.
"""
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets/research/dwa'
DATA = ASSETS / 'data'

def read(name):
    with (DATA / name).open() as stream:
        return list(csv.DictReader(stream))

def save(fig, name):
    svg = ASSETS / f'{name}.svg'
    fig.savefig(svg, bbox_inches='tight', facecolor='white', metadata={'Date': None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()) + '\n')
    fig.savefig(ASSETS / f'{name}.png', dpi=160, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def main():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 11,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.edgecolor': '#CBD2D9', 'text.color': '#25313E',
        'axes.labelcolor': '#536171', 'xtick.color': '#536171',
        'ytick.color': '#25313E', 'svg.fonttype': 'none',
        'svg.hashsalt': 'dwa-project-page-v4',
    })
    timeline = read('timeline_sbj_1.csv')
    tracks = ['GT', 'VIDEO_ONLY', 'ENVELOPE_SHAPE_DWA']
    rows = [[r for r in timeline if r['track'] == track] for track in tracks]
    times = np.array([float(r['time_seconds']) for r in rows[0]])
    assert all(np.array_equal(times, [float(r['time_seconds']) for r in row]) for row in rows)
    array = np.array([[int(r['label']) for r in row] for row in rows])
    palette = plt.get_cmap('tab20')(np.linspace(0, 1, 19))
    names = [
        'Jogging', 'Jogging / arm rotation', 'Jogging / skipping',
        'Jogging / sidesteps', 'Jogging / butt-kicks',
        'Stretch / triceps', 'Stretch / lunging', 'Stretch / shoulders',
        'Stretch / hamstrings', 'Stretch / lumbar rotation',
        'Push-ups', 'Push-ups / complex', 'Sit-ups', 'Sit-ups / complex',
        'Burpees', 'Lunges', 'Lunges / complex', 'Bench-dips', 'Background',
    ]
    fig, ax = plt.subplots(figsize=(13, 4.3))
    ax.imshow(array, aspect='auto', interpolation='nearest',
              extent=(times[0] - .25, times[-1] + .25, 2.5, -.5),
              cmap=ListedColormap(palette), vmin=0, vmax=18)
    ax.set_yticks([0, 1, 2], ['Ground truth', 'Video-only', 'DWA (ours)'])
    ax.tick_params(axis='y', length=0, pad=12)
    for y in [.5, 1.5]:
        ax.axhline(y, color='white', lw=3)
    ax.set_xlabel('Time (seconds)', labelpad=9)
    ax.set_xlim(times[0] - .25, times[-1] + .25)
    ax.set_xticks(np.arange(0, times[-1] + 1, 500))
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.set_title('WEAR · held-out subject sbj_1 · seed 47', loc='left',
                 fontsize=13, fontweight='bold', pad=18)
    fig.legend([Patch(facecolor=c) for c in palette], names, loc='lower center',
               ncol=5, frameon=False, fontsize=8.8, columnspacing=1.8,
               handlelength=1.25, bbox_to_anchor=(.5, .005))
    fig.subplots_adjust(left=.12, right=.99, top=.86, bottom=.42)
    save(fig, 'wear-timeline')

    metrics = {r['method']: r for r in read('aggregate_metrics.csv')}
    old, new = 'SIGNAL_ADAPTIVE_DWA', 'ENVELOPE_SHAPE_DWA'
    timing = read('inference_timing.csv')
    subjects = ['sbj_0', 'sbj_9', 'sbj_17']
    means = {method: np.mean([
        np.mean([float(r['forward_seconds']) for r in timing
                 if r['method'] == method and r['subject'] == subject])
        for subject in subjects]) for method in [old, new]}
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 3.6))
    colors = ['#AFBCC9', '#137D77']
    for ax, values, title, ylabel, limit, fmt in [
        (axes[0], [100 * float(metrics[m]['macro_f1_19']) for m in [old, new]],
         'Recognition quality', 'Subject Macro-F1 (%)', (0, 90), '{:.2f}%'),
        (axes[1], [means[m] for m in [old, new]],
         'Complete-model CPU inference', 'Seconds per sequence', (0, 1.6), '{:.3f} s'),
    ]:
        bars = ax.bar([0, 1], values, width=.48, color=colors)
        ax.set_xticks([0, 1], ['Previous DWA (v3)', 'Shape DWA (v4)'])
        ax.set_ylabel(ylabel)
        ax.set_ylim(*limit)
        ax.set_title(title, loc='left', fontweight='bold', pad=20)
        ax.grid(axis='y', color='#E8ECF0', lw=.8)
        ax.set_axisbelow(True)
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='both', length=0)
        for bar, value in zip(bars, values):
            ax.annotate(fmt.format(value), (bar.get_x() + bar.get_width()/2, value),
                        xytext=(0, 7), textcoords='offset points', ha='center',
                        fontsize=12, fontweight='bold')
    fig.subplots_adjust(left=.07, right=.98, top=.84, bottom=.17, wspace=.32)
    save(fig, 'wear-quality-speed')
    print(f'Latency reduction: {100 * (1-means[new]/means[old]):.4f}%')
    print(f'Speedup: {means[old]/means[new]:.4f}x')
    print(f'Timeline: {len(times)} tokens per track; all time points retained')

if __name__ == '__main__':
    main()
