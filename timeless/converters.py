"""Type converters for ease integrations."""

import warnings

from datetime import datetime as _datetime
from typing import List
from typing import Optional
from typing import Union
from zoneinfo import ZoneInfo

import pandas as pd

from dateutil import parser
from timeless import utils
from timeless.datetime import Datetime
from timeless.period import Period


def to_datetime(datetime: _datetime) -> _datetime:
    """
    Convert a timeless.Datetime to a datetime object.

    Returns
    -------
    _datetime
        Python's default datetime object.
    """
    return _datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=datetime.hour,
        minute=datetime.minute,
        second=datetime.second,
        microsecond=datetime.microsecond,
        tzinfo=datetime.tzinfo,
    )


def from_datetime(
    datetime: _datetime, zone: Union[ZoneInfo, str] = ZoneInfo("UTC")
) -> Datetime:
    """
    Convert a datetime object to a timeless.Datetime.

    Parameters
    ----------
    datetime : _datetime
        Python's default datetime object.
    zone : Union[ZoneInfo, str], optional
        Timezone, by default ZoneInfo("UTC")

    Returns
    -------
    Datetime
        Timeless datetime
    """
    return Datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=datetime.hour,
        minute=datetime.minute,
        second=datetime.second,
        microsecond=datetime.microsecond,
        zone=zone,
    )


def from_pandas(dt: Union[pd.DatetimeIndex, pd.Timestamp]) -> Union[Datetime, Period]:
    """
    Create a Datetime instance from a pandas.Timestamp or a pandas.DateTimeIndex.

    Parameters
    ----------
    dt : Union[pd.DatetimeIndex, pd.Timestamp]
        Pandas instance.

    Returns
    -------
    Union[Datetime, Period]
        Datetime or Period (time span) instance.
    """
    if isinstance(dt, pd.DatetimeIndex):
        freq = None

        if dt.freq:
            freq = utils.parse_pandas_offset_freq(dt.freq.name)
        else:
            pass
            # raise ValueError("No frequency found in DatetimeIndex")

        _start = dt.min().to_pydatetime()
        _end = dt.max().to_pydatetime()

        try:
            _ = _start.tzinfo.zone
        except AttributeError:
            _start = _start.astimezone(ZoneInfo("UTC"))
            _end = _end.astimezone(ZoneInfo("UTC"))

        start = Datetime(
            _start.year,
            _start.month,
            _start.day,
            _start.hour,
            _start.minute,
            _start.second,
            _start.microsecond,
            _start.tzinfo.key,
        )
        end = Datetime(
            _end.year,
            _end.month,
            _end.day,
            _end.hour,
            _end.minute,
            _end.second,
            _end.microsecond,
            _end.tzinfo.key,
        )

        if freq is None:
            warnings.warn("No frequency found in DatetimeIndex: assuming 'days'.")
            freq = "days"

        return Period(start, end, freq)

    else:
        datetime_obj = dt.to_pydatetime()

        try:
            _ = datetime_obj.tzinfo.zone
        except AttributeError:
            datetime_obj = datetime_obj.astimezone(ZoneInfo("UTC"))

        return Datetime(
            datetime_obj.year,
            datetime_obj.month,
            datetime_obj.day,
            datetime_obj.hour,
            datetime_obj.minute,
            datetime_obj.second,
            datetime_obj.microsecond,
            datetime_obj.tzinfo.key,
        )


def to_pandas(dt: Union[Period, Datetime]) -> Union[List[pd.Timestamp], pd.Timestamp]:
    """
    Create a pandas.Timestamp instance from a Datetime.

    Periods are converted to a list of pandas.Timestamp instances.

    Lists of Timestamps are automatically coerced DatetimeIndex by Pandas.

    Parameters
    ----------
    dt : Union[Period, Datetime]
        Timeless Datetime or Period instance.

    Returns
    -------
    Union[List[pd.Timestamp], pd.Timestamp]
        Pandas time instances.
    """
    if isinstance(dt, Period):
        return [pd.Timestamp(d) for d in dt]
    else:
        return pd.Timestamp(dt)


def parse(
    string: str,
    format: Optional[str] = None,
    zone: Optional[str] = None,
    day_first: bool = False,
    year_first: bool = False,
) -> Datetime:
    """
    Parse a string into a Datetime.

    If no format is provided, the string is parsed using Dateutil's parser. Otherwise,
    the string is parsed using strptime. In the latter case dateutil's parser arguments
    (nominally day_first, year_first) are ignored.

    The "ignoretz" parameter is not supported, since "zone" can override the timezone
    value and Timeless does not accept naive datetimes.

    See https://dateutil.readthedocs.io/en/stable/parser.html for more information on
    dautil's parser arguments.

    Parameters
    ----------
    string : str
        datetime string to parse.
    format : Optional[str]
        dateutil format string, by default None.
    zone : Optional[str]
        timezone name (overrides parsed value), by default None.
    day_first : bool, optional
        Whether to interpret the first value in an ambiguous 3-integer date as the day,
        by default False
    year_first : bool, optional
        Whether to interpret the first value in an ambiguous 3-integer date as the year,
        by default False.

    Returns
    -------
    Datetime
        Parsed datetime.
    """
    if format:
        parsed = _datetime.strptime(string, format)
    else:
        parser_info = parser.parserinfo(dayfirst=day_first, yearfirst=year_first)
        parsed = parser.parse(string, parser_info)

    if not zone:
        zone = parsed.tzname()
        if not zone:
            zone = "UTC"

    return Datetime(
        parsed.year,
        parsed.month,
        parsed.day,
        parsed.hour,
        parsed.minute,
        parsed.second,
        parsed.microsecond,
        zone,
    )
