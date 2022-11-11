
import requests

R = requests.get('https://financialmodelingprep.com/api/v3/changelog?apikey=YOUR_API_KEY')  # Gets source code from url
print(R.text)   # It prints as text

image = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/486px-Python_logo_and_wordmark.svg.png?20210516005643')
# print(image.content)  # This will give the content of image in bytes

with open('python.png', 'wb') as f:  # wb means write bytes
    f.write(image.content)  # These two lines will download the image !

print(image.status_code)    # 200's are successes, 300's are Redirects and 400's are client errors and 500's are server errors

print(image.ok)      # anything below 400 will be returned True

print(image.headers)    # Will provide useful info of the website

