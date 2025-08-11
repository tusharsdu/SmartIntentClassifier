# Smart Intent Classifier

**Project Status:** Completed  
**Course:** Introduction to Artificial Intelligence (AAI-501-IN1) – University of San Diego (USD)  
**Instructor:** Ankur Bist  
**Submission Date:** 11-08-2025  

---

## 📌 Project Intro / Objective
The **Smart Intent Classifier** is an NLP-based chatbot intent recognition system built using the **CLINC150 dataset**.  
It is designed to:
- **Classify user intents** across 150 categories.
- Detect **Out-of-Scope (OOS)** queries.
- Continuously improve via a **self-learning feedback loop**.

This project demonstrates the integration of **Natural Language Processing**, **Deep Learning**, and **adaptive learning techniques** to create a scalable, domain-independent intent classification model.

---

## 👥 Contributors
- **Tushar Gorad**
- **Soura Keshari Biswal**
- **Uhana Jyothi Chitti**

---

## 🛠 Methods Used
- Natural Language Processing (NLP)
- Deep Learning & Transformer Models (BERT / DistilBERT)
- Reinforcement Learning-style Feedback
- Out-of-Scope Detection
- Data Visualization & EDA
- Model Evaluation (Precision, Recall, F1-score, Confusion Matrix)

---

## 💻 Technologies
- Python
-  PyTorch
- HuggingFace Transformers
- NLTK / spaCy
- scikit-learn
- pandas, NumPy, seaborn, matplotlib
- Streamlit (UI)

---

## 📂 Dataset Description
- **Dataset:** CLINC150  
- **Files:** `data_full.json`,  
- **Description:** 150 intents across multiple domains (banking, travel, utilities, etc.), with Out-of-Scope queries for robustness.  
- **Stats:**  
  - ~23,700 in-domain samples  
  - Balanced distribution across domains  
  - OOS queries included for better real-world performance

---

## 🚀 Project Roadmap
1. **Setup & Dataset Preparation** – Repository creation, venv, dataset download, EDA.  
2. **Preprocessing & NLP Pipeline** – Tokenization, cleaning, embedding generation (TF-IDF / BERT).  
3. **Model Development** – Transformer model with OOS detection, early stopping.  
4. **Self-Learning** – Confidence tracking, simulated feedback loop.  
5. **Evaluation** – Accuracy, precision, recall, F1-score, confusion matrix.  
6. **Deployment** – Streamlit UI, optional API, CLI tool.  
7. **Documentation** – README, report, contribution logs.

---

## ⚙️ Installation & Setup
**Clone the repository:**
- git clone https://github.com/tusharsdu/SmartIntentClassifier.git
- cd SmartIntentClassifier 

## Install dependencies:
pip install -r requirements.txt
## ▶️ Steps to Run
**Clean Data**
- python -m src.data_processing

**Train the Model** 
 - python -m src.model_training

**Run the Streamlit App**
- streamlit run streamlit_app/app.py
