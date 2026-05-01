# Erste Versuche zur Feature-Auswahl

## Ziel

Fuer die Abgabe am 05.05.2026 wurden erste Versuche zur Feature-Auswahl durchgefuehrt. Dabei wurden mehrere Feature-Sets mit den drei vorausgewaehlten Modellen verglichen:

- LogisticRegression als Baseline und gut interpretierbares lineares Modell
- RandomForestClassifier als robustes Ensemble mit Feature Importances
- HistGradientBoostingClassifier als modernes, leistungsstarkes Boosting-Modell

Die Bewertung erfolgte mit einem stratifizierten 80/20 Train-Test-Split und den Metriken Accuracy sowie Macro-F1. Macro-F1 ist besonders relevant, weil die Klassenverteilung unausgeglichen ist.

## Getestete Feature-Sets

| Feature-Set | Anzahl | Idee |
|---|---:|---|
| `all_16_features` | 16 | Referenz mit allen vorhandenen Merkmalen |
| `domain_8_features` | 8 | fachlich interpretierbare Mischung aus Groesse, Umfang, Rundheit, Laenglichkeit und Formfaktoren |
| `compact_6_features` | 6 | staerker reduzierte Variante mit weniger Merkmalen |
| `mixed_10_features` | 10 | groessere Auswahl mit zusaetzlichen Achsen- und Umfangsmerkmalen |

## Ergebnisse

| Feature-Set | Features | Modell | Accuracy | Macro-F1 |
|---|---:|---|---:|---:|
| `all_16_features` | 16 | Hist Gradient Boosting | 0.9243 | 0.9372 |
| `all_16_features` | 16 | Random Forest | 0.9218 | 0.9339 |
| `all_16_features` | 16 | Logistic Regression | 0.9214 | 0.9335 |
| `domain_8_features` | 8 | Hist Gradient Boosting | 0.9174 | 0.9293 |
| `domain_8_features` | 8 | Logistic Regression | 0.9159 | 0.9292 |
| `domain_8_features` | 8 | Random Forest | 0.9155 | 0.9278 |
| `compact_6_features` | 6 | Logistic Regression | 0.9078 | 0.9208 |
| `compact_6_features` | 6 | Random Forest | 0.9053 | 0.9179 |
| `compact_6_features` | 6 | Hist Gradient Boosting | 0.9005 | 0.9135 |
| `mixed_10_features` | 10 | Logistic Regression | 0.9100 | 0.9234 |
| `mixed_10_features` | 10 | Hist Gradient Boosting | 0.9115 | 0.9228 |
| `mixed_10_features` | 10 | Random Forest | 0.9093 | 0.9211 |

## Durchschnitt ueber die drei Modelle

| Feature-Set | Features | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| `all_16_features` | 16 | 0.9225 | 0.9349 |
| `domain_8_features` | 8 | 0.9163 | 0.9288 |
| `mixed_10_features` | 10 | 0.9103 | 0.9224 |
| `compact_6_features` | 6 | 0.9045 | 0.9174 |

## Random-Forest-Feature-Importance mit allen Features

Die hoechsten Feature Importances lagen bei:

| Rang | Feature | Importance |
|---:|---|---:|
| 1 | `Perimeter` | 0.1038 |
| 2 | `ShapeFactor3` | 0.0980 |
| 3 | `ShapeFactor1` | 0.0975 |
| 4 | `Compactness` | 0.0912 |
| 5 | `MinorAxisLength` | 0.0882 |
| 6 | `Eccentricity` | 0.0653 |
| 7 | `ConvexArea` | 0.0652 |
| 8 | `Area` | 0.0648 |

## Vorlaeufige Bewertung

Alle 16 Features liefern erwartungsgemaess die beste Modellleistung. Fuer die Projektarbeit ist jedoch nicht nur Performance relevant, sondern auch Interpretierbarkeit und eine begruendete Auswahl von 5 bis 10 Features.

Als erster Arbeitsstand wird deshalb `domain_8_features` vorgeschlagen:

```text
Area
Perimeter
AspectRation
Compactness
roundness
ShapeFactor1
ShapeFactor2
ShapeFactor4
```

Diese Auswahl ist fachlich gut begruendbar, da sie Groesse, Umfang, Laenglichkeit, Rundheit und Formfaktoren abdeckt. Gleichzeitig vermeidet sie mehrere stark korrelierte Groessen- und Achsenmerkmale wie `ConvexArea`, `EquivDiameter`, `MajorAxisLength` und `MinorAxisLength`. Die Modellleistung liegt mit einem mittleren Macro-F1 von ca. 0.929 ueber der 10-Feature-Variante und ausreichend nahe an der Referenz mit allen Features.

`ShapeFactor3` wird bewusst nicht aufgenommen, da es im Datensatz praktisch exakt `Compactness²` entspricht und damit redundant zu `Compactness` ist.

Fuer die naechsten Schritte sollte diese Auswahl mit Permutation Importance und SHAP weiter geprueft werden.
