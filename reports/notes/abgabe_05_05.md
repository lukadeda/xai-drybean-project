# Abgabe 05.05.2026: Forschungsfrage und Umsetzungsstrategie

## Forschungsfrage

Inwiefern lassen sich Dry-Bean-Sorten anhand weniger morphologischer Bildmerkmale zuverlaessig klassifizieren, und welche Merkmale erklaeren die Entscheidungen verschiedener Multiclass-Klassifikatoren am staerksten?

## Literaturrecherche zur Domaene

Die Domaene der Projektarbeit ist die automatische Sortenerkennung von Trockenbohnen anhand morphologischer Bildmerkmale. Der verwendete Dry Bean Datensatz basiert auf computer-vision-basierter Bildauswertung und enthaelt sieben Bohnensorten: `SEKER`, `BARBUNYA`, `BOMBAY`, `CALI`, `DERMASON`, `HOROZ` und `SIRA`.

Die fachliche Annahme ist, dass sich diese Sorten vor allem durch Groesse und Form unterscheiden. Entsprechend sind Merkmale wie `Area`, `Perimeter`, `MajorAxisLength`, `MinorAxisLength`, `AspectRation`, `Eccentricity`, `roundness`, `Compactness` und die `ShapeFactor`-Features fuer die Klassifikation relevant. Sehr grosse Sorten wie `BOMBAY` sollten beispielsweise stark ueber Groessenmerkmale erkennbar sein, waehrend laengliche Sorten eher durch Achsenverhaeltnisse und Formmerkmale beschrieben werden.

Als Startliteratur werden insbesondere Koklu und Ozkan (2020) verwendet, da diese Arbeit den Dry Bean Datensatz und die computer-vision-basierte Klassifikation beschreibt. Ergaenzend wird Krishnan et al. (2023) betrachtet, da dort moderne Boosting-Verfahren fuer die Identifikation von Dry-Bean-Sorten verwendet werden.

## Erste Versuche zur Auswahl von Features fuer die Vorhersage

Mit der Anforderung ist gemeint, dass die Feature-Auswahl nicht nur theoretisch begruendet wird, sondern erste datenbasierte Experimente durchgefuehrt werden. Ziel ist es, aus den 16 vorhandenen Features eine begruendete Auswahl von 5 bis 10 Merkmalen fuer die Modellierung abzuleiten.

Dafuer wurden vier Feature-Sets verglichen:

| Feature-Set | Anzahl Features | Idee |
|---|---:|---|
| `all_16_features` | 16 | Referenzmodell mit allen Merkmalen |
| `mixed_10_features` | 10 | groessere Auswahl mit Groessen-, Achsen- und Formmerkmalen |
| `domain_8_features` | 8 | fachlich interpretierbare Auswahl aus Groesse, Laenglichkeit, Rundheit und Formfaktoren |
| `compact_6_features` | 6 | staerker reduzierte Variante |

Die Bewertung erfolgte mit einem stratifizierten 80/20 Train-Test-Split. Als Metriken wurden Accuracy und Macro-F1 verwendet. Macro-F1 ist wichtig, da die Klassenverteilung unausgeglichen ist, insbesondere zwischen `DERMASON` und `BOMBAY`.

Die ersten Ergebnisse zeigen:

| Feature-Set | Anzahl Features | Durchschnittliche Accuracy | Durchschnittlicher Macro-F1 |
|---|---:|---:|---:|
| `all_16_features` | 16 | 0.9225 | 0.9349 |
| `domain_8_features` | 8 | 0.9163 | 0.9288 |
| `mixed_10_features` | 10 | 0.9103 | 0.9224 |
| `compact_6_features` | 6 | 0.9045 | 0.9174 |

Alle 16 Features liefern erwartungsgemaess die beste reine Modellleistung. Fuer die Projektarbeit ist jedoch nicht nur Performance relevant, sondern auch Interpretierbarkeit und eine nachvollziehbare Begruendung der Feature-Auswahl. Das 8-Feature-Set bleibt nahe an der Leistung aller Features und schneidet in den ersten Versuchen besser ab als die 10-Feature-Variante.

Neben Varianten mit 6, 10 und 16 Features wurde ein 8-Feature-Set getestet. Dieses Set wurde bevorzugt, weil es in den ersten Versuchen eine bessere durchschnittliche Macro-F1-Leistung als die 10-Feature-Variante erreicht hat und gleichzeitig kompakter sowie besser interpretierbar ist.

Die 8-Feature-Auswahl konzentriert sich auf Merkmale, die fachlich gut erklaerbar sind: Groesse, Umfang, Laenglichkeit, Rundheit, Kompaktheit und ergaenzende Formfaktoren. Im Vergleich zu groesseren Feature-Sets wurden bewusst einige stark zusammenhaengende Achsen- und Groessenmerkmale weggelassen, zum Beispiel `MajorAxisLength`, `MinorAxisLength`, `ConvexArea` und `EquivDiameter`. Dadurch soll vermieden werden, dass sehr aehnliche Informationen mehrfach in das Modell eingehen und spaetere XAI-Erklaerungen schwerer interpretierbar werden.

`ShapeFactor3` wird ebenfalls nicht verwendet, da eine Pruefung der Daten gezeigt hat, dass dieses Merkmal praktisch exakt `Compactness²` entspricht. Es wuerde daher vor allem dieselbe Information wie `Compactness` nochmals in transformierter Form einbringen.

Als vorlaeufige Feature-Auswahl wird daher folgendes Set verwendet:

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

