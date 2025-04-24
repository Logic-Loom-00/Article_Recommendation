from flask import Flask, render_template, request
import pickle

# Load the model, tfidf, and dataframe
with open("recommendation_model_v2.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data['model']
tfidf = model_data['tfidf']
df = model_data['df']

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        user_input = request.form["article_title"]
        user_vec = tfidf.transform([user_input])
        
        # Get top 6 neighbors: 1st is usually the input itself
        distances, indices = model.kneighbors(user_vec, n_neighbors=6)
        
        # Skip the first one (assumed to be the input itself)
        recommended_indices = indices[0][1:6]

        # Fetch recommended article titles
        recommendations = df.iloc[recommended_indices]['title'].tolist()

    return render_template("index.html", recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
