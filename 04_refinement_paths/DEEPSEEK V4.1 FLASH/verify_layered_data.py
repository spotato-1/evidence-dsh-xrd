# -*- coding: utf-8 -*-
"""Compare observed data in the manual and plugin LayeredOxide GPX files."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(r"D:\AI\codex\workspace")
MODEL_ROOT = ROOT / "DEEPSEEK V4.1 FLASH"
GSAS_ROOT = ROOT / "DSH" / "dsh-portable" / "gsas"
sys.path.insert(0, str(GSAS_ROOT))
sys.path.insert(0, str(GSAS_ROOT / "GSASII"))

from GSASII import GSASIIscriptable as G2sc  # noqa: E402


MANUAL = ROOT / "测试" / "测试集" / "LayeredOxide" / "raw" / "手动精修结构" / "20260813 SG+BM.gpx"
PLUGIN = MODEL_ROOT / "dsh-xrd-test-evidence" / "runs" / "session-d37ffd1b-04a6-460e-8f04-733091bb8cf4" / "artifacts" / "LayeredOxide" / "LO_final" / "LO_final.gpx"


def compare(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    if left.shape != right.shape:
        return {"same_shape": False, "left_shape": left.shape, "right_shape": right.shape}
    delta = left - right
    slope, intercept = np.polyfit(left, right, 1)
    fit_residual = right - (slope * left + intercept)
    return {
        "same_shape": True,
        "n": int(left.size),
        "exact_equal": bool(np.array_equal(left, right)),
        "max_abs_diff": float(np.max(np.abs(delta))),
        "mean_abs_diff": float(np.mean(np.abs(delta))),
        "correlation": float(np.corrcoef(left, right)[0, 1]),
        "right_from_left_slope": float(slope),
        "right_from_left_intercept": float(intercept),
        "rmse_after_linear_transform": float(np.sqrt(np.mean(fit_residual**2))),
    }


def get_hist(path):
    project = G2sc.G2Project(gpxfile=str(path))
    hist = project.histograms()[0]
    arrays = hist.data["data"][1]
    metadata = hist.data["data"][0]
    return hist.name, arrays, {
        key: metadata.get(key)
        for key in ("Nobs", "R", "Rb", "wR", "wRb", "wRmin", "Durbin-Watson")
    }


def main():
    manual_name, manual, manual_res = get_hist(MANUAL)
    plugin_name, plugin, plugin_res = get_hist(PLUGIN)
    fields = ("x", "yobs", "weight", "ycalc", "ybkg", "ydiff")
    payload = {
        "manual": {"path": str(MANUAL), "histogram": manual_name, "residuals": manual_res},
        "plugin": {"path": str(PLUGIN), "histogram": plugin_name, "residuals": plugin_res},
        "comparisons": {field: compare(manual[i], plugin[i]) for i, field in enumerate(fields)},
    }
    output = Path(__file__).with_name("layered_data_identity.json")
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
