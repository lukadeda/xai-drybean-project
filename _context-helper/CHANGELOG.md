# CHANGELOG

## 2026-06-21

- Created root `_context-helper/` workspace.
- Inventoried main project materials with focus outside low-priority lab/paper-presentation areas.
- Initially identified `XAI_Projektarbeit_neu/` as likely current main report state.
- Indexed core claims, results, gaps, and inconsistencies.
- Documented next steps for completing XAI and final report sections.
- Refined the report-folder assessment after user challenge: `XAI_Projektarbeit_neu/` appears newer by timestamps, but `XAI_Projektarbeit/` remains a relevant older/parallel draft and should be confirmed before treating it as obsolete.
- Added user workflow note: report work happens in Overleaf and local `XAI_Projektarbeit*` folders are exports for checking.
- Clarified context structure: root `_context-helper/` is sufficient as overarching projectarbeit context; `peer-review/_context-helper/` remains a separate workstream context.
- Deleted old local draft folder `XAI_Projektarbeit_neu/` after user approval.
- Updated `notebooks/02_model_training.ipynb` so classification reports and confusion matrices are generated for all four models, not only the best/last prediction. The confusion-matrix export now targets the current Overleaf export `XAI_Projektarbeit 19.54.42/Graphics/`.
- Added writing preference: use `human-voice-writer` style rules for report prose.
- Expanded `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex` with a data-based interpretation of the four confusion matrices.
- Clarified submission scope: both report and Jupyter notebook matter; notebook outputs must match report values.
- Converted `Projektarbeit_Anforderungen.pdf` to Markdown and checked the current report/notebook state against the stated requirements.
- Added evidence rule: report arguments and methodological justifications must be source-backed with verifiable references/locators.
- Replaced the short next-step list with a detailed phased plan for completing XAI, report sections, notebook/report consistency checks, and future-chat handoff.
- Cleaned `notebooks/02_model_training.ipynb` into a linear submission-oriented workflow with fixed final model parameters and fresh execution outputs.
- Re-ran the cleaned training notebook successfully. Fresh rounded metrics: MLP `0.923/0.934`, HistGradientBoosting `0.920/0.932`, Random Forest `0.918/0.931`, Logistic Regression `0.917/0.931`.
- Synchronized `Ergebnisse-der-Klassifikation.tex` and `Architektur-Implementierung.tex` with the newly executed notebook outputs.
- Kept the training notebook on `ucimlrepo` loading, but added explicit dataset sanity checks for shape, classes, and missing values. A local CSV cache was considered and then removed at the user's request.
- Checked all notebooks for `ucimlrepo` use. Added `certifi` SSL setup and dataset sanity checks to EDA, training-with-outliers, and XAI notebooks. Aligned old feature-name references in XAI and results-summary notebooks with the final feature set.
- Implemented and executed `notebooks/03_xai_explanations.ipynb`: final Random Forest parameters, direct UCI CSV loading with certifi SSL context, Permutation Importance, global SHAP, local SHAP, and PDF exports to both `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`.
- Added LIME to `notebooks/03_xai_explanations.ipynb` as a local explanation for the same test instance used by local SHAP. Exported `LIME_Local_RandomForest.pdf` to both output folders.
- Refreshed root `_context-helper/` after XAI implementation: updated `START_HERE.md`, `CONTEXT_PACK.md`, `NEXT_STEPS.md`, `OPEN_QUESTIONS.md`, `QUALITY_GATE.md`, `COVERAGE.md`, `IMPORTANT_FILES.md`, `CONTEXT_STATE.json`, and `EVIDENCE_INDEX.md` to remove stale claims about incomplete SHAP/LIME work.
- Cleaned remaining stale statements in `HANDOFF.md` and `FILE_MAP.md` that still described the XAI notebook as partial.
- Added `_context-helper/briefs/zwischenstand-praesentation.md` as a separate brief for a new chat focused on the intermediate presentation.
- Statically inspected `Gastvorlesung/` notebooks without execution. Noted that they use PyTorch/torchvision image inference and Captum Grad-CAM, not the project's tabular scikit-learn SHAP/LIME/PFI workflow.
- Checked implemented XAI methods against Molnar chapters 14, 18, and 23 plus `Gastvorlesung/Übung.pdf`. Confirmed method structure is aligned, with caveats to mention in the report.
- Wrote `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex` from the executed XAI notebook outputs. The chapter now explains Random Forest model choice, PFI, global SHAP, local SHAP, local LIME, method comparison, and caveats from Molnar. Local `latexmk -pdf` build succeeds.
