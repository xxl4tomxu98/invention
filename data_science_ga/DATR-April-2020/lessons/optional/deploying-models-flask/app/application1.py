import pickle
import numpy as np
import pandas as pd
import flask
app = flask.Flask(__name__)

#-------- MODEL GOES HERE -----------#

with open('../titanic_rfc.pkl', 'rb') as picklefile:
    PREDICTOR = pickle.load(picklefile)

with open('../tfid_vector_transform.pkl', 'rb') as picklefile:
    cvec = pickle.load(picklefile)
    
with open('../smsspam_nb.pkl', 'rb') as picklefile:
    smspredictor = pickle.load(picklefile)
    
#-------- ROUTES GO HERE -----------#
@app.route('/predict', methods=["GET"])
def predict():
    pclass = flask.request.args['pclass']
    sex = flask.request.args['sex']
    age = flask.request.args['age']
    fare = flask.request.args['fare']
    sibsp = flask.request.args['sibsp']

    item = np.asarray([pclass, sex, age, fare, sibsp]).reshape(1, -1)
    score = PREDICTOR.predict_proba(item)
    results = {'survival chances': score[0, 1], 'death chances': score[0, 0]}
    return flask.jsonify(results)

@app.route('/is_spam', methods=["GET"])
def is_spam():
     msg = pd.Series(flask.request.args['msg'])
     X_new = cvec.transform(msg)
     score = smspredictor.predict(X_new)
     results = {'prediction': score[0]}
     return flask.jsonify(results)
 
#---------- CREATING AN API, METHOD 2 ----------------#

# This method takes input via an HTML page
@app.route('/page')
def page():
    with open("page1.html", 'r') as viz_file:
        return viz_file.read()


@app.route('/result', methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

        inputs = flask.request.form
        msg = inputs['msg']
        pclass = inputs['pclass'][0]
        sex = inputs['sex'][0]
        age = inputs['age'][0]
        fare = inputs['fare'][0]
        sibsp = inputs['sibsp'][0]

        item = np.array([pclass, sex, age, fare, sibsp]).reshape(1, -1)
        sms_msg = pd.Series(msg)
        score = PREDICTOR.predict_proba(item)
        X_new = cvec.transform(sms_msg)
        sms_score = smspredictor.predict(X_new)
        results = {
            'survival chances': score[0, 1], 'death chances': score[0, 0], 
            'sms_prediction': sms_score[0]}
        return flask.jsonify(results)



if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
