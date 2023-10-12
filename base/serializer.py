from decimal import Decimal
from rest_framework import serializers
from base.models import OnlineBookStore


# Serializer for the OnlineBookStore model, including all fields.
class BookStoreSerailizer(serializers.ModelSerializer):
    # Metadata configuration for the serializer.
    class Meta:
        # Associate the serializer with the OnlineBookStore model.
        model = OnlineBookStore

        # Include all fields from the model in the serialization process.
        fields = '__all__'
