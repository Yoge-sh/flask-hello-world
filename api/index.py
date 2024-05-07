from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    if request.method == 'GET':
        return "Hello G!"
    else:
        return "Not GET"
    
    # if request.method == 'POST':
    #     user_input = request.get_json()    
    #     name, age, sex,location, foodpref, wc, activity, history = user_input.values()
        
    #     results = {
    #         "Patient Name" : name,
    #         "Age": age,
    #         "Sex": sex,
    #         "Location" : location,
    #         "Food Preference" : foodpref,
    #         "Waist Circumference": wc,
    #         "Activity Level": 2,
    #         "Diabetes History": 2,
    #         "Total Score": 30,
    #         "Prediction": "high risk"
    #     }
    #     return results
    # return 'This endpoint expects a GET/POST request with user input data in JSON format.'

@app.route('/about')
def about():
    return 'About'
