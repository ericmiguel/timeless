import pytest
import timeless


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1974), (0, 1975), (-1, 1976)],
)
def test_subtract_years(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 1, 1).subtract(years=offset_value).year
        == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 11), (0, 12), (-1, 1)],
)
def test_subtract_months(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 12, 1).subtract(months=offset_value).month
        == expected_result
    )


def test_subtract_month_with_overflow():
    assert timeless.datetime(2012, 1, 31).subtract(months=2).month == 11


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 30), (0, 31), (-1, 1)],
)
def test_subtract_days(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 31).subtract(days=offset_value).day
        == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 23), (0, 0), (-1, 1)],
)
def test_subtract_hours(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).subtract(hours=offset_value).hour
        == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 59), (0, 0), (-1, 1)],
)
def test_subtract_minutes(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).subtract(minutes=offset_value).minute
        == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 59), (0, 0), (-1, 1)],
)
def test_subtract_seconds(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).subtract(seconds=offset_value).second
        == expected_result
    )
