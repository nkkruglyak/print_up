import requests
import os

path_to_file = os.path.abspath('./test_im/1.JPG')
files = {'file': open(path_to_file, 'rb')}


def post_uploads(files):
    response = requests.post('http://127.0.0.1:5000/uploads', files = files)
    path = os.path.abspath('./test_im/1_new.JPG')
    print (response.headers)
    print (response.content )
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)


def post_exif(files):
    response = requests.post('http://127.0.0.1:5000/exif', files = files)
    path = os.path.abspath('./test_im/1.txt')
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)

    print (response)

post_uploads(files)
post_exif(files)

