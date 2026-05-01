# XAI Projektarbeit: Dry Bean Classification

Dieses Repository enthaelt die Projektarbeit fuer das Modul Erklaerbare Kuenstliche Intelligenz. Ziel ist die Multiclass-Klassifikation von Dry-Bean-Sorten und die Erklaerung der Modellentscheidungen mit XAI-Methoden.

## Ziel bis 05.05.2026

- Forschungsfrage formulieren
- Literaturrecherche zur Domaene beginnen
- Erste Versuche zur Feature-Auswahl durchfuehren
- Mindestens drei KI-Modelle fuer die Klassifikation vorauswaehlen

## Forschungsfrage

Inwiefern lassen sich Dry-Bean-Sorten anhand weniger morphologischer Bildmerkmale zuverlaessig klassifizieren, und welche Merkmale erklaeren die Entscheidungen verschiedener Multiclass-Klassifikatoren am staerksten?

## Geplante Modelle

- LogisticRegression als Baseline und gut interpretierbares lineares Vergleichsmodell
- RandomForestClassifier als robustes Ensemble-Verfahren mit Feature Importances
- HistGradientBoostingClassifier als modernes, leistungsstaerkeres Boosting-Verfahren

## Erste Feature-Auswahl

Als erster Arbeitsstand wird folgendes 8-Feature-Set verwendet:

```text
Area
Perimeter
AspectRation
Compactness
roundness
ShapeFactor1
ShapeFactor2
ShapeFactor4
```

Die Begruendung und erste Modellversuche sind dokumentiert in `reports/notes/feature_selection_first_trials.md`.

## Geplante XAI-Methoden

- Permutation Importance
- SHAP
- Optional: LIME fuer lokale Erklaerungen einzelner Instanzen

## Projektstruktur

```text
DryBeanDataset/     Lokaler Dry-Bean-Datensatz
data/
  raw/              optionale Rohdaten
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

## Git-Hinweise fuer Notebooks

- Vor jedem Commit Notebook-Outputs loeschen: `Clear All Outputs`.
- Nicht gleichzeitig dieselbe Notebook-Datei bearbeiten.
- Vor Arbeitsbeginn immer `git pull` ausfuehren, sobald ein Remote-Repository verbunden ist.
- Kleine Commits mit klaren Nachrichten verwenden.

## Datenquelle und lokaler Pfad

Dry Bean Dataset, UCI Machine Learning Repository:  
https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

Die Notebooks laden den lokalen Excel-Datensatz aus:

```text
DryBeanDataset/Dry_Bean_Dataset.xlsx
```

## Wichtige Literatur

- Koklu, M. & Ozkan, I. A. (2020). Multiclass classification of dry beans using computer vision and machine learning techniques. Computers and Electronics in Agriculture, 174, 105507.
- Krishnan, S. et al. (2023). Identification of Dry Bean Varieties Using CatBoost. Scientific Programming.
- Lundberg, S. M. & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. NeurIPS.
- Ribeiro, M. T., Singh, S. & Guestrin, C. (2016). Why Should I Trust You? KDD.
- Molnar, C. (2022). Interpretable Machine Learning.
