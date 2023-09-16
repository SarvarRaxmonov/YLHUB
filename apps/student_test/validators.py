from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_min_duration(value):
    min_duration = 60
    if value.total_seconds() < min_duration:
        raise ValidationError(
            _("%(value)s is less than the minimum duration of %(min_duration)s seconds."),
            params={"value": value, "min_duration": min_duration},
        )
    return value
