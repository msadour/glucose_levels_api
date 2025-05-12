from datetime import datetime
from typing import Optional

from django.utils import timezone


def convert_to_datetime(
    date_str: str, format: str = "%d-%m-%Y %H:%M"
) -> Optional[datetime]:
    if not date_str:
        return None

    try:
        date_obj = datetime.strptime(date_str, format)
        date_obj = timezone.make_aware(date_obj)
        return date_obj
    except ValueError:
        return None


def to_float(value: str) -> Optional[float]:
    try:
        return float(value) if value else None
    except ValueError:
        return None
