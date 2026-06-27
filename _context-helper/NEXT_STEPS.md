# NEXT STEPS

## Current Goal

Bring the project to a submission-ready state. Submission requires both the written report and a working Jupyter notebook. The notebook outputs must match the report values and figures.

Current confirmed report export: `XAI_Projektarbeit 19.54.42/`.

Before any report work, check whether the user imported a newer `XAI_Projektarbeit*` Overleaf export. If yes, treat the newest confirmed export as authoritative.

## Rules For All Future Work

- Use `human-voice-writer` for all report prose.
- Ground methodological justifications in checked sources. Include concrete citations and locators where possible.
- Keep report and notebook synchronized. Do not change reported values without changing the notebook or explaining the source of the values.
- Do not reintroduce `XAI_Projektarbeit_neu/`; it was deleted as an old draft.
- Keep `peer-review/_context-helper/` separate unless the task is explicitly about peer review.

## Phase 1: Fix And Complete XAI Notebook

Priority: highest.

File: `notebooks/03_xai_explanations.ipynb`.

Tasks:

1. Align data setup with `notebooks/02_model_training.ipynb`.
2. Use the same selected features: `Area`, `AspectRatio`, `Eccentricity`, `Compactness`, `Roundness`, `ShapeFactor1`, `ShapeFactor2`, `ShapeFactor4`.
3. Remove old feature names from XAI work: `AspectRation` and `ShapeFactor3` are not the final setup.
4. Use the same split: `test_size=0.2`, `stratify=y`, `random_state=42`.
5. Train or load the model used for XAI with fixed parameters, not a long GridSearch.
6. Recommended detailed XAI model: Random Forest or HistGradientBoosting. Prefer the one that gives stable SHAP support in the local environment.
7. Keep MLP in the model comparison. Optionally compute Permutation Importance for MLP, but do not make it the first SHAP target unless runtime is acceptable.

Acceptance criteria:

- Notebook runs top to bottom in the project environment.
- XAI notebook uses the same feature set and split as the training notebook.
- At least two XAI methods are implemented.
- At least one global and one local explanation are produced.
- Figures are exported to the current report export under `XAI_Projektarbeit 19.54.42/Graphics/` or a newer confirmed export.

## Phase 2: Implement Minimum XAI Methods

Recommended minimum: Permutation Importance plus SHAP.

Permutation Importance:

- Use `sklearn.inspection.permutation_importance`.
- Score with `f1_macro` to match the report focus on Macro-F1.
- Export a PDF figure, for example `Graphics/Permutation_Importance.pdf`.
- Save a table or print output with feature rankings.

SHAP:

- Use a source-backed justification for the chosen explainer.
- If using a tree model, check SHAP documentation and Molnar before writing that TreeSHAP is efficient for tree models.
- Produce a global SHAP plot or feature ranking.
- Produce local explanations for selected instances.
- Export figures with stable filenames, for example `Graphics/SHAP_Global.pdf` and `Graphics/SHAP_Local_SIRA_DERMASON.pdf`.

Local cases to select:

- One correctly classified `BOMBAY` instance, because confusion matrices show it is easy to separate.
- One `SIRA`/`DERMASON` confusion, because this is the dominant error pattern.
- One `BARBUNYA`/`CALI` confusion if time permits.

Acceptance criteria:

- The XAI outputs can be explained in the report without guessing.
- Each methodological choice has a source-backed explanation.
- Local examples are tied to actual predictions and confusion-matrix patterns.

## Phase 3: Source Check For XAI Justification

Before writing XAI report text, inspect and cite sources.

Likely sources already in bibliography:

- Molnar, `molnar2025interpretable`, especially SHAP, LIME, and Permutation Feature Importance chapters.
- Lundberg and Lee, `lundberg2017shap`, for SHAP foundations.
- Ribeiro et al., `ribeiro2016why`, if LIME is used or discussed.
- scikit-learn documentation for `permutation_importance` or metric definitions if needed.

