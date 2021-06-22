### imports
from flask import Flask, jsonify, request, render_template
#from waitress import serve
from groclient import *
import json


### setup Flask and GroClient
app = Flask(__name__)


@app.route('/groflaskapi/<data>', methods=['GET', 'POST'])
def groAPIConnection(data):
    headers = request.headers
    key = headers.get('API_KEY')
    requestAsJSON = json.loads(data)
    groMethod = requestAsJSON['gromethod']
    parameter = requestAsJSON['parameter']
    item_id = requestAsJSON['item_id']

    print(headers)
    print(read_text('key.txt'))
    if read_text('key.txt')==key:
        groReply = groAPI(groMethod, parameter, item_id)
        if request.method == 'POST':
            return jsonify(groReply)
        elif request.method == "GET":
            return "hi"
        else:
            return "hi"
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


def read_text(file):
    with open(file, 'r') as filename:
        filestring = filename.read().replace('\n', '')
    return filestring

#CALL TO GRO
def groAPI(method, parameter, data):
    gro_token = read_text('grokey.txt')
    gro = GroClient(access_token=gro_token)
    if (method=="search"):
        return gro.search(parameter, data)
    elif (method=="lookup"):
        return gro.lookup(parameter, data)
    elif (method=="get_data_series"):
        return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #serve(app, host='0.0.0.0', port=80)