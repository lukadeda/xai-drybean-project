# HANDOFF

## Current State

The workspace has been inspected and a root `_context-helper/` context has been created. Original files were not modified.

The project concerns a German report for a module on Explainable AI. Topic: multiclass classification of seven dry bean varieties using tabular morphological features from the UCI Dry Bean Dataset, plus explanation of model decisions with XAI methods.

User workflow: the report is edited in Overleaf and copied locally for checking. Always inspect the newest local `XAI_Projektarbeit*` export folder first. Current confirmed export: `XAI_Projektarbeit 19.54.42/`.

Context structure: keep this root `_context-helper/` as the overarching projectarbeit context. Keep `peer-review/_context-helper/` separate unless the task is specifically about peer review.

Writing preference: for report prose, use the `human-voice-writer` style rules. The user explicitly asked to always remember this.

Evidence rule: when giving report justifications, rely on checked sources and include references/locators. The user explicitly asked that claims be traceable and verifiable.

Submission scope: report and Jupyter notebook both matter. The notebook has to run, and its reported metrics/figures must match the report.

## Main Sources Read

- `README.md`
- `data/README.md`
- `reports/notes/domain_research.md`
- `src/utils.py`
- `requirements.txt`
- `notebooks/01_eda_feature_selection.ipynb` via targeted inspection
- `notebooks/02_model_training.ipynb` via targeted inspection
- `notebooks/03_xai_explanations.ipynb` via targeted inspection
- `notebooks/04_results_summary.ipynb` via targeted inspection
- `notebooks/modelvergleich.tex`
- `XAI_Projektarbeit 19.54.42/Chapters/*.tex` for the current Overleaf-exported written chapters
- `XAI_Projektarbeit 19.54.42/Bibliography.bib`
- `XAI_Projektarbeit 19.54.42/paper/drybean_dataset/` skimmed as supporting literature material

## Important Decisions

- Treat the newest local Overleaf export as authoritative for report checks; currently `XAI_Projektarbeit 19.54.42/`.
- Treat the generated `peer-review/_context-helper/` as separate previous context, not source truth for this root context.
- Treat paper folders as supporting literature, not the main focus, per user instruction.
- XAI notebook results now exist; do not assume the written report chapter has been updated yet.
- Use `human-voice-writer` when drafting or revising prose for the report.
- Ground methodological decisions and interpretations in checked sources with references.
- For final submission checks, verify the report and notebook together, especially metric consistency.
- `notebooks/02_model_training.ipynb` has been cleaned and executed successfully. Treat it as ready for the next XAI phase unless source data or model choices change.
- The training notebook loads the Dry Bean dataset via `ucimlrepo` and checks the expected shape, classes, and missing values. A local CSV cache was considered but removed at the user's request.
- All notebooks that use `ucimlrepo` now include the same `certifi` SSL setup and dataset sanity checks. The XAI notebook now uses the final feature names `AspectRatio` and `ShapeFactor4`.
- `notebooks/03_xai_explanations.ipynb` now runs end-to-end. It explains the final Random Forest model with Permutation Importance, global SHAP, and one local SHAP example. Generated files: `Permutation_Importance_RandomForest.pdf`, `SHAP_Global_RandomForest.pdf`, `SHAP_Local_RandomForest.pdf` in both `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`.
- LIME is also implemented in `03_xai_explanations.ipynb` for the same local example. Generated file: `LIME_Local_RandomForest.pdf` in both `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`.

## Main Risks

- The XAI notebook implements SHAP, LIME, and Permutation Importance, but `XAI-Methoden.tex` has not yet been filled from those outputs.
- `04_results_summary.ipynb`, `XAI-Methoden.tex`, `Evaluation-und-Vergleich.tex`, `Diskussion.tex`, `Ausblick.tex`, and `Abstract.tex` are mostly empty or placeholders.
- When writing XAI, justify why Random Forest is the explained model although MLP is narrowly best by Macro-F1.
- The previous `notebooks/modelvergleich.tex` inconsistency has been resolved for the current run, but it should be regenerated whenever model parameters change.

## Recommended Continuation

1. Check whether a newer `XAI_Projektarbeit*` Overleaf export exists before report work.
2. Read `_context-helper/NEXT_STEPS.md`; it contains the detailed phase plan.
3. Use the already executed `notebooks/03_xai_explanations.ipynb` outputs for the XAI chapter.
4. Reference the exported figures: `Permutation_Importance_RandomForest.pdf`, `SHAP_Global_RandomForest.pdf`, `SHAP_Local_RandomForest.pdf`, and `LIME_Local_RandomForest.pdf`.
5. Fill `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex` with actual results and source-backed method limitations.
6. Then complete `Evaluation-und-Vergleich.tex`, `Diskussion.tex`, `Ausblick.tex`, and `Abstract.tex`.
7. Use `EVIDENCE_INDEX.md` and checked source files for all source-backed claims.

## Copy-Paste Prompt For Next Chat

Continue from this handoff. First read `_context-helper/START_HERE.md`, `_context-helper/NEXT_STEPS.md`, `_context-helper/CONTEXT_STATE.json`, and `_context-helper/EVIDENCE_INDEX.md`. Treat `XAI_Projektarbeit 19.54.42/` as the current report export unless a newer `XAI_Projektarbeit*` folder exists and the user confirms it. Use `human-voice-writer` for report prose. Ground all methodological justifications in checked sources with locators. Task: write the XAI report chapter from the executed notebook outputs, then complete evaluation/discussion/conclusion/abstract and run final consistency checks.
