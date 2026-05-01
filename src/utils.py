"""Utility functions for the Dry Bean XAI project."""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"


def ensure_directories() -> None:
    """Create generated-data and report directories if they do not exist."""
    for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, FIGURES_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
