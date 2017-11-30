from flask import Flask, request
import RoutingCalculator, json, os

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def get_data():
    in_records = request.json['trips']
    return json.dumps(RoutingCalculator.main(in_records, os.path.join(dir_path, 'geocodes.json'),
                                             os.path.join(dir_path,'failures.json'), 3).to_json_format())

app.debug = True
app.run(host='0.0.0.0', port=5000)