# CONTEXT

## Project Purpose

The project is a German academic report for an Explainable AI module. It studies the Dry Bean Dataset as a tabular multiclass classification problem and combines predictive modeling with explainability.

The report intentionally does not perform image processing from raw images. It uses already-extracted morphological features from a computer-vision-based dataset. This keeps the scope on classification, feature selection, evaluation, and explainability.

## Domain Framing

Dry beans can be sorted by visual/morphological properties. Relevant feature groups are size, axis length, elongation, roundness, compactness, and shape factors. Domain expectations recorded in `reports/notes/domain_research.md` include:

- `BOMBAY` should be comparatively easy to identify because it is large.
- Rounder varieties should be distinguishable via `Roundness`, `Compactness`, and `Eccentricity`.
- Longer varieties such as `HOROZ`, `SIRA`, or `DERMASON` may depend on `AspectRatio` and axis-like information.
- Highly correlated size features can distort or diffuse XAI explanations.

## Methodological Framing

The report uses Accuracy and Macro-F1. Macro-F1 matters because the class distribution is imbalanced. Confusion matrices are used to inspect which varieties get confused.

XAI is framed as a way to check whether model decisions align with morphologically plausible patterns, not only as a technical add-on. Global and local explanations are planned.

## Current Written Narrative

The written chapters in the current Overleaf export `XAI_Projektarbeit 19.54.42/` establish a coherent narrative:

- Motivation: reliable and understandable automated bean variety recognition.
- Problem: similar morphology, correlated features, imbalanced classes.
- Approach: compare four model families on a reduced, interpretable feature set.
- Evaluation: Accuracy, Macro-F1, confusion matrices.
- Explanation: planned use of SHAP, LIME, and Permutation Feature Importance.

The strongest next writing task is to fill XAI and final discussion sections using actual implemented outputs.
