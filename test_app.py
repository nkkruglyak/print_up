import unittest
from app import app
from handl_image import HandlImage
import os
import unittest
import json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


    def client_upload(self, path_to_dir, name_file, name_new_file):
        """ Send post request to server with photo and save response photo """
        path_to_file = os.path.join(path_to_dir,name_file)
        path_to_new_file = os.path.join(path_to_dir, name_new_file)
        files = {'file': open(path_to_file, 'rb')}
        response = self.app.post('/uploads', content_type='multipart/form-data', data=dict(file=files))
        image = response.data
        if response.status_code == 200:
            with open(path_to_new_file, 'wb') as f:
                f.write(image)
        return path_to_new_file


    def client_exif(self, path_to_dir, name_file):
        """ Send post request to server with photo and return exif as json """
        path_to_file = os.path.join(path_to_dir, name_file)
        files = {'file': open(path_to_file, 'rb')}
        response = self.app.post('/exif', content_type='multipart/form-data', data=dict(file=files))
        exif = response.data.decode('ascii')
        return exif


    def plain_compression(self,path_to_dir, name_file, name_new_file):
        path_to_file = os.path.join(path_to_dir,name_file)
        path_to_new_file = os.path.join(path_to_dir, name_new_file)
        im = HandlImage(path_to_file)
        im.change_size(path_to_new_file, (64, 64))
        return path_to_new_file



    def test_uploads(self):
        """must be file with name_file in ./test_im
        """
        path_to_dir = os.path.abspath('./test_im')
        name_file = '2.JPG'
        name_new_client_file = 'new.JPG'
        name_new_compression_file = 'new_new.JPG'
        f1 = open(self.client_upload(path_to_dir, name_file, name_new_client_file),'rb')
        f2 = open(self.plain_compression(path_to_dir,name_file, name_new_compression_file), 'rb')
        self.assertEqual(f1.read(), f2.read())


    def test_exif(self):
        """must be file with name_file in ./test_im
        """
        path_to_dir = os.path.abspath('./test_im')
        name_file = '1.JPG'
        exif = self.client_exif(path_to_dir,name_file)
        # check to validate json
        json.loads(exif)




if __name__ == '__main__':
    unittest.main()