Diese Auswahl kombiniert Groesse, Laenglichkeit, Rundheit und Formfaktoren. Gleichzeitig vermeidet sie, mehrere stark korrelierte Groessenfeatures wie `Area`, `ConvexArea` und `EquivDiameter` gleichzeitig zu verwenden. Im weiteren Projektverlauf soll diese Auswahl mit XAI-Methoden wie Permutation Importance und SHAP weiter geprueft werden.

Die einzelnen Features wurden aus folgenden Gruenden ausgewaehlt:

| Feature | Bedeutung | Begruendung fuer die Auswahl |
|---|---|---|
| `Area` | Flaeche der Bohne | bildet die Groesse ab und hilft besonders bei der Unterscheidung sehr grosser oder kleiner Sorten |
| `Perimeter` | Umfang der Bohne | war in der Random-Forest-Feature-Importance besonders relevant und ergaenzt die reine Flaecheninformation |
| `AspectRation` | Verhaeltnis von Laenge zu Breite | beschreibt, ob eine Bohne eher rundlich oder laenglich ist |
| `Compactness` | Kompaktheit der Bohnenform | wichtig zur Unterscheidung aehnlich grosser, aber unterschiedlich geformter Sorten |
| `roundness` | Rundheit | fachlich gut interpretierbares Merkmal zur Abgrenzung runder und laenglicher Sorten |
| `ShapeFactor1` | geometrischer Formfaktor | ergaenzt Groessen- und Forminformationen und zeigte im Random Forest eine hohe Relevanz |
| `ShapeFactor2` | geometrischer Formfaktor | liefert zusaetzliche Forminformation und unterstuetzt die Trennung aehnlicher Klassen |
| `ShapeFactor4` | geometrischer Formfaktor | liefert zusaetzliche Forminformation und ist weniger redundant zu `Compactness` als `ShapeFactor3` |

Die Auswahl deckt damit verschiedene fachlich sinnvolle Merkmalsgruppen ab: Groesse und Umfang (`Area`, `Perimeter`), Laenglichkeit (`AspectRation`), Rundheit und Kompaktheit (`roundness`, `Compactness`) sowie ergaenzende Formfaktoren (`ShapeFactor1`, `ShapeFactor2`, `ShapeFactor4`). Bewusst nicht aufgenommen wurden mehrere stark korrelierte Groessenmerkmale wie `ConvexArea` und `EquivDiameter`, da sie aehnliche Informationen wie `Area` enthalten und die Interpretierbarkeit der spaeteren XAI-Erklaerungen erschweren koennen.

Die bisherigen Ergebnisse sind als erste Vorversuche und nicht als finale Modellbewertung zu verstehen. Es wurde ein einfacher stratifizierter 80/20 Train-Test-Split verwendet, um eine erste datenbasierte Grundlage fuer die Feature-Auswahl zu erhalten. Ein umfassendes finales Training steht noch aus. Im weiteren Projektverlauf sollen die Modelle systematischer validiert werden, beispielsweise durch Cross-Validation, Hyperparameter-Tuning, Konfusionsmatrizen und detaillierte Classification Reports pro Klasse. Die hier dargestellten Werte dienen daher primaer dazu, die vorlaeufige Feature-Auswahl zu begruenden und die weitere Umsetzungsstrategie abzuleiten.

## Vorauswahl von KI-Modellen fuer die Klassifikation

Fuer die Klassifikation werden drei Modelle vorausgewaehlt, die gut in Python mit scikit-learn umsetzbar sind und unterschiedliche Modellfamilien abdecken:

| Modell | Rolle im Projekt | Begruendung |
|---|---|---|
| `LogisticRegression` | Baseline und lineares Vergleichsmodell | einfach interpretierbar, schnell trainierbar und geeignet, um zu pruefen, ob die Klassen linear gut trennbar sind |
| `RandomForestClassifier` | robustes Ensemble-Modell | stark fuer tabellarische Daten, wenig Tuning erforderlich, liefert Feature Importances und ist gut mit XAI-Methoden kombinierbar |
| `HistGradientBoostingClassifier` | modernes Boosting-Modell | leistungsstarkes Verfahren fuer tabellarische Daten, schneller sklearn-Ansatz und sinnvoller Vergleich zum Random Forest |

Diese Auswahl erlaubt einen Vergleich zwischen einem linearen Modell, einem Bagging-Ensemble und einem Boosting-Verfahren. Damit bleibt die Umsetzung praktisch gut machbar, deckt aber dennoch unterschiedliche Modelltypen ab.

## Weitere Umsetzungsstrategie

Im naechsten Schritt werden die drei Modelle systematisch trainiert und bewertet. Die naechste Phase umfasst die finale Modellvalidierung mit Cross-Validation, eine gezielte Optimierung der Modellparameter sowie die anschliessende XAI-Analyse der besten Modelle. Neben Accuracy und Macro-F1 wird eine Konfusionsmatrix verwendet, um zu analysieren, welche Bohnensorten besonders haeufig verwechselt werden. Anschliessend werden globale und lokale Erklaerungen mit XAI-Methoden erstellt, insbesondere mit Permutation Importance und SHAP. Die Erklaerungen werden danach kritisch mit dem Domaenenwissen abgeglichen, also vor allem mit der Frage, ob Groesse, Laenglichkeit, Rundheit und Formfaktoren fachlich plausible Entscheidungsgrundlagen darstellen.

## Verweise im Projekt

- Domaenenrecherche: `reports/notes/domain_research.md`
- Erste Feature-Auswahl-Versuche: `reports/notes/feature_selection_first_trials.md`
- EDA und Feature-Auswahl: `notebooks/01_eda_feature_selection.ipynb`
- Modelltraining: `notebooks/02_model_training.ipynb`
