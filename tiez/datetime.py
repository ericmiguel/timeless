"""Human friendly datetime utilities."""

from datetime import date as date
from datetime import datetime as datetime

from dateutil.relativedelta import relativedelta


class Datetime(datetime, date):
    """..."""

    def __new__(cls, *args, **kwargs):
        """..."""
        self = datetime.__new__(cls, *args, **kwargs)
        return self

    def add(self, *args, **kwargs) -> "Datetime":
        """
        Add duration from the instance.

        Returns
        -------
        [type]
            [description]
        """
        dt = self + relativedelta(*args, **kwargs)
        return self.__class__(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
        )

    def subtract(self, *args, **kwargs) -> "Datetime":
        """
        Remove duration from the instance.

        [extended_summary]

        Returns
        -------
        [type]
            [description]
        """
        dt = self - relativedelta(*args, **kwargs)
        return self.__class__(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
        )
