import pandas as py
import matplotlib as mat
import  seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib as jobs
AccidentData = py.read_csv(r"C:\Users\MAYUR\PycharmProjects\Pythontutorials\Newdataset.csv")
y = AccidentData['City']
X = AccidentData.drop('City', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
model=LogisticRegression();
model.fit(X_train , y_train)
pred = model.predict(X_test)
print(accuracy_score(y_test,pred))
#
jobs.dump(model, 'RoadAccidentPredictor.pkl', compress=9)
model_clone = jobs.load('RoadAccidentPredictor.pkl')
print(type(X_test))
pred1 = model_clone.predict(X_test)
print(accuracy_score(y_test,pred1))
obj = {"VehicleType": [5],
       "Road_Type": [9],
       "Speed_limit":[50],
       "Light_Conditions":[7],
       "Weather_Conditions":[9],
       "Road_Surface_Conditions":[4],
       "Urban_or_Rural_Area":[1],
       "City":[24],
       "Sex":[0],
       "Age":[49]
       }
datapoint = py.DataFrame(obj)
predict = 7 if model_clone.predict(datapoint) >= 7 else model_clone.predict(datapoint)
print(predict)
int(predict * 10);
#
# sns.countplot(x='Speed_limit',data=AccidentData)
# mat.pyplot.show()
import csv
fields=['first','second','third']
with open(r'Login.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
# sns.countplot(x='VehicleType' , data=AccidentData )
# mat.pyplot.show()
# sns.countplot(x='City' , data=AccidentData , hue='Sex')
# mat.pyplot.show()
# Accident_issues = [166 , 126 , 116 , 92]
# activities = ['Pune', 'Mumbai' , 'Nashik' , 'Nagpur']
# mat.pyplot.pie(Accident_issues, labels=activities, startangle=90 ,autopct='%.1f%%')
# mat.pyplot.show()