# 🎫 Support Ticket Classification & Prioritization using NLP

An end-to-end **Natural Language Processing (NLP)** and **Machine Learning** project that automatically classifies customer support tickets into predefined categories and assigns a business priority level (High, Medium, or Low).

This project was developed as part of the **Future Interns Machine Learning Internship – Task 2**.

---

## 🚀 Features

- 📩 Automatic support ticket classification
- 🧠 NLP-based text preprocessing
- 📊 TF-IDF feature extraction
- 🤖 Multinomial Naive Bayes classifier
- 🚨 Rule-based priority assignment (High / Medium / Low)
- 📈 Model evaluation using Accuracy, Precision, Recall, F1-Score, Classification Report, and Confusion Matrix
- 🌐 Interactive Streamlit web application

---

## 📂 Dataset

**Dataset:** `all_tickets_processed_improved_v3.csv`

The dataset contains processed customer support ticket descriptions and their corresponding support categories.

### Supported Categories

- Access
- Administrative Rights
- Hardware
- HR Support
- Internal Project
- Miscellaneous
- Purchase
- Storage

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## 🔄 Workflow

```text
Customer Support Ticket
          │
          ▼
Text Cleaning & Preprocessing
          │
          ▼
TF-IDF Vectorization
          │
          ▼
Train/Test Split
          │
          ▼
Multinomial Naive Bayes Model
          │
          ▼
Category Prediction
          │
          ▼
Priority Assignment
```

---

## 🤖 Machine Learning Model

### Text Preprocessing

- Convert text to lowercase
- Remove special characters
- Clean ticket descriptions

### Feature Extraction

The cleaned ticket descriptions are converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

### Classification Model

A **Multinomial Naive Bayes** classifier is trained to predict the appropriate support category for unseen customer tickets.

---

## 🚨 Priority Assignment

Since the dataset does not include priority labels, a simple rule-based priority system is used.

### 🔴 High Priority

Examples:

- urgent
- critical
- server down
- payment failed
- crash
- cannot login

### 🟡 Medium Priority

Examples:

- issue
- warning
- slow
- delay
- problem

### 🟢 Low Priority

General requests that do not contain urgent keywords.

---

## 📊 Model Evaluation

The model was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

### Results

| Metric | Score |
|---------|------:|
| Accuracy | **73.13%** |
| Precision | **(Your weighted precision)** |
| Recall | **(Your weighted recall)** |
| F1-Score | **(Your weighted F1-score)** |

---

## 💡 Business Value

This solution helps organizations by:

- Automatically categorizing support tickets
- Reducing manual ticket routing
- Prioritizing urgent customer issues
- Improving response times
- Increasing support team productivity
- Enhancing customer satisfaction

---

## 📸 Project Screenshots

### Confusion Matrix

_Add screenshot here_

### Model Performance

_Add screenshot here_

### Streamlit Application

_Add screenshot here_

---

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Support-Ticket-Classification-and-Prioritization.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook

```bash
jupyter notebook support_ticket.ipynb
```

### 4. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🖥️ Sample Prediction

### Input

```text
My laptop crashes every time I start Windows.
```

### Output

```text
Category : Hardware
Priority : High
```

---

## 📈 Future Improvements

- Deploy using Streamlit Community Cloud
- Train transformer-based models (BERT/RoBERTa)
- Learn priority directly from labeled datasets
- Integrate with real-time helpdesk systems
- Add confidence scores for predictions

---

## 📁 Repository Structure

```text
Support-Ticket-Classification-and-Prioritization/
│
├── app.py
├── support_ticket.ipynb
├── all_tickets_processed_improved_v3.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 👨‍💻 Author

**Abel George**

Machine Learning Enthusiast | B.Tech Computer Science

Developed as part of the **Future Interns Machine Learning Internship**.

---

## ⭐ If you found this project useful, consider giving it a star!
