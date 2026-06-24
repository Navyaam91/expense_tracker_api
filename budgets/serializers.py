from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = [
            'id',
            'category',
            'limit',
            'month',
            'year',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_limit(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Budget limit must be greater than zero!"
            )
        return value

    def validate_month(self, value):
        if value < 1 or value > 12:
            raise serializers.ValidationError(
                "Month must be between 1 and 12!"
            )
        return value

    def validate_year(self, value):
        if value < 2000:
            raise serializers.ValidationError(
                "Year must be 2000 or later!"
            )
        return value