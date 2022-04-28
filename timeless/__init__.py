"""Timeless - a datetime toolkit for people in a hurry."""

# flake8: noqa
from timeless.converters import from_datetime
from timeless.converters import from_np_datetime64
from timeless.converters import from_pd_datetimeindex
from timeless.converters import from_pd_timestamp
from timeless.converters import to_datetime
from timeless.converters import to_np_datetime64
from timeless.datetime import Datetime as datetime
from timeless.datetime import get_first_weekday_in_month
from timeless.datetime import now
from timeless.datetime import parse
from timeless.datetime import today
from timeless.period import Period as period
from timeless.utils import Weekdays as weekdays


# module level doc-string
__doc__ = """
Timeless - a datetime toolkit for people in a hurry.
=====================================================================
**Timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit. Simple date ranges, datetime operations and just one import.

This package is a work in progress and it was created as a study object.
"""
