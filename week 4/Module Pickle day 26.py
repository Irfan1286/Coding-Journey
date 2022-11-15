
import pickle       # commonly used to pack objects into a .pkl file

# THIS IS PICKILING

object = ['jar', 'Mouse', 'BMW', 'ferrari']
file_name = 'Pickle module.pkl'

# writing- serialization
with open('Pickle module.pkl', 'wb') as file:
    content = pickle.dump(object, file)       # First is the object and second is the file where file is opened!

# Reading - de-serialization
with open('Pickle module.pkl', 'rb') as file:   # .pkl is a binary file so rb reads binary
    print(pickle.load(file))        # Never unpickle data from UNTRUSTED sources

# pickle. load unpickles byte like object