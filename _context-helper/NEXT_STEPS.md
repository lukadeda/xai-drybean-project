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

## Phase 1: XAI Notebook Completed

Status: completed.

File: `notebooks/03_xai_explanations.ipynb`.

Completed work:

1. `notebooks/03_xai_explanations.ipynb` uses the final selected features: `Area`, `AspectRatio`, `Eccentricity`, `Compactness`, `Roundness`, `ShapeFactor1`, `ShapeFactor2`, `ShapeFactor4`.
2. It uses the same split logic as training: `test_size=0.2`, `stratify=y`, `random_state=42`.
3. It trains the final Random Forest configuration from `02_model_training.ipynb`.
4. It loads the UCI CSV directly with a `certifi` SSL context to avoid `ucimlrepo` CSV SSL failures in VS Code/Python setups.
5. It implements Permutation Importance, global SHAP, local SHAP, and local LIME.
6. It exports all XAI figures to both `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`.

Verified acceptance criteria:

- Notebook runs top to bottom in the project environment.
- XAI notebook uses the same feature set and split as the training notebook.
- Three XAI methods are implemented: Permutation Importance, SHAP, and LIME.
- Global and local explanations are produced.
- Figures are exported to the current report export under `XAI_Projektarbeit 19.54.42/Graphics/`.

## Phase 2: Implemented XAI Methods

Status: completed. The final implementation includes Permutation Importance, SHAP, and LIME.

Permutation Importance:

- Use `sklearn.inspection.permutation_importance`.
- Score with `f1_macro` to match the report focus on Macro-F1.
- Exported PDF: `Graphics/Permutation_Importance_RandomForest.pdf`.
- Save a table or print output with feature rankings.

SHAP:

- Use a source-backed justification for the chosen explainer.
- If using a tree model, check SHAP documentation and Molnar before writing that TreeSHAP is efficient for tree models.
- Produced a global SHAP ranking and local SHAP explanation.
- Exported figures: `Graphics/SHAP_Global_RandomForest.pdf` and `Graphics/SHAP_Local_RandomForest.pdf`.

LIME:

- Implemented a local explanation for the same correctly classified test instance used by local SHAP.
- Exported figure: `Graphics/LIME_Local_RandomForest.pdf`.

Current local case:

- One correctly classified `DERMASON` instance. SHAP and LIME explain the same instance.
- Optional improvement if time permits: add a `DERMASON`/`SIRA` confusion case because that is the dominant error pattern in the confusion matrices.

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
3. Keep the report promise in `Einleitung.tex` and `Grundlagen.tex` aligned with the implemented methods: SHAP, LIME, and Permutation Feature Importance are now all implemented and used in the XAI chapter.

Acceptance criteria:

- No methodological justification appears in the report without a citation.
- Claims about runtime, model compatibility, or interpretation limits are backed by checked sources.

## Phase 4: XAI Report Chapter Completed

Status: completed for the current export.

File: `XAI_Projektarbeit 19.54.42/Chapters/XAI-Methoden.tex`.

The chapter now covers:

1. Ziel der XAI-Auswertung.
2. Begründung der Modellwahl für die XAI-Auswertung.
3. Globale Erklärungen mit Permutation Feature Importance.
4. Globale SHAP-Auswertung.
5. Lokale SHAP-Erklärung.
6. Lokale LIME-Erklärung.
7. Vergleich der XAI-Methoden.
8. Zwischenfazit mit Domänenwissen.

Verified:

- All referenced XAI figures exist in `XAI_Projektarbeit 19.54.42/Graphics/`.
- Local `latexmk -pdf -interaction=nonstopmode -halt-on-error htwsaar-i-mst-vorlage.tex` succeeds.
- Remaining LaTeX messages are Overfull/PDF-version warnings, not hard errors.

Historical suggested structure retained below for reference:

Suggested structure:

1. Ziel der XAI-Auswertung.
2. Begründung der Modellwahl für die XAI-Auswertung.
3. Globale Erklärungen mit Permutation Feature Importance.
4. Globale SHAP-Auswertung.
5. Lokale SHAP-Erklärungen.
6. Lokale LIME-Erklärung.
7. Vergleich der XAI-Methoden.
8. Zwischenfazit mit Domänenwissen.

Writing rules:

- Use natural German prose.
- Do not overstate. Say what the figures show.
- Distinguish data-backed findings from interpretation.
- Tie XAI findings back to morphology: size, roundness, elongation, compactness, and shape factors.

Acceptance criteria:

- Chapter contains actual results, not only method descriptions.
- Figures referenced in LaTeX exist in `Graphics/`.
- Text answers RQ3 at least partially.
- Text justifies why Random Forest is used for XAI although MLP is narrowly best by Macro-F1.

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
- XAI report text references all implemented XAI figures with exact filenames.
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

Continue from this handoff. First read `_context-helper/START_HERE.md`, `_context-helper/NEXT_STEPS.md`, `_context-helper/CONTEXT_STATE.json`, and `_context-helper/EVIDENCE_INDEX.md`. Treat `XAI_Projektarbeit 19.54.42/` as the current report export unless a newer `XAI_Projektarbeit*` folder exists and the user confirms it. Use `human-voice-writer` for report prose. Ground all methodological justifications in checked sources with locators. Task: write the XAI report chapter from the already executed XAI notebook outputs, then complete evaluation/discussion/conclusion/abstract and run final consistency checks.
