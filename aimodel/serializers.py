from rest_framework import serializers
from datetime import datetime

#serializer validation 
class carpriceSerializer(serializers.Serializer):
    onroad_price = serializers.IntegerField()
    def validate_onroad_price(self,price):
        if price < 150000:
            raise serializers.ValidationError("value should be greater than 150000")
        return price

    year = serializers.IntegerField()
    def validate_year(self,year):
        present = datetime.now().year
        if year <= 2000 or year > present:
            raise serializers.ValidationError("Year should be greater than 2001")
        return year

    km = serializers.IntegerField()
    def validate_km(self,km):
        if km < 100:
            raise serializers.ValidationError("Km should be more than 100km")
        return km
    condition = serializers.IntegerField()
    def validate_condition(self,condition):
        if 0 >= condition > 10:
            raise serializers.ValidationError("Value should be between 1 to 10")
        return condition
    economy = serializers.IntegerField()
    def validate_economy(self, economy):
        if economy < 2:
            raise serializers.ValidationError("Milage should be Greater than 2")
        return economy
  
    