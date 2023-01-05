from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('prabhat_pizza_price_pred_rf.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        company = int(request.form['company'])
        diameter=float(request.form['diameter'])
        topping=int(request.form['topping'])
        variant=float(request.form['variant'])
        size=int(request.form['size'])
        sauce=int(request.form['sauce'])
        cheese=float(request.form['cheese'])
        
                
        prediction=model.predict([[company,diameter,topping,variant,size,sauce,cheese]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry  enter proper value in the form")
        else:
            return render_template('index.html',prediction_text="Pizza cost price will be  {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

