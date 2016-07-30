# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, jsonify, make_response,send_file,Response
from werkzeug.utils import secure_filename
from handl_image import HandlImage
from path_file import del_files

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/exif', methods=['GET','POST'])
def get_exif():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename:
            filename = secure_filename(file.filename)

            path = os.path.abspath('./server_im')
            full_path = os.path.join(path, filename)

            file.save(full_path)
            im = HandlImage(full_path)
            exif_json = im.get_exif_data()
            resp = Response(response=exif_json,
                            status=200,
                            mimetype="application/json")
            return resp


@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename:
            filename = file.filename
            path = os.path.abspath('./server_im')
            full_path = os.path.join(path, filename)
            down_path = os.path.join(path, 'new.jpg')

            file.save(full_path)
            im = HandlImage(full_path)
            im.change_size(down_path, (64, 64))

            return send_file(down_path, mimetype='image/jpeg')

    return render_template('404.html')


if __name__ == '__main__':
    app.run()
    del_files('./server_im')

