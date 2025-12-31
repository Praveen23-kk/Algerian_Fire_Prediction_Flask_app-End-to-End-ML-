from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open("model/ridge.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

EXPECTED_FEATURES = scaler.n_features_in_

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            features = [
                float(request.form["Temperature"]),
                float(request.form["RH"]),
                float(request.form["Ws"]),
                float(request.form["Rain"]),
                float(request.form["FFMC"]),
                float(request.form["DMC"]),
                float(request.form["DC"]),
                float(request.form["ISI"]),
                float(request.form["Region"])   # FIXED: 9th feature
            ]

            if len(features) != EXPECTED_FEATURES:
                raise ValueError(
                    f"Expected {EXPECTED_FEATURES} features, got {len(features)}"
                )

            scaled_features = scaler.transform([features])
            prediction = round(model.predict(scaled_features)[0], 2)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run()


