from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained logistic regression model
model = joblib.load('trained_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return "No file selected"
        
        # Read the uploaded file into a DataFrame
        data = pd.read_excel('pills.xlsx')  # For Excel files: pd.read_excel(file)

        # Perform prediction using the trained model
        predictions = model.predict(data)

        # Process the predictions as needed and return the results
        return str(predictions)

if __name__ == '__main__':
    app.run(debug=True)
