# CodelerateHackathon
This repository was created for Codelerate_Hackathon orgnanized by Coimbatore Institute of Technology(CIT). 

# 🧠 Article Recommendation System using Machine Learning

Welcome to our project — **Article Recommendation System**, built by **Team Inferno** alias **Logic-Loom**! 🔥  
This ML-powered web application recommends article titles based on user input — specifically, an article they've already read. The system leverages **TF-IDF vectorization** and **Cosine Similarity** through the **Nearest Neighbors algorithm**.

## 🚀 Project Overview

Given a raw, unstructured dataset, we aimed to develop a recommender system that:

- Understands user intent based on article title
- Suggests the top 5 similar articles instantly
- Delivers an elegant and responsive user experience
- Deploys the model using Flask for real-time interaction

---

## 🛠️ Workflow / Methodology

### 1️⃣ Understanding the Dataset
- Inspected structure (categorical vs numerical data)
- Analyzed column types and relationships
- Identified missing values and potential inconsistencies

### 2️⃣ Data Cleaning & Preprocessing
- Handled null values using interpolation and imputation
- Removed duplicates and managed outliers
- Standardized text fields
- Created a `clean_title` column
- Applied **TF-IDF vectorization**

### 3️⃣ Exploratory Data Analysis (EDA)
- Summarized distributions (mean, median, std)
- Analyzed feature correlations
- Detected imbalances in the data
- Visualized data trends using histograms and heatmaps

### 4️⃣ Data Visualization & Insight Extraction
- Used **matplotlib**, **seaborn**, and **pandas** to draw insights
- Created plots like boxplots, bar charts, and pair plots
- Identified key patterns in user interests and article structure

### 5️⃣ Feature Engineering
- Selected meaningful features for input
- Scaled features for consistency
- Derived useful transformations from existing data

### 6️⃣ Efficient Use of Data
- Removed unused and redundant fields
- Justified all preprocessing actions via statistical checks

### 7️⃣ Final Report & Documentation
- Well-commented Jupyter Notebook with full processing flow
- Explained model logic, output structure, and performance
- Project demo deployed via Flask server

---

## 🤖 ML Model Used

- **TF-IDF Vectorizer** for transforming article titles into feature vectors
- **Nearest Neighbors (Cosine Similarity)** to suggest top 5 similar articles
- Saved model components in a `.pkl` file for real-time deployment

---

## 🧪 Output Example

> **User Input**: *"Understanding Cloud Computing"*  
> **Recommended Articles**:
> - Basics of Cloud Architecture  
> - How Cloud Platforms Work  
> - Cloud Security Essentials  
> - SaaS vs PaaS: What's the Difference?  
> - Real-world Use Cases of Cloud AI  

---

## 🌐 Deployment

The application is deployed using **Flask**, where:
- The input is accepted via a simple HTML form
- Backend processes user input and runs the recommender
- The top 5 articles are returned and displayed beautifully

---

## 💡 Technologies Used

- Python (pandas, sklearn, numpy, rapidfuzz)
- Flask
- HTML5 / CSS3 (Responsive Design)
- Jupyter Notebook

---

## 👨‍👩‍👧 Team Inferno

| Name                   | Role                              |
|------------------------|-----------------------------------|
| 🔥 Elango-Kannan-00           | Dataset Cleaning & Model Training |
| 🎨 Dhanushiya-srini | Frontend Design (HTML + CSS)      |
| ⚙️ DharshiniSaravanan-2006  | Flask Deployment & Integration    |

---

## 🙌 Acknowledgements

If you'd like to test the project or want to collaborate, feel free to fork or open an issue!  
⭐ Star the repository if you find it useful!

---

## 📌 Tags  
#AI #MachineLearning #RecommendationSystem #Flask #TeamInferno #TFIDF #CosineSimilarity #ProjectShowcase


