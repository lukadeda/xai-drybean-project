# Dry Bean Classification with XAI

Classify Dry Bean varieties with machine learning and inspect individual model decisions with XAI methods. The project trains four classifiers on morphological bean features and produces feature-importance charts, SHAP values, and LIME explanations.

## Features

- Four-model comparison with Logistic Regression, Random Forest, HistGradientBoostingClassifier, and MLPClassifier
- Exploratory data analysis and selection of eight morphological features
- Confusion matrices for the final classifiers
- Global feature importance with permutation importance and SHAP
- Local SHAP and LIME explanations for correctly classified and misclassified samples
- Exported charts and CSV tables in the repository

## Requirements

- Python 3
- `pip`
- An internet connection for the initial dataset download

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The three final notebooks run in this order.

```bash
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/01_eda_feature_selection.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/02_model_training.ipynb
.venv/bin/jupyter-nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 notebooks/03_xai_explanations.ipynb
```

The notebooks download the [Dry Bean Dataset](https://archive.ics.uci.edu/dataset/602/dry+bean+dataset) through `ucimlrepo`. A fresh run needs an internet connection.

## Notebook flow

`01_eda_feature_selection.ipynb` explores the dataset and documents the final feature set.

`02_model_training.ipynb` trains and evaluates the four classifiers.

`03_xai_explanations.ipynb` compares their feature importance and produces global and local explanations. It writes figures and tables to `notebooks/` and `XAI_Projektarbeit 19.54.42/Graphics/`.

## Project structure

```text
data/         Optional local data and generated intermediate files
notebooks/    Analysis, training, and explanation notebooks
reports/      Notes and report assets
src/          Shared Python utilities
```
