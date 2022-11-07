"""Datetime helper functions."""

seconds_in_minute = 60
seconds_in_hour = seconds_in_minute * 60
seconds_in_day = seconds_in_hour * 24

minutes_in_hour = 60
minutes_in_day = minutes_in_hour * 24

hours_in_day = 24


def seconds_to_minutes(seconds: int) -> float:
    """Seconds to minutes conversion."""
    return seconds / seconds_in_minute


def seconds_to_hours(seconds: int) -> float:
    """Seconds to hours conversion."""
    return seconds / seconds_in_hour


def seconds_to_days(seconds: int) -> float:
    """Seconds to days conversion."""
    return seconds / seconds_in_day


def minutes_to_seconds(minutes: int) -> float:
    """Minutes to seconds conversion."""
    return minutes * seconds_in_minute


def minutes_to_hours(minutes: int) -> float:
    """Minutes to hours conversion."""
    return minutes * minutes_in_hour


def minutes_to_days(minutes: int) -> float:
    """Minutes to days conversion."""
    return minutes * minutes_in_day


def hours_to_seconds(hours: int) -> float:
    """Hours to seconds conversion."""
    return hours * seconds_in_hour


def hours_to_minutes(hours: int) -> float:
    """Hours to minutes conversion."""
    return hours / minutes_in_hour


def hours_to_days(hours: int) -> float:
    """Hours to days conversion."""
    return hours / hours_in_day


def days_to_seconds(days: int) -> float:
    """Days to seconds conversion."""
    return days * seconds_in_day


def days_to_minutes(days: int) -> float:
    """Days to minutes conversion."""
    return days * minutes_in_day


def days_to_hours(days: int) -> float:
    """Days to hours conversion."""
    return days * hours_in_day
