import flask
app = flask.Flask(__name__)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#-------- MODEL GOES HERE -----------#

df = pd.read_csv('../data/SMSSpamCollection.txt', sep='\t', header=None)
df.columns = ['target', 'msg']
y = df['target']
X = df['msg']

# Tfidf, filter stop words, 300 features
cvec = TfidfVectorizer(stop_words='english', max_features = 300)
X = cvec.fit_transform(X)
clf = MultinomialNB()
clf.fit(X, y)

#-------- ROUTES GO HERE -----------#


@app.route('/is_spam', methods=["GET"])
def is_spam():
    msg = pd.Series(flask.request.args['msg'])
    X_new = cvec.transform(msg)
    score = clf.predict(X_new)
    results = {'prediction': score[0]}
    return flask.jsonify(results)

# This method takes input via an HTML page
@app.route('/page')
def page():
   with open("page.html", 'r') as viz_file:
       return viz_file.read()



if __name__ == '__main__':
    '''Connects to the server'''

    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
