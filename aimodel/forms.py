# Not integreated in this project
from django import forms
from datetime import datetime

class pricepredictionform(forms.Form):

    onroad_price = forms.IntegerField(label='onroad_price',
                                      min_value=50000,required=True,
                                      error_messages={
                                          'min_value':'value should be greater than 50,000'
                                          ,'required':'on road price is required for better accuracy'})
    year = forms.IntegerField(label='year',max_value=datetime.now().year,
                              required=True,error_messages={
                                  'max_value':'How can you sell car that was not even purchased',
                                  'required':'Year is required for better accuracy'
                              })
    km = forms.IntegerField(label='km',min_value=1,required=True,error_messages={
                                           'required':'km is required for better accuracy'
                              })
    condition = forms.IntegerField(label='condition',min_value=1,max_value=10
                                   ,required=True,error_messages={
                                       'reqired':'car condition is required for better accuracy'
                                    })
    economy = forms.IntegerField(label='economy',min_value=2,required=True,error_messages={
                                             'required':'milage is required for better accuracy'
                                            })
    

