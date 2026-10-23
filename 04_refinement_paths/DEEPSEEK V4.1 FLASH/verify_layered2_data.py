# -*- coding: utf-8 -*-
"""Verify whether the LayeredOxide_2ph answer GPX and raw files match."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(r"D:\AI\codex\workspace")
GSAS_ROOT = ROOT / "DSH" / "dsh-portable" / "gsas"
sys.path.insert(0, str(GSAS_ROOT))
sys.path.insert(0, str(GSAS_ROOT / "GSASII"))

from GSASII import GSASIIscriptable as G2sc  # noqa: E402


CASE = ROOT / "测试" / "测试集" / "LayeredOxide_2ph"
CSV_PATH = CASE / "raw" / "Na0.9K0.1.csv"
TXT_PATH = CASE / "raw" / "91.txt"
GPX_PATH = CASE / "answer" / "20251121.gpx"


def hash_array(values):
    array = np.ascontiguousarray(values, dtype=np.float64)
    return hashlib.sha256(array.tobytes()).hexdigest()


def stats(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    if left.shape != right.shape:
        return {"same_shape": False, "left_shape": left.shape, "right_shape": right.shape}
    diff = left - right
    return {
        "same_shape": True,
        "n": int(left.size),
        "exact_equal": bool(np.array_equal(left, right)),
        "allclose_1e-12": bool(np.allclose(left, right, rtol=0.0, atol=1e-12)),
        "max_abs_diff": float(np.max(np.abs(diff))),
        "mean_abs_diff": float(np.mean(np.abs(diff))),
        "correlation": float(np.corrcoef(left, right)[0, 1]) if left.size > 1 else None,
    }


def main():
    csv_data = np.genfromtxt(CSV_PATH, delimiter=",", names=True)
    txt_data = np.genfromtxt(TXT_PATH, names=True)

    project = G2sc.G2Project(gpxfile=str(GPX_PATH))
    hist = project.histograms()[0]
    arrays = hist.data["data"][1]
    x_gpx, yobs_gpx, w_gpx, ycalc_gpx, ybkg_gpx = arrays[:5]

    payload = {
        "sources": {
            "csv": str(CSV_PATH),
            "txt": str(TXT_PATH),
            "answer_gpx": str(GPX_PATH),
            "answer_histogram_name": hist.name,
        },
        "row_counts": {
            "csv": int(csv_data.shape[0]),
            "txt": int(txt_data.shape[0]),
            "gpx": int(len(x_gpx)),
        },
        "comparisons": {
            "csv_vs_txt_x": stats(csv_data["x"], txt_data["x"]),
            "csv_vs_txt_yobs": stats(csv_data["obs"], txt_data["y_obs"]),
            "csv_vs_gpx_x": stats(csv_data["x"], x_gpx),
            "csv_vs_gpx_yobs": stats(csv_data["obs"], yobs_gpx),
            "txt_vs_gpx_x": stats(txt_data["x"], x_gpx),
            "txt_vs_gpx_yobs": stats(txt_data["y_obs"], yobs_gpx),
            "txt_vs_gpx_weight": stats(txt_data["weight"], w_gpx),
            "txt_vs_gpx_ycalc": stats(txt_data["y_calc"], ycalc_gpx),
            "txt_vs_gpx_ybkg": stats(txt_data["y_bkg"], ybkg_gpx),
        },
        "fingerprints": {
            "csv_yobs_float64": hash_array(csv_data["obs"]),
            "txt_yobs_float64": hash_array(txt_data["y_obs"]),
            "gpx_yobs_float64": hash_array(yobs_gpx),
        },
        "gpx_residuals": {
            key: hist.data["data"][0].get(key)
            for key in ("Nobs", "R", "Rb", "wR", "wRb", "wRmin", "Durbin-Watson")
        },
        "interpretation": (
            "Observed intensities are the identity criterion. Small x differences are expected "
            "if 91.txt is a rounded export of the CSV/GPX grid."
        ),
    }

    output = Path(__file__).with_name("layered2_data_identity.json")
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
