# Duplicate Question Pair Detection – Streamlit Application

This project is an end-to-end Machine Learning application that identifies whether two questions are duplicates of each other. The application is built using **Streamlit** as the frontend interface and uses a trained ML model at the backend.

---

## 🔍 Problem Description
Online platforms receive multiple user queries that may have the same meaning. Identifying and grouping these similar questions helps:
- Reduce redundant answers
- Improve search relevance
- Improve user experience

This project aims to classify a pair of questions as:
✔ Duplicate  
❌ Not Duplicate

---

## 🚀 Key Features
- Interactive Streamlit web UI
- Preprocessed text with:
  - Stop-word removal
  - Character normalization
  - Spelling simplification
  - Removal of unwanted symbols
- Custom similarity features:
  - Word ratios
  - Fuzzy matching scores
  - Longest common substring ratio
  - Length-based similarity
- Bag-of-Words representation
- Pretrained ML model for prediction

---

## 🧠 Model Components
The project uses:
- `model.pkl` → Trained classification model  
- `cv.pkl` → CountVectorizer for feature generation  
- `stopwords.pkl` → Custom stop-word list  

The model was trained using Jupyter notebooks based on extensive feature engineering.

---

## 📁 Project Structure
```
project/
│── streamlit-app/
│   │── app.py                 # Main Streamlit UI
│   │── helper.py              # Feature generation + preprocessing
│   │── model.pkl              # ML model
│   │── cv.pkl                 # CountVectorizer
│   │── stopwords.pkl          # Stopwords used during model building
│   │── Procfile               # For deployment usage (optional)
│   │── setup.sh               # Deployment config (optional)
│
│── requirements.txt           # Project dependencies
│── README.md                  # Documentation
│── train.csv (optional)       # Training dataset
│── notebooks/*.ipynb (optional training files)
```

Only the `streamlit-app` folder is required to run the application.

---

## 🏃 How to Run Locally

### 1. Install Dependencies
```
pip install -r requirements.txt
```

### 2. Start the Application
```
streamlit run streamlit-app/app.py
```

After successful execution, your local browser will automatically open at:
```
http://localhost:8501/
```

---

## 🧪 How It Works Internally

### Step-wise Flow:
1. User enters **Question 1** and **Question 2**
2. Application invokes helper methods
3. Input is cleaned and converted into feature vectors
4. Vectorized data is passed to the trained ML model
5. Model predicts:
   - `1` → Duplicate  
   - `0` → Not duplicate  
6. Result is displayed back on UI

### Feature Generation Includes:
- Word overlap measures
- Stopword-based similarity
- Normalized length comparison
- Fuzzy string metrics
- Bag-of-Words vectors for both questions

---

## 🧰 Technology Stack
| Component        | Technology Used |
|------------------|-----------------|
| UI Framework     | Streamlit       |
| Model Training   | Scikit-learn    |
| Feature Handling | NumPy, Pandas   |
| Text Transformation | CountVectorizer |
| Deployment Ready | Heroku/Docker   |

---

## 🌐 Deployment Support
You can deploy using:
- Heroku  
- Render  
- Local server  
- Docker  

Heroku required files already included:
- `Procfile`
- `setup.sh`
- `requirements.txt`

---

## 🗑 Recommended Cleanup (Optional)
You can safely remove these if deployment-only use:

❌ `.ipynb_checkpoints`  
❌ `__pycache__`  
❌ multiple `.pkl` duplicates in root  
❌ virtual environment folders like:
- `.venv/`
- `venv/`  

Recommended organization:
```
data/ → train.csv  
notebooks/ → *.ipynb  
scripts/ → version.py (optional utility)
```

---

## 📌 Future Scope
- Add explanation / interpretability of prediction
- Enable multi-language support
- Show similarity scores visually
- Save user queries for analytics

---

## ✔️ Conclusion
This project demonstrates how ML models can be used for meaningful text-based similarity prediction in real-time. Using data preprocessing, handcrafted features, and an interactive web UI, this application is fully deployable and production ready.
