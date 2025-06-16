from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import datetime
import re

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # 1. Get raw input values from form
        make = request.form.get('Make')
        kilometer = float(request.form.get('Kilometer'))
        fuel = request.form.get('Fuel Type')
        transmission = request.form.get('Transmission')
        location = request.form.get('Location')
        color = request.form.get('Color')
        owner = request.form.get('Owner')
        seller = request.form.get('Seller Type')
        engine = float(request.form.get('Engine'))
        drivetrain = request.form.get('Drivetrain')
        length = float(request.form.get('Length'))
        width = float(request.form.get('Width'))
        height = float(request.form.get('Height'))
        seating_capacity = int(request.form.get('Seating Capacity'))
        fuel_tank_capacity = float(request.form.get('Fuel Tank Capacity'))

        # 2. Extract bhp and rpm from text inputs like '87 bhp @ 6000 rpm'
        def extract_per_rpm(value_text, unit):
            numbers = re.findall(r'(\d+)', value_text)
            if len(numbers) >= 2:
                num = float(numbers[0])
                rpm = float(numbers[1])
                return num / rpm
            return 0.0

        power_text = request.form.get('Max_Power')  # e.g. "87 bhp @ 6000 rpm"
        torque_text = request.form.get('Max_Torque')  # e.g. "109 Nm @ 4500 rpm"

        power_per_rpm = extract_per_rpm(power_text, 'bhp')
        torque_per_rpm = extract_per_rpm(torque_text, 'Nm')

        # 3. Calculate Age from manufacture year
        year = int(request.form.get('Year'))
        current_year = datetime.datetime.now().year
        age = current_year - year

        # 4. Normalize categorical variables
        fuel = fuel if fuel in ['Petrol', 'Diesel'] else 'Other'
        allowed_colors = ['Grey', 'White', 'Maroon', 'Red', 'Blue', 'Silver', 'Brown', 'Black']
        color = color if color in allowed_colors else 'Other'
        owner = owner if owner in ['First', 'Second', 'Third'] else 'Other'
        seller = seller if seller == 'Individual' else 'Other'

        # 5. Create data object
        data = CustomData(
            Make=make,
            Kilometer=kilometer,
            Fuel_Type=fuel,
            Transmission=transmission,
            Location=location,
            Color=color,
            Owner=owner,
            Seller_Type=seller,
            Engine=engine,
            Drivetrain=drivetrain,
            Length=length,
            Width=width,
            Height=height,
            Seating_Capacity=seating_capacity,
            Fuel_Tank_Capacity=fuel_tank_capacity,
            power_per_rpm=power_per_rpm,
            torque_per_rpm=torque_per_rpm,
            Age=age
        )

        pred_df = data.get_data_as_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(debug=True)
