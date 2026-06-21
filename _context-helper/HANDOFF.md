# HANDOFF

## Current State

The workspace has been inspected and a root `_context-helper/` context has been created. Original files were not modified.

The project concerns a German report for a module on Explainable AI. Topic: multiclass classification of seven dry bean varieties using tabular morphological features from the UCI Dry Bean Dataset, plus explanation of model decisions with XAI methods.

User workflow: the report is edited in Overleaf and copied locally for checking. Always inspect the newest local `XAI_Projektarbeit*` export folder first. Current confirmed export: `XAI_Projektarbeit 19.54.42/`.

Context structure: keep this root `_context-helper/` as the overarching projectarbeit context. Keep `peer-review/_context-helper/` separate unless the task is specifically about peer review.

Writing preference: for report prose, use the `human-voice-writer` style rules. The user explicitly asked to always remember this.

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
- Do not assume XAI results exist beyond the partial notebook and empty report chapter.
- Use `human-voice-writer` when drafting or revising prose for the report.

## Main Risks

- The report currently states SHAP and LIME will be used, but `03_xai_explanations.ipynb` only has implemented Permutation Importance and commented SHAP starter code.
- `04_results_summary.ipynb`, `XAI-Methoden.tex`, `Evaluation-und-Vergleich.tex`, `Diskussion.tex`, `Ausblick.tex`, and `Abstract.tex` are mostly empty or placeholders.
- There is a feature-selection wording mismatch in `01_eda_feature_selection.ipynb`: markdown mentions `ShapeFactor3`, but executed code and the main Methodik chapter use `ShapeFactor4` and exclude `ShapeFactor3` due to high correlation with `Compactness`.
- `notebooks/modelvergleich.tex` contains older/different metrics than `XAI_Projektarbeit 19.54.42/Chapters/Ergebnisse-der-Klassifikation.tex` and `02_model_training.ipynb`.

## Recommended Continuation

1. Check whether a newer `XAI_Projektarbeit*` Overleaf export exists before report work.
2. Decide whether to finish the report text, complete XAI experiments, or reconcile inconsistencies first.
3. If writing report sections, use `EVIDENCE_INDEX.md` for source-backed claims.
4. If coding, start with `notebooks/03_xai_explanations.ipynb` and generate reusable XAI outputs for the report.
