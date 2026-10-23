# DWA project-page figures

This folder supports the research overview at `/research/dwa/`.
It does not introduce a new training run.

## TGIF

- `tgif-idle.jpg`, `tgif-sewing.jpg`, `tgif-handling.jpg`: existing TGIF
  workstation frames at approximately 558 s, 417 s and 328 s, respectively,
  converted to JPEG without cropping or changing the scene. They illustrate
  the action classes; they are not new DWA prediction examples.
- `tgif_vibration_smoothing.png` and `tgif_timeline_seed43.png`: exact copies
  of the original project figures. The photo times and vibration excerpts
  differ. The timeline retains the original seed-43 “good-vibration validation
  subset” label; no new subset-selection rule is asserted.
- `data/tgif_confirmed_metrics.csv`: original reported validation values.
  These are separate from the WEAR v4 experiment.

Source: [TGIF project, commit 23ecc749](https://github.com/shureduan/TGIF-Multimodal-Temporal-Segmentation/tree/23ecc74921b1559cbf8fd2f0fc22dd36c59fb1ec).

## WEAR capture figure

- `wear-capture-setup.png`: unmodified figure from the
  [official WEAR website](https://mariusbock.github.io/wear/),
  [original image](https://mariusbock.github.io/wear/static/images/banner.png).
- Credit: Marius Bock, Hilde Kuehne, Kristof Van Laerhoven and Michael Moeller,
  *WEAR: An Outdoor Sports Dataset for Wearable and Egocentric Activity
  Recognition*, IMWUT 8(4), Article 175 (2024).
  [DOI: 10.1145/3699776](https://doi.org/10.1145/3699776).
- License: [Creative Commons Attribution–NonCommercial–ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
  The third-party figure retains this license.

## WEAR result figures

- `wear-timeline.svg` / `.png`: all time points from the released `sbj_1`
  timeline, filtered to ground truth, video-only and envelope-shape DWA.
  The original 19-class palette is retained.
- `wear-quality-speed.svg` / `.png`: released 18-subject seed-47 Macro-F1
  and CPU timing values. Timing averages five complete-model forwards per
  sequence, then averages equally over three sequences. It excludes loading,
  normalization and feature extraction.
- Bundled `data/aggregate_metrics.csv` and `data/inference_timing.csv` are
  exact copies from the
  [v4 results](https://github.com/shureduan/TGIF-Multimodal-Temporal-Segmentation/tree/23ecc74921b1559cbf8fd2f0fc22dd36c59fb1ec/results/wear_shape_v4).
  `data/timeline_sbj_1.csv` retains all time points for the three displayed tracks.
- Data-derived WEAR visualizations retain the dataset's CC BY-NC-SA 4.0 license.

Redraw the two simplified WEAR figures from this website repository:

```sh
python tools/build_dwa_page_figures.py
```

Dependencies: Python 3, numpy and matplotlib. Full model reproduction is covered
by the research repository's [reproduction guide](https://github.com/shureduan/TGIF-Multimodal-Temporal-Segmentation/blob/main/docs/envelope_shape_pilot.md).

`provenance.json` records asset origins and transformations.
