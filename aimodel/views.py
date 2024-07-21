import os
import joblib 
import datetime
from .models import cardata
from rest_framework import status
from django.shortcuts import render
from .serializers import carpriceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# retreving model and data from model_train.py
model_path = os.path.join(os.path.dirname(__file__), '..', 'car_price_model.pkl')
score_path = os.path.join(os.path.dirname(__file__), '..', 'model_score.txt')
model = joblib.load(model_path)


with open(score_path,'r') as f:
    model_score = float(f.read())

#building API using function api_view 
@api_view(['POST'])
def carprice(request):
    if request.method == "POST":
        #debug
        print(request.data)
        #created instance for serializer that takes input feature from interface
        serialized_data = carpriceSerializer(data=request.data)
        if serialized_data.is_valid():
            print("Data is valid")  # debug
            #Data retreving from validated Serializer
            onroad_price = serialized_data.validated_data['onroad_price']
            year = serialized_data.validated_data['year']
            km = serialized_data._validated_data['km']
            condition = serialized_data.validated_data["condition"]
            economy = serialized_data.validated_data["economy"]
            
            # Year converting for the model
            present = datetime.datetime.now().year
            year_diff= present - year
            
            print(year_diff) #debug
            print("year is working")
            
            #model prediciton 
            input_data = [[onroad_price , year_diff, km, condition, economy]]
            print(input_data[0])
            model_prediction =float(model.predict(input_data))
            model_prediction = round(model_prediction,2)
            
            print(model_prediction) #debug

            #year converting for the database sqlite
            year = present - year_diff

            #sending data to the database and saving 
            data = cardata(
                onroad_price = onroad_price,
                year = year,
                km = km,
                condition = condition,
                economy = economy,
                model_prediction = model_prediction
                )
            data.save()

            return Response({'model_prediction': model_prediction,'model_score':round(model_score*100,2)}, status=status.HTTP_200_OK)
        
        print("data is invalid") #debug
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "only post method is allowed to submit data"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#calling frontend
def home(request):
    return render(request,'home.html')