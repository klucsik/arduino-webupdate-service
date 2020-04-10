from flask import Flask, request, url_for
from config import Config
import os
app = Flask(__name__)


@app.route('/check')
def check_ver():
    name = request.args.get("name")
    installed_ver = request.args.get("ver")
    response = ""
    my_ver = ""
    binary_path =""
    dir_to_file = "bin/" + name
    dir_to_search = Config.STATIC + dir_to_file
    print(dir_to_search)
    for root, dirs, files in os.walk(dir_to_search):
        my_ver = files[0].split(".")[0]
        binary_path = url_for('static', filename=dir_to_file + "/" + files[0])
        print(binary_path)
    if installed_ver != my_ver:
        response = binary_path
    else:
        response = "update not needed"
    if response is not "":
        return response
    else:
        return "no name found", 404
