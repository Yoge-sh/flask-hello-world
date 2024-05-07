from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name, age, sex,location, foodpref, wc, activity, history = "Yogesh",23, "male", "India", 3, 70, 3, 2
    results = {
        "Patient Name" : name,
        "Age": age,
        "Sex": sex,
        "Location" : location,
        "Food Preference" : foodpref,
        "Waist Circumference": wc,
        "Activity Level": 2,
        "Diabetes History": 2,
        "Total Score": 30,
        "Prediction": "high risk"
    }
    return results

@app.route('/about')
def about():
    return 'About'
