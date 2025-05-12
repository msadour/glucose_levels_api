import csv
import os
import uuid
from datetime import datetime
from typing import Optional, TextIO

from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone

from source.apps.level.models import GlucoseRecord, UnaUser


def convert_to_datetime(date_str: str) -> Optional[datetime]:
    if not date_str:
        return None

    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
        date_obj = timezone.make_aware(date_obj)
        return date_obj
    except ValueError:
        return None


def get_csv_reader(csvfile: TextIO) -> csv.DictReader:
    """
    Tries to read the CSV file and determine if the headers are on line 2 or 3.
    Returns a csv.DictReader object if successful, or raises an exception if not.
    """
    csvfile = csvfile.readlines()
    try:
        csvfile_2 = csvfile[1:]
        reader_2 = csv.DictReader(csvfile_2)

        if reader_2.fieldnames:
            return reader_2
        else:
            raise ValueError("Unable to read headers correctly on second line.")

    except Exception:
        csvfile_3 = csvfile[2:]
        reader_3 = csv.DictReader(csvfile_3)

        if reader_3.fieldnames:
            return reader_3
        else:
            raise ValueError("Unable to read headers correctly on third line.")


def create_glucose_records(una_file: InMemoryUploadedFile):
    try:
        user_id_str = os.path.splitext(una_file.name)[0]
        user_id = uuid.UUID(user_id_str)
    except ValueError:
        raise ValueError("Invalid filename format. Expected format: user_id.csv")

    user, created = UnaUser.objects.get_or_create(una_id=user_id)

    file_path_temp = default_storage.save(f"temp/{una_file.name}", una_file)
    file_path = os.path.join(default_storage.location, file_path_temp)

    records_created = 0

    try:
        with open(file_path, "r", encoding="utf-8-sig") as csvfile:
            reader = get_csv_reader(csvfile)
            for row in reader:
                device_timestamp_str = row.get("Gerätezeitstempel")
                device_timestamp = convert_to_datetime(date_str=device_timestamp_str)
                GlucoseRecord.objects.create(
                    user=user,
                    serie_number=row.get("Seriennummer"),
                    device_timestamp=device_timestamp,
                    record_type=row.get("Aufzeichnungstyp"),
                    glucose_value_history_mg_dl=to_float(
                        row.get("Glukosewert-Verlauf mg/dL")
                    ),
                    glucose_scan_mg_dl=to_float(row.get("Glukose-Scan mg/dL")),
                    non_numeric_rapid_insulin=row.get(
                        "Nicht numerisches schnellwirkendes Insulin"
                    ),
                    rapid_insulin_units=to_float(
                        row.get("Schnellwirkendes Insulin (Einheiten)")
                    ),
                    non_numeric_food_data=row.get("Nicht numerische Nahrungsdaten"),
                    carbohydrates_grams=to_float(row.get("Kohlenhydrate (Gramm)")),
                    carbohydrates_servings=to_float(
                        row.get("Kohlenhydrate (Portionen)")
                    ),
                    non_numeric_basal_insulin=row.get("Nicht numerisches Depotinsulin"),
                    basal_insulin_units=to_float(row.get("Depotinsulin (Einheiten)")),
                    notes=row.get("notes"),
                    glucose_test_strip_mg_dl=to_float(
                        row.get("Glukose-Teststreifen mg/dL")
                    ),
                    ketone_mmol_l=to_float(row.get("Keton mmol/L")),
                    mealtime_insulin_units=to_float(
                        row.get("Mahlzeiteninsulin (Einheiten)")
                    ),
                    correction_insulin_units=to_float(
                        row.get("Korrekturinsulin (Einheiten)")
                    ),
                    user_adjusted_insulin_units=to_float(
                        row.get("Insulin-Änderung durch Anwender (Einheiten)")
                    ),
                )
                records_created += 1

    except Exception as e:
        raise Exception(str(e))
    finally:
        if os.path.exists(file_path_temp):
            os.remove(file_path_temp)

    return records_created


def to_float(value):
    try:
        return float(value) if value else None
    except ValueError:
        return None
