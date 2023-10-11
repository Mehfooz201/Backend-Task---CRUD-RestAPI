from decimal import Decimal
from rest_framework import serializers
from base.models import OnlineBookStore



class BookStoreSerailizer(serializers.ModelSerializer):
    class Meta:
        model = OnlineBookStore
        fields = '__all__'
