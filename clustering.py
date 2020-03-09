import pandas as py
from sklearn import preprocessing
import matplotlib.pyplot as mat
#
# data = py.read_csv(r'C:\Users\MAYUR\Desktop\Accidents0515.csv',nrows=10000)
#
# mat.scatter(data.Longitude,data.Latitude)
# mat.show()


data = py.read_csv(r'C:\Users\MAYUR\Downloads\new-york-city-airbnb-open-data\AB_NYC_2019.csv');


# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# # Encode labels in column 'species'.
# data['host_name'] = label_encoder.fit_transform(data['host_name'])
#
# data['neighbourhood_group'] = label_encoder.fit_transform(data['neighbourhood_group'])

data['neighbourhood'] = label_encoder.fit_transform(data['neighbourhood'])

data['room_type'] = label_encoder.fit_transform(data['room_type'])
print(data.columns)
data=data[:100]
print(data)
data.info()







