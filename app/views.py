from flask import render_template, request
from app import app, model

#              it should be diabetic
#patient = [[5, 150, 33.7, 50, 150, 74, 0.5, 53]]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        pregnancies = int(request.form['Pregnancies'])
        glucose = int(request.form['Glucose'])
        bloodPressure = float(request.form['BloodPressure'])
        skinThickness = int(request.form['SkinThickness'])
        insulin = int(request.form['Insulin'])
        bmi = int(request.form['bmi'])
        diabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        age = int(request.form['Age'])
        
        patient = [[
            pregnancies,
            glucose,
            bloodPressure,
            skinThickness,
            insulin,
            bmi,
            diabetesPedigreeFunction,
            age
        ]]
        
        result = model.predict(patient)
        
        if result == 1:
            message = 'You have diabetes'
        else:
            message = 'You do NOT have diabetes'
         
        return render_template('index.html', message=message)
    return render_template('index.html')