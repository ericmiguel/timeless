"""Datetime helper functions."""

seconds_per_minute = 60
seconds_per_hour = seconds_per_minute * 60
seconds_per_day = seconds_per_hour * 24

minutes_per_hour = 60
minutes_per_day = minutes_per_hour * 24

hours_per_day = 24


def seconds_to_minutes(seconds: int) -> float:
    """Seconds to minutes conversion."""
    return seconds / seconds_per_minute


def seconds_to_hours(seconds: int) -> float:
    """Seconds to hours conversion."""
    return seconds / seconds_per_hour


def seconds_to_days(seconds: int) -> float:
    """Seconds to days conversion."""
    return seconds / seconds_per_day


def minutes_to_seconds(minutes: int) -> float:
    """Minutes to seconds conversion."""
    return minutes * seconds_per_minute


def minutes_to_hours(minutes: int) -> float:
    """Minutes to hours conversion."""
    return minutes * minutes_per_hour


def minutes_to_days(minutes: int) -> float:
    """Minutes to days conversion."""
    return minutes * minutes_per_day


def hours_to_seconds(hours: int) -> float:
    """Hours to seconds conversion."""
    return hours * seconds_per_hour


def hours_to_minutes(hours: int) -> float:
    """Hours to minutes conversion."""
    return hours / minutes_per_hour


def hours_to_days(hours: int) -> float:
    """Hours to days conversion."""
    return hours / hours_per_day


def days_to_seconds(days: int) -> float:
    """Days to seconds conversion."""
    return days * seconds_per_day


def days_to_minutes(days: int) -> float:
    """Days to minutes conversion."""
    return days * minutes_per_day


def days_to_hours(days: int) -> float:
    """Days to hours conversion."""
    return days * hours_per_day


DAYS_PER_MONTHS = {
    0: {  # non-leap years
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    },
    1: {  # leap years
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    },
}
