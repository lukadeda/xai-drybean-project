# XAI-Projektarbeit, Dry Bean Classification

Dieses Paket enthält den reproduzierbaren Code zur Klassifikation der sieben Dry-Bean-Sorten und zur XAI-Auswertung der vier finalen Modelle.

## Enthaltene Notebooks

- `01_eda_feature_selection.ipynb` untersucht Klassenverteilung und Merkmalskorrelationen. Daraus ergibt sich das finale Feature-Set.
- `02_model_training.ipynb` trainiert und bewertet Logistic Regression, Random Forest, HistGradientBoosting und MLP.
- `03_xai_explanations.ipynb` vergleicht PFI, SHAP und LIME für diese vier Modelle.

Die Notebooks laden den Dry-Bean-Datensatz direkt aus dem UCI Machine Learning Repository. Lokale Rohdaten werden nicht benötigt.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name xai-drybean --display-name "Python (xai-drybean)"
```

## Ausführung

Die Notebooks werden in dieser Reihenfolge ausgeführt:

```bash
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/01_eda_feature_selection.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/02_model_training.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/03_xai_explanations.ipynb
```

Alternativ können die Notebooks in VS Code mit dem Kernel `Python (xai-drybean)` geöffnet werden.

## Datenquelle

Dry Bean Dataset, UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/602/dry+bean+dataset
