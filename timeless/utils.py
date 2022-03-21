"""Convenience functions, mostly for internal use."""

from dataclasses import dataclass
from typing import Optional

from dateutil import relativedelta


def parse_pandas_offset_freq(offset: str) -> Optional[str]:
    """
    Map pandas offset strings to timeless.Datetime strings.

    Parameters
    ----------
    offset : str
        Pandas offset string.

    Returns
    -------
    Optional[str]
        Timeless offset string.

    Raises
    ------
    ValueError
        Invalid or unknown offset string.
    """
    offsets = {
        "B": None,
        "C": None,
        "D": "days",
        "W": "weeks",
        "M": "months",
        "SM": None,
        "BM": None,
        "CBM": None,
        "MS": "months",
        "SMS": None,
        "BMS": None,
        "CBMS": None,
        "Q": None,
        "BQ": None,
        "QS": None,
        "BQS": None,
        "A": "years",
        "Y": "years",
        "BA": None,
        "BY": None,
        "AS": "years",
        "YS": "years",
        "BAS": None,
        "BYS": None,
        "BH": None,
        "H": "hours",
        "T": "minutes",
        "min": "minutes",
        "S": "seconds",
        "L": None,
        "ms": None,
        "U": "microseconds",
        "US": "microseconds",
        "N": None,
    }

    if offset not in offsets or offsets[offset] is None:
        raise ValueError(f"Unknown offset: {offset}")

    return offsets[offset]


@dataclass
class Weekdays:
    """Weekdays mapping for easy acess."""

    monday = relativedelta.MO
    tuesday = relativedelta.TU
    wednesday = relativedelta.WE
    thursday = relativedelta.TH
    friday = relativedelta.FR
    saturday = relativedelta.SA
    sunday = relativedelta.SU
