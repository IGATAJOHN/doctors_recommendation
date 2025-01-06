# Doctor Recommendation System

This project is an AI-powered doctor recommendation system built with Flask, pandas, and scikit-learn. It allows users to receive personalized doctor recommendations based on their preferences and interaction history.

## Features

- **Doctor Data**: Contains details about doctors, including specialization, location, rating, and consultation fee.
- **User Data**: Stores user preferences and interaction history.
- **Recommendation Engine**: Provides doctor recommendations using a collaborative filtering approach.
- **RESTful API**: Exposes endpoints for recommendations.

---

## Project Structure

```
quantum-doctor/
├── app.py               # Flask API
├── data/
│   ├── doctors.csv      # Dummy doctor data
│   ├── users.csv        # Dummy user data
│   └── interactions.csv # Dummy user-doctor interactions
├── models/
│   └── recommendation_model.pkl  # Saved recommendation model
├── templates/           # HTML templates (if any)
├── static/              # Static files (CSS/JS/images)
└── requirements.txt     # List of dependencies
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IGATAJOHN/doctor-recommendation-system.git
   cd doctor-recommendation-system
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare dummy data:**
   Ensure the `doctors.csv`, `users.csv`, and `interactions.csv` files are present in the `data/` directory. Use the provided example files or create your own.

5. **Train the recommendation model:**
   ```bash
   python train_recommendation_model.py
   ```

6. **Run the Flask app:**
   ```bash
   python app.py
   ```

7. **Access the API:**
   Open your browser or use a tool like Postman to access the API at `http://127.0.0.1:5000`.

---

## API Endpoints

### `/recommend`
- **Method**: `GET`
- **Description**: Provides doctor recommendations for a given user.
- **Parameters**:
  - `user_id` (int): The ID of the user.
- **Response**:
  ```json
  {
    "recommendations": [
      {
        "id": 1,
        "name": "Maryann Yusuf",
        "specialization": "Oncologist",
        "location": "Lagos",
        "rating": 4.8,
        "consultation_fee": 15000
      },
      {
        "id": 4,
        "name": "John Smith",
        "specialization": "Cardiologist",
        "location": "Abuja",
        "rating": 4.6,
        "consultation_fee": 30000
      }
    ]
  }
  ```

---

## Example Data

### `doctors.csv`
```csv
id,name,specialization,location,rating,consultation_fee
1,Maryann Yusuf,Oncologist,Lagos,4.8,15000
2,Monday Morgan,Gynecologist,Abuja,4.7,25000
3,Jane Doe,Dentist,Lagos,4.5,20000
4,John Smith,Cardiologist,Abuja,4.6,30000
```

### `users.csv`
```csv
id,name,preferences
1,John Doe,{"specialization": "Oncologist", "location": "Lagos"}
2,Jane Smith,{"specialization": "Dentist", "location": "Abuja"}
```

### `interactions.csv`
```csv
user_id,doctor_id,rating
1,1,5
2,3,4
1,4,3
```

---

## Future Enhancements

- Integrate with real doctor and user data once the platform is officially launched.
- Add additional filtering options (e.g., budget, online consultation availability).
- Enhance the recommendation engine using deep learning approaches.
- Build a frontend UI for better user interaction.

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any inquiries or support, please contact:
- **Name**: Igata John
- **Email**: info@qit.com.ng
- **Website**: [Quantum Innovative Tech Solutions Ltd](https://www.qit.com.ng)
