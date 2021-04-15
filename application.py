from flask import Flask, render_template, request
import os, joblib

model = joblib.load('model_v2.joblib')

# init app
application = app = Flask(__name__)

# home page 
@app.route('/')
def index():
    return render_template('index.html')

# 
@app.route('/pedict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        
        bedrooms = int(request.form['bedrooms']) 
        bathrooms = float(request.form['bathrooms'])
        waterfront = int(request.form['waterfront'])
        view = int(request.form['view'])
        grade = int(request.form['grade'])
        lat = float(request.form['lat'])
        sqft_living = float(request.form['sqft_living'])

        data = [[bedrooms, bathrooms, waterfront, view, grade, lat, sqft_living]]
        predicted_price = model.predict(data)[0]
        predicted_price = round(predicted_price, 2)

    return render_template('index.html', pred_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)