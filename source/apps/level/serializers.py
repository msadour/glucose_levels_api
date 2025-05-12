from rest_framework import serializers

from .models import GlucoseRecord


class GlucoseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlucoseRecord
        fields = [
            "id",
            "serie_number",
            "device_timestamp",
            "record_type",
            "glucose_value_history_mg_dl",
            "glucose_scan_mg_dl",
            "non_numeric_rapid_insulin",
            "rapid_insulin_units",
            "non_numeric_food_data",
            "carbohydrates_grams",
            "carbohydrates_servings",
            "non_numeric_basal_insulin",
            "basal_insulin_units",
            "notes",
            "glucose_test_strip_mg_dl",
            "ketone_mmol_l",
            "mealtime_insulin_units",
            "correction_insulin_units",
            "user_adjusted_insulin_units",
        ]
        read_only_fields = ["id"]
