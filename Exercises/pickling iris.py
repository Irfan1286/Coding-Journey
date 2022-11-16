# use requests and pickle module
import requests
import pickle

req = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text

list_of_req = [item.split(',') for item in req.split('\n') if len(item) != 0]

with open('pickling iris.pkl', 'wb') as file:
    pickle.dump(list_of_req, file)

with open('pickling iris.pkl', 'rb') as file:
    data = pickle.load(file)
    print(data)