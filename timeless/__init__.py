"""Timeless - a datetime toolkit for people in a hurry."""

# flake8: noqa
from timeless.converters import from_datetime
from timeless.converters import from_pandas
from timeless.converters import parse
from timeless.converters import to_datetime
from timeless.converters import to_pandas
from timeless.datetime import Datetime as datetime
from timeless.datetime import get_first_weekday_in_month
from timeless.datetime import now
from timeless.datetime import today
from timeless.period import Period as period
from timeless.utils import Weekdays as weekdays


# module level doc-string
__doc__ = """
Timeless - a datetime toolkit for people in a hurry.
=====================================================================

**timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit to easly perform datetime operations like create time ranges, add and subtract.
It tries to be as simple as possible abstracting some anoying details like timezones 
and multiple date objects types like timestamps, date, datetime, etc.
"""
