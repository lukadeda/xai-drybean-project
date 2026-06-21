# OPEN QUESTIONS

- Has the user imported a newer Overleaf export than `XAI_Projektarbeit 19.54.42/`? If yes, switch authoritative checks to that newer export.
- Should SHAP and LIME actually be implemented, or should the report reduce its XAI scope to implemented Permutation Importance plus one additional method?
- Which model should be the primary XAI target: Random Forest, best MLP, HistGradientBoosting, or multiple models?
- Should the feature-selection mismatch in `01_eda_feature_selection.ipynb` markdown be corrected to remove `ShapeFactor3` from the prose?
- Which metric table is authoritative: the current report/`02_model_training.ipynb` table or `notebooks/modelvergleich.tex`?
- Are there formal requirements in `Projektarbeit_Anforderungen.pdf` that must be converted and indexed before final writing?
