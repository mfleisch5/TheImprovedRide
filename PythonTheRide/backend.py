from flask import Flask, request
import RoutingCalculator, json

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def get_data():
    in_records = request.json['trips']
    return json.dumps(RoutingCalculator.main(in_records, 'geocodes.json', 'failures.json', 3).to_json_format())

app.debug = True
app.run(host='0.0.0.0', port=5000)