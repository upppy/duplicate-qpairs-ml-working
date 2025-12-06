import sklearn
import joblib

# Load your existing trained model and vectorizer
trained_model = joblib.load("model.pkl")
trained_vectorizer = joblib.load("cv.pkl")

# Add scikit-learn version info
model_data = {
    "model": trained_model,
    "vectorizer": trained_vectorizer,
    "sklearn_version": sklearn.__version__,
}

# Save combined data
joblib.dump(model_data, 'model_data.pkl')
print("Saved model_data.pkl with scikit-learn version:", sklearn.__version__)
