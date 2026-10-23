# -*- coding: utf-8 -*-
"""Read-only comparison of final GPX projects shared by both model campaigns."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np


ROOT = Path(r"D:\AI\codex\workspace")
GSAS_ROOT = ROOT / "DSH" / "dsh-portable" / "gsas"
sys.path.insert(0, str(GSAS_ROOT))
sys.path.insert(0, str(GSAS_ROOT / "GSASII"))

from GSASII import GSASIIscriptable as G2sc  # noqa: E402


PROJECTS = {
    "Fe2O3_Fe3O4_2ph": {
        "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-588a939a-a652-444f-9fd7-b5e427b2d84f" / "artifacts" / "Fe2O3_Fe3O4_2ph" / "Fe2O3_Fe3O4_2ph_final" / "Fe2O3_Fe3O4_2ph_final.gpx",
        "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-d40fa1a9-2b14-44eb-9eef-3f176c3101e2" / "artifacts" / "Fe2O3_Fe3O4_2ph" / "Fe2O3_Fe3O4_2ph_final" / "Fe2O3_Fe3O4_2ph_final.gpx",
    },
    "FE50": {
        "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-23c57f48-47b8-49e3-a32b-59dc7992f390" / "artifacts" / "FE50" / "FE50_final" / "FE50_final.gpx",
        "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-4b077d73-ddc4-4bfc-8950-a958ddeda1d7" / "artifacts" / "FE50" / "deliverables" / "FE50_final" / "FE50_final.gpx",
    },
    "Fluoroapatite": {
        "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-92f1897c-c6c8-4c4d-b45f-37dcd4ea2d63" / "artifacts" / "Fluoroapatite" / "FAP_final" / "FAP_final.gpx",
        "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-d219da8b-d575-4d6b-982c-b91137ef5b2f" / "artifacts" / "Fluoroapatite" / "Fluoroapatite_final" / "Fluoroapatite_final.gpx",
    },
    "LayeredOxide": {
        "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-d37ffd1b-04a6-460e-8f04-733091bb8cf4" / "artifacts" / "LayeredOxide" / "LO_final" / "LO_final.gpx",
        "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-e3dc1b53-7232-4c25-8d7f-c8462e17a85b" / "artifacts" / "LayeredOxide" / "LayeredOxide_final" / "LayeredOxide_final.gpx",
    },
    "LiFePO4": {
        "deepseek": ROOT / "DEEPSEEK V4.1 FLASH" / "dsh-xrd-test-evidence" / "runs" / "session-ae4d57b2-f73e-40d2-ad3d-91e64c9602e0" / "artifacts" / "LiFePO4" / "LiFePO4_final" / "LiFePO4_final.gpx",
        "gpt56": ROOT / "GPT 5.6 SOL" / "dsh-xrd-test-evidence" / "runs" / "session-e03ae580-d18c-423f-806e-9920746a5e8e" / "workspace_snapshot" / "LiFePO4_best_physical_final" / "LiFePO4_best_physical_final.gpx",
    },
}


def simple(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    if isinstance(value, (list, tuple)):
        return [simple(item) for item in value]
    if isinstance(value, dict):
        return {str(key): simple(item) for key, item in value.items()}
    return repr(value)


def scalar_parameter(entry):
    if isinstance(entry, (list, tuple)):
        # GSAS-II instrument parameters are normally [original, current, refine].
        candidates = entry[1:2] if len(entry) >= 2 else entry
        for item in candidates:
            if isinstance(item, (int, float, np.number)) and not isinstance(item, bool):
                return float(item)
    if isinstance(entry, (int, float, np.number)) and not isinstance(entry, bool):
        return float(entry)
    return None


def compare_arrays(left, right):
    left = np.asarray(left, dtype=float)
    right = np.asarray(right, dtype=float)
    if left.shape != right.shape:
        return {"same_shape": False, "left_shape": list(left.shape), "right_shape": list(right.shape)}
    delta = right - left
    return {
        "same_shape": True,
        "n": int(left.size),
        "exact_equal": bool(np.array_equal(left, right)),
        "max_abs_diff": float(np.max(np.abs(delta))),
        "mean_abs_diff": float(np.mean(np.abs(delta))),
        "correlation": float(np.corrcoef(left, right)[0, 1]),
    }


def extract(path):
    project = G2sc.G2Project(gpxfile=str(path))
    hist = project.histograms()[0]
    metadata = hist.data["data"][0]
    arrays = [np.asarray(array, dtype=float) for array in hist.data["data"][1][:6]]
    instrument_blocks = hist.data.get("Instrument Parameters", [])
    instrument = instrument_blocks[0] if instrument_blocks else {}
    phases = []
    for phase in project.phases():
        general = phase.data.get("General", {})
        hist_values = phase.data.get("Histograms", {}).get(hist.name, {})
        phases.append(
            {
                "name": phase.name,
                "space_group": general.get("SGData", {}).get("SpGrp"),
                "cell": simple(phase.get_cell()),
                "composition_per_cell": simple(phase.composition),
                "density": float(phase.density),
                "scale": simple(hist_values.get("Scale")),
                "phase_fraction": simple(hist_values.get("PhaseFraction")),
                "atoms": [
                    {
                        "label": atom.label,
                        "element": atom.element,
                        "occupancy": float(atom.occupancy),
                        "adp_type": atom.adp_flag,
                        "adp": simple(atom.ADP),
                    }
                    for atom in phase.atoms()
                ],
            }
        )
    current_instrument = {key: scalar_parameter(instrument.get(key)) for key in ("Lam", "Lam1", "Lam2", "Zero", "U", "V", "W", "X", "Y", "SH/L")}
    theta = np.deg2rad(arrays[0] / 2.0)
    tan_theta = np.tan(theta)
    cos_theta = np.cos(theta)
    gaussian_width_term = (
        current_instrument["U"] * tan_theta**2
        + current_instrument["V"] * tan_theta
        + current_instrument["W"]
    )
    lorentz_width_term = current_instrument["X"] / cos_theta + current_instrument["Y"] * tan_theta
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "histogram": hist.name,
        "residuals": simple({key: metadata.get(key) for key in ("Nobs", "R", "Rb", "wR", "wRb", "wRmin", "Durbin-Watson")}),
        "instrument": current_instrument,
        "profile_domain_diagnostic": {
            "two_theta_min": float(np.min(arrays[0])),
            "two_theta_max": float(np.max(arrays[0])),
            "gaussian_width_term_min": float(np.min(gaussian_width_term)),
            "gaussian_width_term_max": float(np.max(gaussian_width_term)),
            "gaussian_nonpositive_fraction": float(np.mean(gaussian_width_term <= 0)),
            "lorentz_width_term_min": float(np.min(lorentz_width_term)),
            "lorentz_width_term_max": float(np.max(lorentz_width_term)),
            "lorentz_nonpositive_fraction": float(np.mean(lorentz_width_term <= 0)),
            "formula_note": "Diagnostic only: G=U*tan(theta)^2+V*tan(theta)+W; L=X/cos(theta)+Y*tan(theta).",
        },
        "phases": phases,
        "arrays": arrays,
    }


def main():
    output = {"note": "Read-only extraction; source GPX files were not modified.", "cases": {}}
    fields = ("x", "yobs", "weight", "ycalc", "ybkg", "ydiff")
    for case, projects in PROJECTS.items():
        extracted = {model: extract(path) for model, path in projects.items()}
        comparison = {
            field: compare_arrays(extracted["deepseek"]["arrays"][index], extracted["gpt56"]["arrays"][index])
            for index, field in enumerate(fields)
        }
        for project in extracted.values():
            del project["arrays"]
        output["cases"][case] = {"projects": extracted, "comparison": comparison}
    out_path = Path(__file__).with_name("common_cases_cross_model_gpx.json")
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()
