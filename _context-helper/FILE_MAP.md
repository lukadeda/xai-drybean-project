# FILE MAP

## Root

- `README.md`: project overview, research question, planned models, planned XAI methods, setup, data source, start literature.
- `requirements.txt`: Python dependencies for notebooks and XAI work.
- `BookAdvanced.md` / `BookAdvanced.pdf`: converted/full text of Hastie, Tibshirani, Friedman, likely reference background for model explanations.
- `Projektarbeit_Anforderungen.pdf`: assignment requirements; not deeply converted in this pass.

## Data And Code

- `data/README.md`: states dataset is loaded via `ucimlrepo`; raw local data would belong in `data/raw/`.
- `DryBeanDataset/`: contains a temporary Excel lock file only in inspected listing; no usable dataset file found there.
- `src/utils.py`: path constants and directory creation helper.

## Notebooks

- `notebooks/01_eda_feature_selection.ipynb`: EDA, class distribution, correlation matrix, feature-selection reasoning.
- `notebooks/02_model_training.ipynb`: model training and comparison; current main metrics match the report chapter.
- `notebooks/02_model_training_mit_ausreisserbehandlung.ipynb`: variant with IQR outlier handling; not the final setup described in the report.
- `notebooks/03_xai_explanations.ipynb`: executed XAI notebook with Permutation Importance, global SHAP, local SHAP, and local LIME for the final Random Forest model.
- `notebooks/04_results_summary.ipynb`: placeholder result summary.
- `notebooks/modelvergleich.tex`: older/different model table; use cautiously.

## Main Report

- `XAI_Projektarbeit 19.54.42/`: current user-confirmed Overleaf export; authoritative until a newer export appears.
- `XAI_Projektarbeit 19.54.42/htwsaar-i-mst-vorlage.tex`: main LaTeX driver; includes report chapters.
- `XAI_Projektarbeit 19.54.42/htwsaar-i-mst-config.tex`: title/config/author metadata and packages.
- `XAI_Projektarbeit 19.54.42/Chapters/Einleitung.tex`: motivation, problem, research questions, structure.
- `XAI_Projektarbeit 19.54.42/Chapters/Grundlagen.tex`: domain, feature, model, XAI, and related-work foundations.
- `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex`: dataset, class distribution, data quality, correlations, outliers, modeling implications.
- `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex`: setup, preprocessing, feature selection, split, scaling, models, evaluation design.
- `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex`: model metric comparison and confusion-matrix framing.
- `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex`: empty skeleton for XAI evaluation.
- `XAI_Projektarbeit 19.54.42/Chapters/Evaluation-und-Vergleich.tex`: empty skeleton.
- `XAI_Projektarbeit 19.54.42/Chapters/Diskussion.tex`: commented placeholders only.
- `XAI_Projektarbeit 19.54.42/Chapters/Ausblick.tex`: empty conclusion/outlook skeleton.
- `XAI_Projektarbeit 19.54.42/FrontBackmatter/Abstract.tex`: empty abstract skeleton.
- `XAI_Projektarbeit 19.54.42/Bibliography.bib`: current bibliography.

## Older Or Secondary Material

- `Gastvorlesung/`: separate guest-lecture material with PyTorch/torchvision image inference notebooks for classification, object detection, segmentation, and Captum Grad-CAM. It is structurally different from the Dry Bean tabular scikit-learn workflow and should not be treated as a template for the report's SHAP/LIME/PFI implementation without adaptation.
- `XAI_Projektarbeit_neu/`: deleted old local draft after user approval.
- `XAI_Projektarbeit 19.54.42/paper/drybean_dataset/`: supporting literature PDFs; skimmed only.
- `peer-review/`: separate peer-review materials and its own `_context-helper/`; not merged into this root context.
