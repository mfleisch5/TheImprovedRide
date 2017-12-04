from flask import Flask, request
from . import RoutingCalculator
import json, os
from flask_cors import CORS

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
CORS(app)


@app.route('/post', methods=['POST'])
def get_data():
    in_records = request.json['trips']
    data = RoutingCalculator.main(in_records, os.path.join(dir_path, 'geocodes.json'),
                                  os.path.join(dir_path, 'failures.json'), 100)
    return json.dumps({'routes': data[0].to_json_format(),
                       'uber': data[1]})


app.debug = True
app.run(host='0.0.0.0', port=5000)
