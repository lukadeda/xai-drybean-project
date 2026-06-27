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
- Do not assume XAI results exist beyond the partial notebook and empty report chapter.
- Use `human-voice-writer` when drafting or revising prose for the report.
- Ground methodological decisions and interpretations in checked sources with references.
- For final submission checks, verify the report and notebook together, especially metric consistency.
- `notebooks/02_model_training.ipynb` has been cleaned and executed successfully. Treat it as ready for the next XAI phase unless source data or model choices change.

## Main Risks

- The report currently states SHAP and LIME will be used, but `03_xai_explanations.ipynb` only has implemented Permutation Importance and commented SHAP starter code.
- `04_results_summary.ipynb`, `XAI-Methoden.tex`, `Evaluation-und-Vergleich.tex`, `Diskussion.tex`, `Ausblick.tex`, and `Abstract.tex` are mostly empty or placeholders.
- There is a feature-selection wording mismatch in `01_eda_feature_selection.ipynb`: markdown mentions `ShapeFactor3`, but executed code and the main Methodik chapter use `ShapeFactor4` and exclude `ShapeFactor3` due to high correlation with `Compactness`.
- The previous `notebooks/modelvergleich.tex` inconsistency has been resolved for the current run, but it should be regenerated whenever model parameters change.

## Recommended Continuation

1. Check whether a newer `XAI_Projektarbeit*` Overleaf export exists before report work.
2. Read `_context-helper/NEXT_STEPS.md`; it contains the detailed phase plan.
3. Start with `notebooks/03_xai_explanations.ipynb` and align it with `notebooks/02_model_training.ipynb`.
4. Implement at least two XAI methods, recommended minimum: Permutation Importance plus SHAP.
5. Produce at least one global and one local explanation.
6. Export XAI figures into the current report export under `XAI_Projektarbeit 19.54.42/Graphics/` or a newer confirmed export.
7. Fill `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex` only after XAI outputs are stable.
8. Use `EVIDENCE_INDEX.md` and checked source files for all source-backed claims.

## Copy-Paste Prompt For Next Chat

Continue from this handoff. First read `_context-helper/START_HERE.md`, `_context-helper/NEXT_STEPS.md`, `_context-helper/CONTEXT_STATE.json`, and `_context-helper/EVIDENCE_INDEX.md`. Treat `XAI_Projektarbeit 19.54.42/` as the current report export unless a newer `XAI_Projektarbeit*` folder exists and the user confirms it. Use `human-voice-writer` for report prose. Ground all methodological justifications in checked sources with locators. Task: complete the XAI notebook and then fill the XAI report chapter so the report and notebook satisfy `Projektarbeit_Anforderungen.md`.
