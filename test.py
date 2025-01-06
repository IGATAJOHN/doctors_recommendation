import requests

# Replace with your actual user ID
sample_user_id = 1

# URL of your recommendation endpoint
url = f"http://127.0.0.1:5001/recommend?user_id={sample_user_id}"

try:
    response = requests.get(url)
    response.raise_for_status()
    recommendations = response.json()

    if "error" in recommendations:
        print(f"Error: {recommendations['error']}")
    else:
        print("Recommended Doctors:")
        for doctor in recommendations["recommendations"]:
            # Print the dictionary for debugging
            print(doctor)
            print(f"ID: {doctor['id']}, Name: {doctor['name']}, Specialty: {doctor['specialization']}, Location: {doctor['location']}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
