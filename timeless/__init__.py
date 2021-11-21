"""..."""

# flake8: noqa

from api import datetime
from api import period
from api import to_pandas
from api import from_pandas
from api import today
from api import now

# module level doc-string
__doc__ = """
timeless - a datetime toolkit for people in a hurry.
=====================================================================

**timeless** sits on sholders of giants to provide a simple and easy to use datetime
toolkit to easly perform datetime operations like create a period, add, subtract. It
tries to be as simple as possible abstracting some anoying details like timezones.
"""