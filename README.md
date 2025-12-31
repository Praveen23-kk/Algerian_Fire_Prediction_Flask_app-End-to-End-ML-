# 🔥 Algerian Forest Fire Predictor (FWI Prediction)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![ML Library](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview
This project is a machine learning web application designed to predict the **Fire Weather Index (FWI)** based on meteorological data collected from the Algerian forest regions.

The application utilizes a **Ridge Regression** model trained on the *Algerian Forest Fires Dataset*. It provides a user-friendly interface built with **Flask**, allowing users to input environmental parameters (such as temperature, humidity, and wind speed) to estimate the potential fire danger intensity.

---

## 📸 Sample Result
![App Screenshot](screenshot.png)

*Above: A preview of the web interface where users input weather data to receive an FWI prediction.*

---

## 📂 About the Dataset
[cite_start]The model is trained on the **Algerian Forest Fires Dataset**[cite: 2], which includes data from two regions in Algeria: the **Bejaia** region and the **Sidi Bel-Abbes** region.

### Features Used for Prediction
The model requires **9 input features** to generate a prediction, as defined in the training pipeline:

| Feature | Description |
| :--- | :--- |
| **Temperature** | Maximum temperature in noon (°C) |
| **RH** | Relative Humidity in % |
| **Ws** | Wind Speed in km/h |
| **Rain** | Total day rain in mm |
| **FFMC** | Fine Fuel Moisture Code (indicates ignition potential) |
| **DMC** | Duff Moisture Code (indicates fuel consumption in moderate soil layers) |
| **DC** | Drought Code (indicates fuel consumption in deep soil layers) |
| **ISI** | Initial Spread Index (velocity of fire spread) |
| **Region** | Binary Class (0 for Bejaia, 1 for Sidi Bel-Abbes) |

### Target Variable
* **FWI (Fire Weather Index):** A numerical rating of fire intensity. [cite_start]The dataset also contains a `Classes` column (fire/not fire), but this specific app predicts the continuous `FWI` value using Regression[cite: 2].

---

## 🛠️ Technical Architecture

### Tech Stack
* **Frontend:** HTML/CSS (rendered via Flask templates)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn (Ridge Regression), NumPy, Pandas
* [cite_start]**Deployment:** Gunicorn (ready for production) [cite: 1]

### Project Structure
```bash
├── model/
│   ├── ridge.pkl        # Trained Ridge Regression Model
│   └── scaler.pkl       # Standard Scaler for feature normalization
├── templates/
│   └── index.html       # Frontend UI for the form
├── Algerian_forest_fires_cleaned_dataset.csv  # Source data
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
