import timeless


def test_seconds_to_minutes():
    assert timeless.seconds_to_minutes(60) == 1


def test_seconds_to_hours():
    assert timeless.seconds_to_hours(3600) == 1


def test_seconds_to_days():
    assert timeless.seconds_to_days(86400) == 1


def test_minutes_to_seconds():
    assert timeless.minutes_to_seconds(1) == 60


def test_minutes_to_hours():
    assert timeless.minutes_to_hours(60) == 1


def test_minutes_to_days():
    assert timeless.minutes_to_days(1440) == 1


def test_hours_to_seconds():
    assert timeless.hours_to_seconds(1) == 3600


def test_hours_to_minutes():
    assert timeless.hours_to_minutes(1) == 60


def test_hours_to_days():
    assert timeless.hours_to_days(24) == 1


def test_days_to_seconds():
    assert timeless.days_to_seconds(1) == 86400


def test_days_to_minutes():
    assert timeless.days_to_minutes(1) == 1440


def test_days_to_hours():
    assert timeless.days_to_hours(1) == 24
