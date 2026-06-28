# CONTEXT PACK

## Project Snapshot

The repository is for an XAI project report: `XAI Projektarbeit: Dry Bean Classification`. The central research problem is whether seven dry bean varieties can be reliably classified from a reduced, interpretable set of morphological image-derived tabular features, and how model decisions can be explained with XAI methods.

## Research Question

Central question from `XAI_Projektarbeit 19.54.42/Chapters/Einleitung.tex`:

> Wie zuverlässig lassen sich die sieben Dry-Bean-Sorten mit Machine-Learning-Modellen auf Basis ausgewählter morphologischer Bildmerkmale klassifizieren, und wie können die Modellentscheidungen mit XAI-Methoden erklärt werden?

Subquestions:

- RQ1: Which ML models classify the seven bean varieties reliably?
- RQ2: Which feature combination is especially suitable?
- RQ3: To what extent can the models be explained with XAI methods, and do the explanations fit domain knowledge?

## Data

- Dataset: UCI Dry Bean Dataset.
- Observations: 13,611.
- Inputs: 16 numerical morphological features.
- Target: `Class` with seven varieties: `SEKER`, `BARBUNYA`, `BOMBAY`, `CALI`, `DERMASON`, `HOROZ`, `SIRA`.
- No missing values were found in the project EDA.
- Class imbalance exists: `DERMASON` is largest with 3,546 samples; `BOMBAY` is smallest with 522 samples.

## Feature Selection

Final feature set in the report and training notebook:

- `Area`
- `AspectRatio`
- `Eccentricity`
- `Compactness`
- `Roundness`
- `ShapeFactor1`
- `ShapeFactor2`
- `ShapeFactor4`

Rationale: cover size, length/width relation, elongation, compactness, roundness, and shape descriptors while avoiding highly redundant features such as `ConvexArea`, `EquivDiameter`, `Perimeter`, axis lengths, and `ShapeFactor3`.

## Strong EDA Facts

- `Area` and `ConvexArea`: correlation `r=0.999939`.
- `Compactness` and `ShapeFactor3`: correlation `r=0.998686`.
- `Perimeter` and `EquivDiameter`: correlation `r=0.991380`.
- `AspectRatio` and `Compactness`: correlation about `r=0.987687`.

## Models

The main model families are:

- Logistic Regression as linear baseline.
- Random Forest as robust ensemble.
- HistGradientBoostingClassifier as boosting model.
- MLPClassifier as simple neural network.

Setup described in `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex`:

- Python/Jupyter workflow.
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`; repository also includes `shap`, `lime`, `joblib`, `ucimlrepo`.
- Test split: 20%.
- Stratification by `Class`.
- Random state: 42.
- Training samples: 10,888; test samples: 2,723.
- Scaling for Logistic Regression and MLP; no scaling for tree-based models.

## Main Results

Current main result table in `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex` and `02_model_training.ipynb`:

- MLP Neural Network: Accuracy `0.923`, Macro-F1 `0.934`.
- HistGradientBoosting: Accuracy `0.920`, Macro-F1 `0.932`.
- Logistic Regression: Accuracy `0.917`, Macro-F1 `0.931`.
- Random Forest: Accuracy `0.918`, Macro-F1 `0.931`.

Interpretation: all models are close; MLP is only narrowly best in this test run, not clearly superior.

## XAI Status

Implemented in `notebooks/03_xai_explanations.ipynb`:

- Permutation Feature Importance for the final Random Forest model, scored with Macro-F1.
- Global SHAP feature importance for the same Random Forest model.
- Local SHAP explanation for one correctly classified test instance.
- Local LIME explanation for the same test instance.

Generated figures exist in both `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`:

- `Permutation_Importance_RandomForest.pdf`
- `SHAP_Global_RandomForest.pdf`
- `SHAP_Local_RandomForest.pdf`
- `LIME_Local_RandomForest.pdf`

Key XAI result pattern: Permutation Importance ranks `ShapeFactor1`, `Roundness`, and `Area` highest. Global SHAP ranks `ShapeFactor1`, `Area`, `ShapeFactor2`, and `Compactness` highest. The local SHAP/LIME example is a correctly classified `DERMASON` instance and is mainly driven by size and shape-factor conditions.

`XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex` has now been written from these outputs. It references all four XAI figures and explains why Random Forest is used for XAI although MLP is narrowly best by Macro-F1.

Source check: Molnar's chapters on LIME, SHAP, and Permutation Feature Importance align with the implemented structure. Important caveats for report writing are correlated features, PFI's loss-based/ranking-only interpretation, SHAP's dependence assumptions, and LIME's neighborhood/fidelity/stability limitations. The `Gastvorlesung/` XAI material is image-based Captum Grad-CAM and should be mentioned only as a contrast if needed.

## Report Status

Current active report folder: `XAI_Projektarbeit 19.54.42/`. This is the user-confirmed latest local Overleaf export. Future work should first check whether a newer `XAI_Projektarbeit*` export exists.

Mostly drafted:

- Introduction.
- Fundamentals and related work.
- Dataset and EDA.
- Methodology and implementation.
- Classification results.

Mostly missing:

- Abstract.
- Evaluation/discussion.
- Discussion chapter.
- Conclusion/outlook.
