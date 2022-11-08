import pytest
import timeless


try:  # Python <3.9
    from zoneinfo import ZoneInfo  # type: ignore
except ImportError:
    from backports.zoneinfo import ZoneInfo  # type: ignore


@pytest.mark.parametrize(
    "new_value, expected_value",
    [(1976, 1976), (1975, 1975), (1974, 1974)],
)
def test_set_year(new_value, expected_value):
    dt = timeless.datetime(1975, 1, 1)
    assert dt.set(year=new_value).year == expected_value


@pytest.mark.parametrize(
    "new_value, expected_value",
    [(2, 2), (1, 1), (12, 12)],
)
def test_set_month(new_value, expected_value):
    dt = timeless.datetime(1975, 1, 1)
    assert dt.set(month=new_value).month == expected_value


@pytest.mark.parametrize(
    "new_value, expected_value",
    [(1, 1), (26, 26), (28, 28)],
)
def test_set_day(new_value, expected_value):
    dt = timeless.datetime(1975, 1, 1)
    assert dt.set(day=new_value).day == expected_value


@pytest.mark.parametrize(
    "new_value, expected_value",
    [
        ("UTC", "UTC"),
        ("America/Sao_Paulo", "America/Sao_Paulo"),
        ("Europe/Vienna", "Europe/Vienna"),
    ],
)
def test_set_timezone(new_value, expected_value):
    dt = timeless.datetime(1975, 1, 1)
    assert dt.set(zone=new_value).tzinfo == ZoneInfo(expected_value)


def test_set_utc():
    dt = timeless.datetime(1975, 1, 1, 3)
    assert dt.set_utc().tzinfo == ZoneInfo("UTC")
    assert dt.set_utc().hour == dt.hour


def test_set_zero():
    dt = timeless.datetime(1975, 1, 1, 3, 1, 10, 1, zone="UTC")
    assert dt.set_zero().tzinfo == ZoneInfo("UTC")
    assert dt.set_zero().hour == 0
    assert dt.set_zero().minute == 0
    assert dt.set_zero().second == 0
    assert dt.set_zero().microsecond == 0
