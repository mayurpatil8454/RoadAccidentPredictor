from flask import Flask, render_template ,url_for,request,redirect,session,send_file
import matplotlib as mat
import urllib.parse
import pandas as py
import joblib as jobs
from matplotlib  import pyplot
import io
import os
import base64
app = Flask(__name__)
app.secret_key = 'loginner'

py.options.mode.chained_assignment = None
LoginData = py.read_csv(r"Login.csv")
cities = ["Bhandup", "Mumbai", "Visakhapatnam", "Ahmedabad", "Delhi", "Bangalore", "Pune", "Nagpur", "Panvel",
          "Vadodara",
          "Indore", "Ulhasnagar", "Bhopal", "Kolkata", "Kanpur", "New Delhi", "Kalyan", "Rajkot", "Ghaziabad",
          "Chennai",
          "Meerut", "Agra", "Jaipur", "Jabalpur"]
Weather = ["Spring", "Summer", "Monsoon", "Winter"]
Sex = ["Male", "Female"]
Road_Types = ["National Highways", "State Highways", "PWD Roads", " Rural Roads", "Urban Roads", "Project Roads"]
Vehicles = ["Bike","Car","Bus","Truck","Rickshaw"]

@app.route('/', methods =['GET','POST'])
def Login():
    if request.method == 'POST':
        LoginData = py.read_csv(r"Login.csv")
        Username = request.form['Username'];
        password = request.form['password'];
        print(Username)
        print(password)
        for row in LoginData.index:
            if LoginData['Username'][row] == Username and LoginData['Password'][row] == password:
                session['LoginFlag'] = True;
                return render_template('index.html')
        return render_template('login.html',error="Invalid UserID and Password")

    return render_template('login.html')


@app.route('/SignUp', methods =['GET','POST'])
def SignUp():
    if request.method == 'POST':
        Username = request.form['Username'];
        password = request.form['password'];
        flag = True
        for row in LoginData.index:
            if LoginData['Username'][row] == Username:
                return render_template('SignUp.html',error="UserId already exist please try again with different UserId")
        LoginData1 = LoginData.append({'Username' :  Username, 'Password' : password} , ignore_index=True)
        LoginData1.to_csv("Login.csv", index=False)
        return render_template('login.html')
    return render_template('SignUp.html')


@app.route('/SignOut', methods =['GET','POST'])
def SignOut():
    print("signout called")
    if not session.get('LoginFlag'):
        return render_template('login.html')
    else:
        session['LoginFlag'] = False
    return render_template('login.html')

@app.route('/DownloadFile', methods =['GET'])
def Download():
    path = "/Login.csv"
    return send_file(path, as_attachment=True)

@app.route('/Index', methods =['GET','POST'])
def home():
    if session['LoginFlag'] == True:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/Stat', methods =['GET','POST'])
def Stat():
    if session['LoginFlag'] == True:

        return render_template('Stat.html')
    else:
        return render_template('login.html')


@app.route('/Predictor', methods =['GET','POST'])
def Predictor():
    if session['LoginFlag'] ==True:
       if request.method == 'POST':
            prediction = Predict(request)
            Accident_issues = [prediction,100-prediction]
            activities = ['Not Safe','Safe']
            pyplot.pie(Accident_issues, labels=activities, startangle=90, autopct='%.1f%%')

            img = io.BytesIO()  # create the buffer
            pyplot.savefig(img, format='png')  # save figure to the buffer
            img.seek(0)  # rewind your buffer
            plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode())  # base64 encode & URL-escape
            return render_template('Predictor.html',cities =cities,Weather=Weather,Sex=Sex,Road_Types=Road_Types,Vehicles=Vehicles,PredictionGraph = plot_data)
       else:
            return render_template('Predictor.html',cities =cities,Weather=Weather,Sex=Sex,Road_Types=Road_Types,Vehicles=Vehicles)
    else:
        return render_template('login.html')


def Predict(x):
    vehicletype = Vehicles.index(x.form['VehicleType']);
    cityname = cities.index(x.form['city']);
    Weather1 = Weather.index(x.form['Weather']);
    RoadType = Road_Types.index(x.form['RoadType']);
    Sex1 = Sex.index(x.form['Sex']);
    Age = x.form['Age'];
    Speedlimit = x.form['Speedlimit'];
    model_clone = jobs.load('RoadAccidentPredictor.pkl')
    obj = {"VehicleType": [vehicletype],
           "Road_Type": [RoadType],
           "Speed_limit": [Speedlimit],
           "Light_Conditions": [Weather1],
           "Weather_Conditions": [Weather1],
           "Road_Surface_Conditions": [Weather1],
           "Urban_or_Rural_Area": [1],
           "City": [cityname],
           "Sex": [Sex1],
           "Age": [Age]
           }
    datapoint = py.DataFrame(obj)
    predict =model_clone.predict(datapoint)
    print(predict)
    predict = predict * 10
    if predict <= 50:
        predict = 25
    elif predict <= 70:
        predict =45
    elif predict <= 120:
        predict = 60
    elif predict <= 160:
        predict =65
    else:predict =70
    print(predict);
    return predict

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
