# CodelerateHackathon
This repository was created for Codelerate_Hackathon orgnanized by Coimbatore Institute of Technology(CIT). 

# Article Recommendation System using Machine Learning

Welcome to our project — **Article Recommendation System**, built by **Team Inferno** alias **Logic-Loom**!   
This ML-powered web application recommends article titles based on user input — specifically, an article they've already read. The system leverages **TF-IDF vectorization** and **Cosine Similarity** through the **Nearest Neighbors algorithm**.

## Project Overview

Given a raw, unstructured dataset, we aimed to develop a recommender system that:

- Understands user intent based on article title
- Suggests the top 5 similar articles instantly
- Delivers an elegant and responsive user experience
- Deploys the model using Flask for real-time interaction

---

## Workflow / Methodology

### 1️⃣ Understanding the Dataset
### 2️⃣ Data Cleaning & Preprocessing
### 3️⃣ Exploratory Data Analysis (EDA)
### 4️⃣ Data Visualization 
### 5️⃣ Training and Testing 
---

## ML Model Used

- **TF-IDF Vectorizer** for transforming article titles into feature vectors
- **Nearest Neighbors (Cosine Similarity)** to suggest top 5 similar articles
- Saved model components in a `.pkl` file for real-time deployment

---

## Output Example

> **User Input**: *"Understanding Cloud Computing"*  
> **Recommended Articles**:
> - Basics of Cloud Architecture  
> - How Cloud Platforms Work  
> - Cloud Security Essentials  
> - SaaS vs PaaS: What's the Difference?  
> - Real-world Use Cases of Cloud AI  

---

## Deployment

The application is deployed using **Flask**, where:
- The input is accepted via a simple HTML form
- Backend processes user input and runs the recommender
- The top 5 articles are returned and displayed beautifully

---

## Technologies Used

- Python (pandas, sklearn, numpy)
- Flask
- HTML5 / CSS3 (Responsive Design)
- Jupyter Notebook

---

## Team Logic-Loom

| Name                   | Role                              |
|------------------------|-----------------------------------|
| Elango-Kannan-00           | Dataset Cleaning & Model Training |
| Dhanushiya-srini | Frontend Design (HTML + CSS)      |
| DharshiniSaravanan-2006  | Flask Deployment & Integration    |

---

## Acknowledgements

If you'd like to test the project or want to collaborate, feel free to fork or open an issue!  
⭐ Star the repository if you find it useful!

---


