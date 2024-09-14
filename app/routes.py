from flask import render_template, request, jsonify
import pandas as pd
import numpy as np
import os
from app import app

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define SNPs and their weights based on scientific research
snp_weights = {
    'rs429358': 1.35,   # APOE-e4, increases risk
    'rs7412': -0.86,    # APOE-e2, decreases risk
    'rs6656401': 0.25,  # CR1 gene, increases risk
    'rs9331896': 0.2,   # CLU gene, increases risk
    'rs6733839': 0.3,   # BIN1 gene, increases risk
    'rs10948363': 0.15, # CD2AP gene, increases risk
    'rs10792832': 0.22, # PICALM gene, increases risk
    'rs3851179': 0.17,  # PICALM gene variant, increases risk
    'rs11218343': 0.29, # SORL1 gene, increases risk
    'rs3865444': 0.14,  # CD33 gene, increases risk
}

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting Alzheimer's risk from the uploaded file
@app.route('/predict', methods=['POST'])
def predict():
    if 'dna_file' not in request.files:
        return jsonify({'error': 'No file part in the request'})
    
    file = request.files['dna_file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    if file:
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Load the patient's DNA data from the uploaded CSV file
        try:
            patient_data = pd.read_csv(file_path)
        except Exception as e:
            return jsonify({'error': f"Error loading patient data: {str(e)}"})
        
        # Calculate Polygenic Risk Score (PRS) based on SNPs
        def calculate_prs(patient_data, snp_weights):
            prs_score = 0
            for snp, weight in snp_weights.items():
                if snp in patient_data.columns:
                    genotype = patient_data[snp].values[0]
                    prs_score += genotype * weight
            return prs_score
        
        # Calculate the PRS
        prs = calculate_prs(patient_data, snp_weights)
        
        # Convert PRS to a percentage risk score using a logistic function (example)
        risk_percentage = 1 / (1 + np.exp(-prs)) * 100

        return jsonify({'risk': f"{risk_percentage:.2f}%"})

    return jsonify({'error': 'File processing failed.'})
