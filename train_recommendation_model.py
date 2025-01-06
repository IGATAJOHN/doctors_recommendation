import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle

# Load data
doctors = pd.read_csv("data/doctors.csv")
interactions = pd.read_csv("data/interactions.csv")

# Pivot the interactions for a collaborative filtering approach
interaction_matrix = interactions.pivot_table(index='user_id', columns='doctor_id', values='rating').fillna(0)

# Train a recommendation model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(interaction_matrix)

# Save the model
with open("models/recommendation_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")
