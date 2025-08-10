
# Chatbot Project (Intent Classification + OOS Detection)

This repository contains a complete scaffold for building an intent-classification chatbot with out-of-scope (OOS) detection using Python and Streamlit for the UI.

## Structure
```
chatbot-project/
├─ data/
│  ├─ raw/                  # raw JSON files (your uploads)
│  └─ processed/            # processed CSV/JSON produced by notebooks
├─ notebooks/               # Jupyter notebooks (step-by-step)
├─ src/                     # helper Python modules
│  └─ app/                  # Streamlit app
├─ models/                  # saved model artifacts
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## Notebooks (run in order)
1. `01_data_overview.ipynb` - load raw JSONs and EDA
2. `02_preprocessing_and_splits.ipynb` - cleaning and dataset splits
3. `03_feature_engineering_and_embeddings.ipynb` - TF-IDF and embedding examples
4. `04_train_intent_classifier.ipynb` - train baseline classifiers
5. `05_oos_detection_and_thresholding.ipynb` - OOS strategies and tuning
6. `06_evaluation_and_error_analysis.ipynb` - metrics, confusion matrix, analysis
7. `07_streamlit_demo_and_integration.ipynb` - Streamlit demo and integration steps

## Quickstart
1. Create and activate virtual env:
   - Linux/macOS: `python -m venv venv && source venv/bin/activate`
   - Windows (Powershell): `python -m venv venv; .\venv\Scripts\Activate.ps1`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run notebooks to preprocess and train models.
4. Run the demo UI:
   ```bash
   streamlit run src/app/streamlit_app.py
   ```

## Notes
- The repo includes placeholders and starter code. Notebooks contain step-by-step cells which you can run and extend.
- Uploaded raw JSONs (if present) are copied to `data/raw/`.
