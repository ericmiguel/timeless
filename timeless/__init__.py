"""..."""

# flake8: noqa

from timeless.api import datetime
from timeless.api import from_pandas
from timeless.api import now
from timeless.api import parse
from timeless.api import period
from timeless.api import to_pandas
from timeless.api import today
from timeless.utils import Weekdays as weekdays
from timeless.datetime import Datetime
from timeless.period import Period


# module level doc-string
__doc__ = """
timeless - a datetime toolkit for people in a hurry.
=====================================================================

**timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit to easly perform datetime operations like create time ranges, add and subtract.
It tries to be as simple as possible abstracting some anoying details like timezones 
and multiple date objects types like timestamps, date, datetime, etc.
"""
