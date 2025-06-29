import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Create a synthetic dataset
data = {
    'name': [f'Prisoner {i}' for i in range(1, 101)],
    'year': np.random.choice(['2021', '2022', '2023'], 100),
    'period_of_detention': np.random.randint(1, 365, 100),
    'male': np.random.choice([0, 1], 100),
    'female': np.random.choice([0, 1], 100),
    'total': np.random.randint(1, 10, 100),
}

# Generating random eligibility for bail (you can modify the logic here)
data['eligible_for_bail'] = np.where(
    (data['period_of_detention'] <= 30) & (data['male'] == 1), 1,
    np.where((data['period_of_detention'] <= 60) & (data['female'] == 1), 1, 0)
)

# Create DataFrame
df = pd.DataFrame(data)

# Save the synthetic dataset to a CSV file
df.to_csv('undertrial_prisoners.csv', index=False)

# Display the first few rows of the dataset
print("Synthetic Dataset Created:")
print(df.head())

# Step 2: Load the dataset
data = pd.read_csv('undertrial_prisoners.csv')

# Preprocessing
data = data.drop(['name'], axis=1)  # Drop name column as it’s not needed for prediction

# Encode the 'year' column
label_encoder = LabelEncoder()
data['year'] = label_encoder.fit_transform(data['year'])

# Split features and target variable
X = data.drop('eligible_for_bail', axis=1)  # Features
y = data['eligible_for_bail']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model (using Random Forest Classifier as an example)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Example of making a prediction for a new undertrial prisoner
new_prisoner = np.array([[2023, 30, 1, 0, 1]])  # Example input: [year, period_of_detention, male, female, total]
new_prisoner = scaler.transform(new_prisoner)  # Don't forget to scale
prediction = model.predict(new_prisoner)

print("\nPrediction for New Prisoner:")
print("Eligible for bail" if prediction[0] == 1 else "Not eligible for bail")
