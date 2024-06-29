#cleaning & formating the data and
import pandas as pd       

#visualizing the data and seaborn is rival to it
import matplotlib.pyplot as plt   

# use for dividing the data(train data and test data ) to train the model
from sklearn.model_selection import train_test_split      

#We using linear regression model because of car price change time to time so, regression is used for continuous data
from sklearn.linear_model import LinearRegression  

#for evaluating the model(accuracy of the model)
from sklearn.metrics import mean_squared_error   

# used to saving the model and we can use in django
import joblib

import os



car_dataset = pd.read_csv('dataset/car_data.csv')   

#first 5 rows of the data to understand
# print(car_dataset.head())   
                                  
#information about the data(car data.csv)
# car_dataset.info()     
                            
#shape of the data(no.of rows,columns)
# print(car_dataset.shape)
                                    
#checking for null values
# car_dataset.isnull().sum()  
                                 


#method1: removing error from replace because of we downcasting the type of column 
# pd.set_option('future.no_silent_downcasting', True)  



#Changing data type char to into for better understaing to the model

# car_dataset.replace({"Fuel_Type":{"Petrol":0,"Diesel":1,"CNG":2}},inplace=True)  
# car_dataset.replace({"Transmission":{"Manual":0,"Automatic":1}},inplace=True)



#method2: Explicitly downcast the columns to integer type
# car_dataset['Fuel_Type'] = car_dataset['Fuel_Type'].astype(int)
# car_dataset['Transmission'] = car_dataset['Transmission'].astype(int)


# X is Input values, Y is Output values(Target column)
# X = car_dataset[["Year","Present_Price","Kms_Driven","Fuel_Type","Transmission"]]  
# Y = car_dataset["Selling_Price"]      
X = car_dataset[['onroad_price','years','km','condition','economy']]
Y = car_dataset['current_price']                                         


#spliting test data and training data and (test size of 20%)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)  

print("HEllo world")


# model getting trained by using the "fit" from sklearn
model = LinearRegression()
model.fit(X_train,Y_train)

train_score = model.score(X_train,Y_train)
test_score = model.score(X_test,Y_test)

#Testing the model using the test data
# model_prediction = model.predict(X_test)                        
# print(model_prediction)



# Save the trained model(dump)and -----> we load this model in views.py to execute according to our instructions
model_path = os.path.join(os.path.dirname(__file__), 'car_price_model.pkl')
score_path = os.path.join(os.path.dirname(__file__), 'model_score.txt')
joblib.dump(model, model_path)

with open(score_path,'w') as f:
    f.write(str(test_score))
