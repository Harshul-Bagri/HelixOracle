# GenePredict: Neurological Disease Risk Prediction

**GenePredict** is a web-based application designed to predict the risk of neurological diseases, such as Alzheimer's, using genetic data. This project leverages a machine learning model to calculate a Polygenic Risk Score (PRS) from DNA data and presents the results through a user-friendly interface.

## Features

- **Upload Genetic Data:** Users can upload a CSV file containing genetic data to predict their risk of neurological diseases.
- **Risk Calculation:** The application calculates the risk percentage based on SNPs (Single Nucleotide Polymorphisms) and their weights.
- **Results Display:** The risk percentage is displayed in a table along with an analysis summary.
- **Graphical Representation:** A bar chart compares the user's risk with the average risk of a normal person.
- **Future-Proof:** The system is designed to be extendable for other neurological diseases, such as Huntington's disease.

## Project Structure

- **`routes.py`**: Contains Flask routes for rendering pages and processing file uploads.
- **`templates/index.html`**: HTML template for the user interface.
- **`static/css/styles.css`**: CSS file for styling the web page.
- **`uploads/`**: Directory where uploaded files are temporarily stored.


### Prerequisites

- Python 3.x
- Flask
- Pandas
- NumPy
- Chart.js (for graphical representation)
  
Collaborators:

  [Harshul-Bagri](https://github.com/Harshul-Bagri)
  
  [Harsh12bhardwaj](https://github.com/Harsh12bhardwaj)

  [Subhankar-Bose2005](https://github.com/Subhankar-Bose2005)
