# XAI Projektarbeit: Dry Bean Classification

Dieses Repository enthaelt die Projektarbeit fuer das Modul Erklaerbare Kuenstliche Intelligenz. Ziel ist die Multiclass-Klassifikation von Dry-Bean-Sorten und die Erklaerung der Modellentscheidungen mit XAI-Methoden.

## Forschungsfrage

Inwiefern lassen sich Dry-Bean-Sorten anhand weniger morphologischer Bildmerkmale zuverlaessig klassifizieren, und welche Merkmale erklaeren die Entscheidungen verschiedener Multiclass-Klassifikatoren am staerksten?

## Finale Modelle

- Logistic Regression als lineares Vergleichsmodell
- Random Forest als robustes Ensemble-Verfahren
- HistGradientBoostingClassifier als leistungsstaerkeres Boosting-Verfahren
- MLPClassifier als neuronales Netz

## Finale XAI-Methoden

- Permutation Importance
- SHAP
- LIME fuer lokale Erklaerungen einzelner Instanzen

PFI, SHAP und LIME werden im finalen XAI-Notebook auf alle vier Modelle angewandt und verglichen. Das Notebook exportiert Grafiken und CSV-Tabellen sowohl nach `notebooks/` als auch nach `XAI_Projektarbeit 19.54.42/Graphics/`.

## Projektstruktur

```text
data/
  raw/              Rohdaten, falls lokal gespeichert
  processed/        generierte Zwischendaten, nicht versioniert
notebooks/
  01_eda_feature_selection.ipynb
  02_model_training.ipynb
  03_xai_explanations.ipynb
  04_results_summary.ipynb
reports/
  figures/          Abbildungen fuer Bericht und Praesentation
  notes/            Notizen, Literatur, Zwischenstaende
src/
  utils.py          Wiederverwendbare Hilfsfunktionen
```

## Setup in VS Code

1. Virtuelle Umgebung erstellen:

```bash
python3 -m venv .venv
```

2. Umgebung aktivieren:

```bash
source .venv/bin/activate
```

3. Pakete installieren:

```bash
pip install -r requirements.txt
```

4. Jupyter-Kernel registrieren:

```bash
python -m ipykernel install --user --name xai-drybean --display-name "Python (xai-drybean)"
```

5. In VS Code ein Notebook oeffnen und den Kernel `Python (xai-drybean)` auswaehlen.

## Reproduzierbare Ausfuehrung

Die drei finalen Notebooks werden in dieser Reihenfolge ausgefuehrt:

```bash
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/01_eda_feature_selection.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/02_model_training.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/03_xai_explanations.ipynb
```

`01_eda_feature_selection.ipynb` dokumentiert die Auswahl der acht Merkmale. `02_model_training.ipynb` trainiert die vier finalen Modelle und erzeugt die Konfusionsmatrizen. `03_xai_explanations.ipynb` berechnet PFI, globale SHAP-Werte sowie lokale SHAP- und LIME-Erklärungen für alle vier Modelle.

## Git-Hinweise fuer Notebooks

- Vor jedem Commit Notebook-Outputs loeschen: `Clear All Outputs`.
- Nicht gleichzeitig dieselbe Notebook-Datei bearbeiten.
- Vor Arbeitsbeginn immer `git pull` ausfuehren, sobald ein Remote-Repository verbunden ist.
- Kleine Commits mit klaren Nachrichten verwenden.

## Datenquelle

Dry Bean Dataset, UCI Machine Learning Repository:  
https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

## Wichtige Literatur

- Koklu, M. & Ozkan, I. A. (2020). Multiclass classification of dry beans using computer vision and machine learning techniques. Computers and Electronics in Agriculture, 174, 105507.
- Krishnan, S. et al. (2023). Identification of Dry Bean Varieties Using CatBoost. Scientific Programming.
- Lundberg, S. M. & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. NeurIPS.
- Ribeiro, M. T., Singh, S. & Guestrin, C. (2016). Why Should I Trust You? KDD.
- Molnar, C. (2022). Interpretable Machine Learning.
