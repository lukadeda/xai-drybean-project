# Brief: Zwischenstands-Praesentation

## Zweck

Eine separate Praesentation zum aktuellen Zwischenstand der XAI-Projektarbeit vorbereiten. Nicht den Bericht finalisieren, sondern den Stand verstaendlich und strukturiert vorstellen.

## Aktueller Projektstand

- Projekt: XAI Dry Bean Classification.
- Datensatz: UCI Dry Bean Dataset mit 13.611 Beobachtungen, 16 numerischen morphologischen Features und sieben Klassen.
- Ziel: Klassifikation der sieben Bohnensorten und Erklaerung der Modellentscheidungen mit XAI.
- EDA ist lauffaehig und zeigt Klassenverteilung, Datenqualitaet und starke Feature-Korrelationen.
- Finale Feature-Auswahl: `Area`, `AspectRatio`, `Eccentricity`, `Compactness`, `Roundness`, `ShapeFactor1`, `ShapeFactor2`, `ShapeFactor4`.
- Begruendung Feature-Auswahl: fachliche Abdeckung von Groesse/Form/Rundheit und Reduktion stark redundanter Merkmale.
- Training ist lauffaehig mit vier Modellen: Logistic Regression, Random Forest, HistGradientBoosting, MLP.
- Aktuelle Ergebnisse: MLP knapp beste Macro-F1, andere Modelle sehr nah beieinander.
- XAI-Notebook ist lauffaehig fuer Random Forest.
- Implementierte XAI-Methoden: Permutation Feature Importance, SHAP, LIME.
- XAI-Figuren liegen in `XAI_Projektarbeit 19.54.42/Graphics/`.

## Wichtige Ergebniswerte

Modellvergleich aus aktuellem Stand:

- MLP Neural Network: Accuracy `0.923`, Macro-F1 `0.934`.
- HistGradientBoosting: Accuracy `0.920`, Macro-F1 `0.932`.
- Random Forest: Accuracy `0.918`, Macro-F1 `0.931`.
- Logistic Regression: Accuracy `0.917`, Macro-F1 `0.931`.

XAI Random Forest:

- Macro-F1 im XAI-Notebook: `0.9311654788132865`.
- Permutation Importance Top 3: `ShapeFactor1`, `Roundness`, `Area`.
- Global SHAP Top 4: `ShapeFactor1`, `Area`, `ShapeFactor2`, `Compactness`.
- Lokale SHAP- und LIME-Erklaerung nutzen dieselbe korrekt klassifizierte `DERMASON`-Instanz.

## Verfuegbare Grafiken

Berichtsgrafikordner: `XAI_Projektarbeit 19.54.42/Graphics/`

- `Klassenverteilung_Bohnensorten.pdf`
- `Korrelationsmatrix_Features.pdf`
- `Konfusionsmatrizen_Alle_Modelle.pdf`
- `Permutation_Importance_RandomForest.pdf`
- `SHAP_Global_RandomForest.pdf`
- `SHAP_Local_RandomForest.pdf`
- `LIME_Local_RandomForest.pdf`

## Empfohlene Praesentationsstruktur

1. Thema und Forschungsfrage.
2. Datensatz und Problemstellung.
3. EDA: Klassenverteilung und Feature-Korrelationen.
4. Feature-Auswahl und Begruendung.
5. Modellvergleich: vier Modelle und Metriken.
6. Konfusionsmatrizen: wichtigste Fehlermuster.
7. XAI-Setup: Warum Random Forest fuer XAI?
8. Globale XAI-Ergebnisse: Permutation Importance und SHAP.
9. Lokale Erklaerungen: SHAP und LIME an einer Instanz.
10. Aktueller Stand, offene Arbeit, naechste Schritte.

## Wichtige Erklaerlogik

- Nicht behaupten, dass das Projekt fertig ist. Es ist ein Zwischenstand.
- Klar trennen: Notebook-Outputs existieren, Berichtskapitel sind noch nicht komplett geschrieben.
- Random Forest fuer XAI begruenden: starke Leistung, baumbasiert, SHAP praktikabel, keine Skalierung der Eingangsfeatures noetig.
- MLP bleibt im Modellvergleich wichtig, wird aber nicht als primaeres XAI-Modell genutzt.
- Feature-Reduktion als Interpretierbarkeitsentscheidung erklaeren, nicht als rein automatisches Feature-Ranking.
- Grenzen nennen: korrelierte Features erschweren XAI-Interpretation; lokale Erklaerungen sind beispielhaft.

## Naechste Schritte Nach Praesentation

- XAI-Kapitel im Bericht schreiben.
- Evaluation/Diskussion/Fazit/Abstract vervollstaendigen.
- Bericht und Notebook final synchronisieren.
- Overleaf-Kompilierung und Quellen/Citations pruefen.

## Relevante Kontextdateien

- `_context-helper/START_HERE.md`
- `_context-helper/CONTEXT_PACK.md`
- `_context-helper/NEXT_STEPS.md`
- `_context-helper/EVIDENCE_INDEX.md`
- `_context-helper/IMPORTANT_FILES.md`
- `notebooks/01_eda_feature_selection.ipynb`
- `notebooks/02_model_training.ipynb`
- `notebooks/03_xai_explanations.ipynb`
