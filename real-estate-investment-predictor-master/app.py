import numpy as np
from numpy.core.numeric import outer
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]     
    df = pd.DataFrame (final_features, columns = ['price', 'zestimate','bathrooms','bedrooms','area','rent_zestimate','zipcode'])
    # prediction = model.predict(final_features)
    prediction = model.predict(df)

    output = round(prediction[0], 2)
    if(output != 0):
        output = "a good investment"
    else:
        output = "not a good investment"

    return render_template('index.html', prediction_text='This property is {}'.format(output))


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
