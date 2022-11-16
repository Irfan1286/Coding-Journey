# use requests and pickle module
import requests
import pickle

req = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text

list_of_req = [item.split(',') for item in req.split('\n') if len(item) != 0]

with open('pickling iris.pkl', 'wb') as file:
    for items in list_of_req:
        pickle.dump(items, file)

with open('pickling iris.pkl', 'rb') as file:
    print(pickle.load(file))
