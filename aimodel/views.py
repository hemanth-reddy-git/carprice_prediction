from django.shortcuts import render
import os
import joblib 
model_path = os.path.join(os.path.dirname(__file__), '..', 'car_price_model.pkl')
score_path = os.path.join(os.path.dirname(__file__), '..', 'model_score.txt')
model = joblib.load(model_path)
from datetime import datetime

from .forms import pricepredictionform

# Type casting using Dict

# Transmission = {"Manual":0,"Automatic":1}
# Fuel_Type = {"Petrol":0,"Diesel":1,"CNG":2}

with open(score_path,'r') as f:
    model_score = float(f.read())

def home(request):
    model_prediction = None
    if request.method == "POST":
        p_form = pricepredictionform(request.POST)
        if p_form.is_valid():
            onroad_price = p_form.cleaned_data['onroad_price']
            year = p_form.cleaned_data['year']
            km = p_form.cleaned_data['km']
            condition = p_form.cleaned_data["condition"]
            economy = p_form.cleaned_data["economy"]

            present = datetime.now().year
            year = present - year

            # feature4 = Fuel_Type[feature4]
            # feature5 = Transmission[feature5]
            input_data = [[onroad_price, year, km, condition, economy]]
            model_prediction =float(model.predict(input_data))
            print(model_prediction)
            p_form = pricepredictionform()
            return render(request,"home.html",{'model_prediction':round(model_prediction,2),'form':p_form,'model_score':round(model_score*100,2)}) 
        else:
            p_form = pricepredictionform(request.POST)
            
                

    else:
        p_form = pricepredictionform()
    
    return render(request,"home.html",{'form':p_form})
