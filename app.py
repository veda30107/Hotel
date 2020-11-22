# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:03:35 2020

@author: Veda
"""

from flask import Flask, render_template, request
from wtforms import Form, validators
from wtforms import TextAreaField
import numpy as np
import sklearn.externals
import joblib


loaded_model=joblib.load('./pkl_objects/model.pkl')
loaded_stop=joblib.load('./pkl_objects/stop_words.pkl')
loaded_vec=joblib.load('./pkl_objects/vectorizer.pkl')

app = Flask(__name__)
def classify(document):
     label = {1: 'negative', 3: 'positive', 2:'neutral'}
     X = loaded_vec.transform([document])
     y = loaded_model.predict(X)[0:]
     return y
 
class ReviewForm(Form):
     hotelreview = TextAreaField('',[validators.DataRequired(),validators.length(min=15)])
     
@app.route('/')

def index():
    form = ReviewForm(request.form)
    return render_template('index.html', form=form)

@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
       review = request.form['hotelreview']
       y = classify(review)
       return render_template('result.html',content=review,prediction=y)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)