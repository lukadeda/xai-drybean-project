# EVIDENCE INDEX

| Claim | Source | Locator | Confidence | Notes |
|---|---|---:|---|---|
| Project goal is Dry Bean multiclass classification with XAI explanations. | `README.md` | lines 1-4 | high | Root overview. |
| Central research question asks reliability of classifying seven bean varieties from selected morphological features and explanation with XAI. | `XAI_Projektarbeit 19.54.42/Chapters/Einleitung.tex` | lines 21-35 | high | Current Overleaf export; includes RQ1-RQ3 and model/XAI list. |
| Dataset has 13,611 observations, 16 numeric input features, target `Class`, and seven varieties. | `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex` | lines 6-10 | high | Current Overleaf export. |
| Largest class is `DERMASON` with 3,546, smallest is `BOMBAY` with 522. | `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex` | lines 12-34 | high | Table included. |
| No missing values were found in the project analysis. | `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex` | lines 8-10 | high | Also supported by notebook inspection. |
| Strong correlations motivate feature reduction. | `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex` | lines 47-54, 70-78 | high | Exact correlations listed. |
| `Area` and `ConvexArea` correlation is `0.999939`. | `notebooks/01_eda_feature_selection.ipynb` | lines 499-500 | high | Also rounded in report text. |
| `Compactness` and `ShapeFactor3` correlation is `0.998686`. | `notebooks/01_eda_feature_selection.ipynb` | lines 499-501 | high | Key reason to exclude `ShapeFactor3`. |
| Final selected features are `Area`, `AspectRatio`, `Eccentricity`, `Compactness`, `Roundness`, `ShapeFactor1`, `ShapeFactor2`, `ShapeFactor4`. | `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex`; `notebooks/02_model_training.ipynb` | report lines 19-38; notebook lines 48-58 | high | Consistent with training notebook. |
| EDA markdown mentions `ShapeFactor3`, but code selects `ShapeFactor4`. | `notebooks/01_eda_feature_selection.ipynb` | lines 543-554 and 681-690 | high | Important inconsistency. |
| Final setup did not automatically remove outliers. | `XAI_Projektarbeit 19.54.42/Chapters/Datensatz.tex`; `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex` | lines 62-68; lines 12-17 | high | Alternative outlier notebook exists but is not final report setup. |
| Train-test split uses 20% test, stratification by `Class`, random state 42. | `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex` | lines 40-50 | high | Also states train/test sizes. |
| Logistic Regression and MLP use scaling; tree methods do not. | `XAI_Projektarbeit 19.54.42/Chapters/Architektur-Implementierung.tex` | lines 40-52 | high | Method detail. |
| Main model results: MLP `0.923` accuracy / `0.934` Macro-F1, HGB `0.920` / `0.932`, LR `0.917` / `0.931`, RF `0.917` / `0.929`. | `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex`; `notebooks/02_model_training.ipynb` | report lines 5-22; notebook grep lines 383-387 | high | Current authoritative table. |
| MLP is only narrowly best, not clearly superior. | `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex` | lines 5-7 and 24-42 | high | Report explicitly states small differences. |
| `03_xai_explanations.ipynb` currently implements Permutation Importance and has SHAP only as planned/commented code. | `notebooks/03_xai_explanations.ipynb` | grep lines 67-128 | high | LIME not found as implementation. |
| `XAI-Methoden.tex` is empty skeleton. | `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex` | lines 1-24 | high | Major report gap in current export. |
| Abstract, evaluation/discussion, discussion, and conclusion/outlook are mostly empty. | `XAI_Projektarbeit 19.54.42/FrontBackmatter/Abstract.tex`; `Chapters/Evaluation-und-Vergleich.tex`; `Chapters/Diskussion.tex`; `Chapters/Ausblick.tex` | inspected files | high | Major finalization gap in current export. |
| User edits in Overleaf and copies the latest version locally for checking. | User message | 2026-06-21 | high | Future report checks should inspect newest `XAI_Projektarbeit*` export first. |
| Current confirmed local Overleaf export is `XAI_Projektarbeit 19.54.42/`. | User message plus local timestamps | `stat`: 2026-06-21 17:53 for central files | high | Supersedes earlier assumption that `XAI_Projektarbeit_neu/` was current. |
| `XAI_Projektarbeit_neu/` appeared newer than an earlier `XAI_Projektarbeit/` copy by local modification time. | Historical `stat` on paired files | `Einleitung.tex`: 2026-06-17 vs 2026-06-16; `XAI-Methoden.tex`: 2026-06-17 vs 2026-06-16; compiled PDF: 2026-06-17 vs 2026-06-16 | historical | No longer authoritative after new Overleaf export. |
