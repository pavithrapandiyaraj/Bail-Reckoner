import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Create a Flask app
app = Flask(__name__)

# Load the dataset and preprocess
data = {
    'name': [f'Prisoner {i}' for i in range(1, 101)],
    'year': np.random.choice(['2021', '2022', '2023'], 100),
    'period_of_detention': np.random.randint(1, 365, 100),
    'male': np.random.choice([0, 1], 100),
    'female': np.random.choice([0, 1], 100),
    'total': np.random.randint(1, 10, 100),
}

data['eligible_for_bail'] = np.where(
    (data['period_of_detention'] <= 30) & (data['male'] == 1), 1,
    np.where((data['period_of_detention'] <= 60) & (data['female'] == 1), 1, 0)
)

df = pd.DataFrame(data)

# Preprocess the data
df = df.drop(['name'], axis=1)
label_encoder = LabelEncoder()
df['year'] = label_encoder.fit_transform(df['year'])
X = df.drop('eligible_for_bail', axis=1)
y = df['eligible_for_bail']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    year = request.form['year']
    period_of_detention = int(request.form['period_of_detention'])
    male = int(request.form['male'])
    female = int(request.form['female'])
    total = int(request.form['total'])

    # Prepare the input for prediction
    input_data = np.array([[year, period_of_detention, male, female, total]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)

    # Return the result
    result = "Eligible for bail" if prediction[0] == 1 else "Not eligible for bail"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
