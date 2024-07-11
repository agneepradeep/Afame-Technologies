from flask import Flask, request, render_template
import joblib
import json
import numpy as np

app = Flask(__name__)

# Load the trained model and category mapping
random_forest_model = joblib.load('model/random_forest_model.pkl')
with open('category_mapping.json', 'r') as file:
    category_mapping = json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    if request.method == 'POST':
        # Get form data
        amt = float(request.form['amt'])
        gender_encoded = int(request.form['gender_encoded'])
        hour_of_day = int(request.form['hour_of_day'])
        category = request.form['category']
        age = int(request.form['age'])
        distance = float(request.form['distance'])

        # Convert category to encoded value
        category_encoded = category_mapping.get(category, -1)

        # Ensure category is valid
        if category_encoded == -1:
            return render_template('index.html', categories=category_mapping.keys(), prediction_text='Invalid category')

        # Prepare the input data
        input_data = np.array([[amt, hour_of_day, category_encoded, age, distance, gender_encoded]])

        # Make prediction
        prediction = random_forest_model.predict(input_data)
        prediction_text = 'Fraudulent Transaction' if prediction[0] == 1 else 'Legitimate Transaction'

    return render_template('index.html', categories=category_mapping.keys(), prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
