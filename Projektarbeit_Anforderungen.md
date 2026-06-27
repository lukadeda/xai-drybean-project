Projektarbeit XAI
Aufgabenstellung

   Erklärbare Künstliche Intelligenz

         Prof. Dr. Christoph Tholen

                                                                                                                                                     1
Lernziele

  · Lernziele dieser Projektarbeit

        - Eigenständiges Trainieren und Bewerten von Multiclass-Klassifikatoren
        - Anwendung etablierter XAI-Methoden (SHAP, LIME, Permutation Importance) auf tabulare Daten
        - Kritische Bewertung von Erklärungen und Abgleich mit Domänenwissen
        - Selbstständige Literaturrecherche und Anfertigen einer wissenschaftlichen Arbeit

Prof. Dr. Christoph Tholen                                                                            2
Der Datensatz im Überblick

  · Dry Bean Dataset

        - Dry Bean [Dataset]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C50S4B.
        - Donatoren: M. Koklu & I. A. Ozkan, Selçuk
        - Lizenz: Creative Commons Attribution 4.0 International (CC BY 4.0)
        - https://archive.ics.uci.edu/dataset/602/dry+bean+dataset

  · Eckdaten

        - 13.611 Instanzen - ausreichend für robustes Training und Cross-Validation
        - 7 Klassen registrierter Bohnensorten: Seker, Barbunya, Bombay, Cali, Dermosan, Horoz, Sira
        - 16 numerische Features aus computer-vision-basierter Bildauswertung
        - Keine fehlenden Werte

Prof. Dr. Christoph Tholen                                                                               3
Klassen und Datencharakteristik

  · Klassenverteilung

        - Dermosan: 3.546 | Sira: 2.636 | Seker: 2.027 | Horoz: 1.928
        - Cali: 1.630 | Barbunya: 1.322 | Bombay: 522

  · Datencharakteristik

        - Klassen-Imbalance ca. 7:1 (Dermosan vs. Bombay)
        - Alle Features kontinuierlich, keine kategorialen Variablen
        - Hohe Korrelation zwischen Größenmerkmalen (z. B. Area, ConvexArea, EquivDiameter)

Prof. Dr. Christoph Tholen                                                                   4
Feature-Übersicht

  · Dimensionale Features (12)

        - Area, Perimeter, MajorAxisLength, MinorAxisLength, AspectRation, Eccentricity
        - ConvexArea, EquivDiameter, Extent, Solidity, Roundness, Compactness

  · Formfaktoren (4)

        - ShapeFactor1, ShapeFactor2, ShapeFactor3, ShapeFactor4

  · Hinweis zur Aufgabenstellung

        - Es sollen 5 bis 10 Features für die Modellierung ausgewählt werden
        - Begründete Auswahl auf Basis von Korrelationsanalyse, Domänenwissen oder XAI-gestützter Feature

           Importance
        - Die Feature-Auswahl ist Teil der wissenschaftlichen Eigenleistung

Prof. Dr. Christoph Tholen                                                                                 5
Die sieben Bohnensorten im Vergleich

Prof. Dr. Christoph Tholen            6
Aufgabenstellung

  · Hauptaufgabe

        - Entwicklung eines Multiclass-Klassifikators und dessen Erklärung mittels XAI-Methoden

  · Teilaufgaben

        - 1. Explorative Datenanalyse und begründete Auswahl von 5-10 Features
        - 2. Training mindestens zweier Klassifikatoren (z. B. Random Forest, Gradient Boosting, Neural Network)
        - 3. Bewertung mittels geeigneter Metriken (Accuracy, Macro-F1, Konfusionsmatrix)
        - 4. Anwendung von mindestens zwei XAI-Methoden (z. B. SHAP, LIME, Permutation Importance)
        - 5. Vergleich globaler und lokaler Erklärungen für ausgewählte Instanzen
        - 6. Kritische Diskussion: Stimmen Erklärungen mit agrarwissenschaftlichem Domänenwissen überein?

Prof. Dr. Christoph Tholen                                                                                        7
Literaturhinweise

  · Datensatz und Anwendungsdomäne

        - Koklu, M. & Ozkan, I. A. (2020). Multiclass classification of dry beans using computer vision and machine
           learning techniques. Computers and Electronics in Agriculture, 174, 105507.

        - Krishnan, S. et al. (2023). Identification of Dry Bean Varieties Using CatBoost. Scientific Programming.

  · XAI-Methodik

        - Lundberg, S. M. & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. NeurIPS.
        - Ribeiro, M. T., Singh, S. & Guestrin, C. (2016). Why Should I Trust You? KDD.
        - Molnar, C. (2022). Interpretable Machine Learning. 2. Auflage, frei online verfügbar.
        - Salih, A. M. et al. (2025). A Perspective on Explainable AI Methods: SHAP and LIME. Advanced Intelligent

           Systems.

Prof. Dr. Christoph Tholen                                                                                           8
Beispiel NN in KNIME

Prof. Dr. Christoph Tholen  9
Abgaben

· Forschungsfrage und Umsetzungsstrategie             05.05.2026

- Literaturrecherche zur Domäne

- Durchführen erster Versuche zur Auswahl von Features für die Vorhersage

- Vorauswahl von mind. drei KI-Modellen für die Klassifikation

· Präsentation Stand der Wissenschaft (Bonus) bis 02.06.2026

      - Präsentation zu einer ausgewählten aktuellen XAI-Publikation

· Abgabe Stand für Peer-Review                        15.-17.06.2026

      - Abgabe eines Zwischenstandes des Berichts
      - Sie erhalten Feedback von Ihren Kommilitonen

· Präsentation der Zwischenstände                     07.07. & 14.07.2026 (Anwesenheitspflicht)

· Finale Abgabe                                       14.08.2026

- Schriftlicher Bericht im PDF-Format

- Reproduzierbarer Quellcode (Jupyter-Notebook oder Python-Skripte) bzw. KNIME-Workflow inkl. README

Prof. Dr. Christoph Tholen                                                                            10
