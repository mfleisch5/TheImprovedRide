from flask import Flask, request
import RoutingCalculator

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def get_json():
    in_dict = request.json['trips']
    return RoutingCalculator.main(in_dict, 'geocodes.json', 'failures.json')

app.debug = True
app.run(host='0.0.0.0', port=5000)