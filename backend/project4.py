from flask import Flask, jsonify
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
from joblib import load
import pickle
import numpy as np
from flask import request


app = Flask(__name__)
CORS(app)


# load model
loaded_rf_model = pickle.load(open('../DataProcessing/rf_model2.pickle', "rb"))
loaded_scaler = load('../DataProcessing/std_scaler.bin')


@app.route("/input", methods=['POST'])
def input():
    data = request.get_json()
    # x_array = np.array(data)
    # print(x_array)
    x_array = loaded_scaler.transform(data)
    print(x_array)
    output = []
    result = loaded_rf_model.predict(x_array)
    print(result[0])
    output.append({'value': result[0]})
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
