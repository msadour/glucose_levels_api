from django.db import models


class User(models.Model):
    una_id = models.UUIDField(unique=True)


class GlucoseRecord(models.Model):
    serie_number = models.UUIDField()
    device_timestamp = models.DateTimeField()
    record_type = models.CharField(max_length=50)
    glucose_value_history_mg_dl = models.FloatField(null=True, blank=True)
    glucose_scan_mg_dl = models.FloatField(null=True, blank=True)
    non_numeric_rapid_insulin = models.CharField(max_length=100, null=True, blank=True)
    rapid_insulin_units = models.FloatField(null=True, blank=True)
    non_numeric_food_data = models.CharField(max_length=100, null=True, blank=True)
    carbohydrates_grams = models.FloatField(null=True, blank=True)
    carbohydrates_servings = models.FloatField(null=True, blank=True)
    non_numeric_basal_insulin = models.CharField(max_length=100, null=True, blank=True)
    basal_insulin_units = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    glucose_test_strip_mg_dl = models.FloatField(null=True, blank=True)
    ketone_mmol_l = models.FloatField(null=True, blank=True)
    mealtime_insulin_units = models.FloatField(null=True, blank=True)
    correction_insulin_units = models.FloatField(null=True, blank=True)
    user_adjusted_insulin_units = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="glucose_records"
    )
