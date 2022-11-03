"""Timeless - a datetime toolkit for people in a hurry."""

from timeless.datetime import Datetime as datetime
from timeless.datetime import Weekdays as weekdays
from timeless.datetime import get_first_weekday_in_month
from timeless.datetime import now
from timeless.datetime import parse
from timeless.datetime import today
from timeless.period import Period as period


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
]