Tasks:

1. Verify exact claims about SHAP explainers before writing them.
2. Verify exact claims about PFI and correlated features before writing them.
3. If LIME is skipped, adjust the report promise in `Einleitung.tex` and `Grundlagen.tex`, or explicitly say why LIME was not used in the final evaluation. This decision must fit the requirements, which ask for at least two XAI methods.

Acceptance criteria:

- No methodological justification appears in the report without a citation.
- Claims about runtime, model compatibility, or interpretation limits are backed by checked sources.

## Phase 4: Fill XAI Report Chapter

File: `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex`.

Suggested structure:

1. Ziel der XAI-Auswertung.
2. Begründung der Modellwahl für die XAI-Auswertung.
3. Globale Erklärungen mit Permutation Feature Importance.
4. Globale SHAP-Auswertung.
5. Lokale SHAP-Erklärungen.
6. Vergleich der XAI-Methoden.
7. Zwischenfazit mit Domänenwissen.

Writing rules:

- Use natural German prose.
- Do not overstate. Say what the figures show.
- Distinguish data-backed findings from interpretation.
- Tie XAI findings back to morphology: size, roundness, elongation, compactness, and shape factors.

Acceptance criteria:

- Chapter contains actual results, not only method descriptions.
- Figures referenced in LaTeX exist in `Graphics/`.
- Text answers RQ3 at least partially.

## Phase 5: Evaluation, Discussion, Conclusion, Abstract

Files:

- `XAI_Projektarbeit 19.54.42/Chapters/Evaluation-und-Vergleich.tex`
- `XAI_Projektarbeit 19.54.42/Chapters/Diskussion.tex`
- `XAI_Projektarbeit 19.54.42/Chapters/Ausblick.tex`
- `XAI_Projektarbeit 19.54.42/FrontBackmatter/Abstract.tex`

Order:

1. Evaluation and comparison: answer RQ1, RQ2, RQ3 directly.
2. Discussion: limitations, correlated features, class imbalance, XAI reliability, domain fit.
3. Conclusion/outlook: short summary, final answer, future work.
4. Abstract: write last, once results are stable.

Acceptance criteria:

- RQ1, RQ2, and RQ3 are answered explicitly.
- Limitations are named honestly.
- Abstract summarizes data, methods, main results, XAI findings, and limitations.

## Phase 6: Notebook And Report Consistency Check

Checklist:

- `02_model_training.ipynb` values match `Ergebnisse-der-Klassifikation.tex`.
- `03_xai_explanations.ipynb` feature set matches training notebook and report.
- All report figures exist locally.
- No report text promises an XAI method that is not implemented.
- Current Overleaf export contains the latest graphics.
- If Overleaf is updated manually, export/copy the newest folder locally before final check.

Known issue to watch:

- Local `ucimlrepo` fetch can fail with SSL certificate errors. Do not bake an unsafe SSL workaround into the notebook unless the user explicitly accepts it. Prefer fixing the local environment or using a documented data-loading fallback.

## Phase 7: Final Quality Gate

Run or verify:

- Notebook execution from top to bottom.
- LaTeX/Overleaf compile without missing figures or citations.
- Requirements from `Projektarbeit_Anforderungen.md` are all covered.
- Metrics and figure filenames are consistent.
- `_context-helper/` files reflect any new decisions.

## Copy-Paste Prompt For Next Chat

Continue from this handoff. First read `_context-helper/START_HERE.md`, `_context-helper/NEXT_STEPS.md`, `_context-helper/CONTEXT_STATE.json`, and `_context-helper/EVIDENCE_INDEX.md`. Treat `XAI_Projektarbeit 19.54.42/` as the current report export unless a newer `XAI_Projektarbeit*` folder exists and the user confirms it. Use `human-voice-writer` for report prose. Ground all methodological justifications in checked sources with locators. Task: complete the XAI notebook and then fill the XAI report chapter so the report and notebook satisfy `Projektarbeit_Anforderungen.md`.
