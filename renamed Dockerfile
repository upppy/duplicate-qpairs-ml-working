# 1. Base Python image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first (cache layer)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix fuzzywuzzy warning — install Levenshtein for faster matching
# ❗ Best to install inside requirements.txt, not separately
RUN pip install python-Levenshtein

# 5. Copy the entire project
COPY . .

# 6. Streamlit configuration
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLE_CORS=false \
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false \
    STREAMLIT_SERVER_PORT=8501

# 7. Expose port
EXPOSE 8501

# 8. Run Streamlit app
CMD ["streamlit", "run", "streamlit-app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
