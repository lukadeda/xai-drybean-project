# Literaturrecherche zur Domaene

## Domaene

Die Arbeit liegt im Bereich der automatischen Sortenerkennung von Trockenbohnen anhand morphologischer Bildmerkmale. Der Dry Bean Datensatz enthaelt numerische Merkmale, die aus computer-vision-basierter Bildauswertung gewonnen wurden.

## Fachlich relevante Merkmalsgruppen

- Groesse: `Area`, `ConvexArea`, `EquivDiameter`
- Laenge und Breite: `MajorAxisLength`, `MinorAxisLength`
- Laenglichkeit: `AspectRation`, `Eccentricity`
- Rundheit und Kompaktheit: `roundness`, `Compactness`, `ShapeFactor1-4`

## Erste fachliche Annahmen

- Sehr grosse Sorten wie `Bombay` sollten stark durch Groessenmerkmale erkennbar sein.
- Runde Sorten sollten sich ueber `roundness`, `Compactness` und `Eccentricity` abgrenzen lassen.
- Laengliche Sorten wie `Horoz`, `Sira` oder `Dermosan` sollten durch `AspectRation` und Achsenlaengen unterscheidbar sein.
- Stark korrelierte Groessenmerkmale sollten nicht unkritisch gemeinsam verwendet werden, weil sie XAI-Erklaerungen verzerren koennen.

## Startliteratur

- Koklu, M. & Ozkan, I. A. (2020). Multiclass classification of dry beans using computer vision and machine learning techniques. Computers and Electronics in Agriculture, 174, 105507.
- Krishnan, S. et al. (2023). Identification of Dry Bean Varieties Using CatBoost. Scientific Programming.
