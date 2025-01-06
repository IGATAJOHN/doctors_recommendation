from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load data and model
doctors = pd.read_csv("data/doctors.csv")
with open("models/recommendation_model.pkl", "rb") as f:
    recommendation_model = pickle.load(f)

# Dummy user-doctor interaction matrix
interactions = pd.read_csv("data/interactions.csv")
interaction_matrix = interactions.pivot_table(index='user_id', columns='doctor_id', values='rating').fillna(0)

@app.route("/recommend", methods=["GET"])
def recommend_doctors():
    user_id = int(request.args.get("user_id"))

    # Get the user's interaction vector
    if user_id not in interaction_matrix.index:
        return jsonify({"error": "User not found"}), 404

    user_vector = interaction_matrix.loc[user_id].values.reshape(1, -1)

    # Get recommendations
    distances, indices = recommendation_model.kneighbors(user_vector, n_neighbors=1)
    recommended_ids = interaction_matrix.columns[indices.flatten()].tolist()

    # Fetch doctor details
    recommendations = doctors[doctors["id"].isin(recommended_ids)].to_dict(orient="records")
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
