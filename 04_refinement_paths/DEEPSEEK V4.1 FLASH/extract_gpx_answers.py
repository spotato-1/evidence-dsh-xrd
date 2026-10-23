# -*- coding: utf-8 -*-
"""Read-only extraction of comparison fields from selected GSAS-II projects."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


GSAS_ROOT = Path(r"D:\AI\codex\workspace\DSH\dsh-portable\gsas")
EVIDENCE_ROOT = Path(r"D:\AI\codex\workspace\DEEPSEEK V4.1 FLASH\dsh-xrd-test-evidence")
sys.path.insert(0, str(GSAS_ROOT))
sys.path.insert(0, str(GSAS_ROOT / "GSASII"))

from GSASII import GSASIIscriptable as G2sc  # noqa: E402


PROJECTS = [
    Path(r"D:\AI\codex\workspace\测试\测试集\LayeredOxide_2ph\answer\20251121.gpx"),
    Path(r"D:\AI\codex\workspace\测试\测试集\LiFePO4\answer\精修完成版.bak17.bak0.bak0.gpx"),
    Path(r"D:\AI\codex\workspace\测试\测试集\LayeredOxide\raw\手动精修结构\20260813 SG+BM.gpx"),
    EVIDENCE_ROOT / r"runs\session-2c4aff20-e5cf-458d-920f-f19ab4d4277f\artifacts\CeO2\CeO2_final\CeO2_final.gpx",
    EVIDENCE_ROOT / r"runs\session-588a939a-a652-444f-9fd7-b5e427b2d84f\artifacts\Fe2O3_Fe3O4_2ph\Fe2O3_Fe3O4_2ph_final\Fe2O3_Fe3O4_2ph_final.gpx",
    EVIDENCE_ROOT / r"runs\session-92f1897c-c6c8-4c4d-b45f-37dcd4ea2d63\artifacts\Fluoroapatite\FAP_final\FAP_final.gpx",
    EVIDENCE_ROOT / r"runs\session-d37ffd1b-04a6-460e-8f04-733091bb8cf4\artifacts\LayeredOxide\LO_final\LO_final.gpx",
    EVIDENCE_ROOT / r"runs\session-ae4d57b2-f73e-40d2-ad3d-91e64c9602e0\artifacts\LiFePO4\LiFePO4_final\LiFePO4_final.gpx",
    EVIDENCE_ROOT / r"runs\session-a94a7058-4f31-488d-bfd1-dac63c3ef338\artifacts\PbSO4\PbSO4_final\PbSO4_final.gpx",
    EVIDENCE_ROOT / r"runs\session-82c8a1fe-ea71-462a-8f49-87004ac99588\artifacts\Y2O3\xrd_workflow\Y2O3_final\Y2O3_final.gpx",
    EVIDENCE_ROOT / r"runs\session-79f76a24-3904-4839-9908-6f8c38360173\artifacts\ZnO\ZnO_final\ZnO_final.gpx",
]


def atom_record(atom):
    return {
        "label": atom.label,
        "element": atom.element,
        "coordinates": [float(x) for x in atom.coordinates],
        "occupancy": float(atom.occupancy),
        "multiplicity": int(atom.mult),
        "adp_type": atom.adp_flag,
        "adp": simple(atom.ADP),
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
        return [simple(x) for x in value]
    if isinstance(value, dict):
        return {str(k): simple(v) for k, v in value.items()}
    return repr(value)


def extract(path: Path):
    project = G2sc.G2Project(gpxfile=str(path))
    phases = []
    for phase in project.phases():
        general = phase.data.get("General", {})
        hap = {}
        for hist_name, values in phase.data.get("Histograms", {}).items():
            keep = {
                key: values.get(key)
                for key in ("Scale", "PhaseFraction", "Size", "Mustrain", "Pref.Ori.")
                if key in values
            }
            hap[hist_name] = simple(keep)
        phases.append(
            {
                "name": phase.name,
                "space_group": general.get("SGData", {}).get("SpGrp"),
                "cell": simple(phase.get_cell()),
                "composition_per_cell": simple(phase.composition),
                "density": float(phase.density),
                "atoms": [atom_record(atom) for atom in phase.atoms()],
                "histogram_parameters": hap,
            }
        )

    histograms = []
    for hist in project.histograms():
        metadata = hist.data.get("data", [{}])[0]
        residuals = {
            key: metadata.get(key)
            for key in ("Nobs", "R", "Rb", "wR", "wRb", "wRmin", "Durbin-Watson")
            if isinstance(metadata, dict) and key in metadata
        }
        try:
            mass_fractions = simple(hist.ComputeMassFracs())
        except Exception as exc:
            mass_fractions = {"error": f"{type(exc).__name__}: {exc}"}
        histograms.append(
            {
                "name": hist.name,
                "residuals": simple(residuals),
                "mass_fractions": mass_fractions,
                "metadata_keys": sorted(metadata) if isinstance(metadata, dict) else [],
            }
        )

    return {
        "path": str(path),
        "size": path.stat().st_size,
        "phases": phases,
        "histograms": histograms,
    }


def main():
    output = Path(__file__).with_name("gpx_answer_extract.json")
    payload = {
        "note": "Read-only extraction; source GPX files were not modified.",
        "projects": [extract(path) for path in PROJECTS],
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
