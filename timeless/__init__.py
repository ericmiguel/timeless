"""Timeless - a datetime toolkit for people in a hurry."""

from timeless.converters.datetime_converter import from_datetime
from timeless.converters.datetime_converter import to_datetime
from timeless.datetime import Datetime as datetime
from timeless.datetime import Weekdays as weekdays
from timeless.datetime import get_first_weekday_in_month
from timeless.datetime import now
from timeless.datetime import parse
from timeless.datetime import today
from timeless.helpers import days_to_hours
from timeless.helpers import days_to_minutes
from timeless.helpers import days_to_seconds
from timeless.helpers import hours_to_days
from timeless.helpers import hours_to_minutes
from timeless.helpers import hours_to_seconds
from timeless.helpers import minutes_to_days
from timeless.helpers import minutes_to_hours
from timeless.helpers import minutes_to_seconds
from timeless.helpers import seconds_to_days
from timeless.helpers import seconds_to_hours
from timeless.helpers import seconds_to_minutes
from timeless.period import Period as period


try:
    import pandas  # type: ignore
except ImportError:
    pass
else:
    from timeless.converters.pandas_converter import from_pd_datetimeindex
    from timeless.converters.pandas_converter import from_pd_timestamp
    from timeless.converters.pandas_converter import to_pd_timestamp

try:
    import numpy  # type: ignore
except ImportError:
    pass
else:
    from timeless.converters.numpy_converter import from_np_datetime64
    from timeless.converters.numpy_converter import to_np_datetime64


# module level doc-string
__doc__ = """
Timeless - a datetime toolkit for people in a hurry.
=====================================================================
**Timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit. Simple date ranges, datetime operations and just one import.

This package is a work in progress and it was created as a study object.
"""

__all__ = [
    "datetime",
    "period",
    "get_first_weekday_in_month",
    "now",
    "today",
    "parse",
    "weekdays",
    "seconds_to_minutes",
    "seconds_to_hours",
    "seconds_to_days",
    "minutes_to_seconds",
    "minutes_to_hours",
    "minutes_to_days",
    "hours_to_seconds",
    "hours_to_minutes",
    "hours_to_days",
    "days_to_seconds",
    "days_to_minutes",
    "days_to_hours",
    "to_datetime",
    "from_datetime",
    "from_np_datetime64",
    "to_np_datetime64",
    "from_pd_datetimeindex",
    "from_pd_timestamp",
    "to_pd_timestamp",
]
