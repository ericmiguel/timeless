import pytest
import timeless


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1976), (0, 1975), (-1, 1974)],
)
def test_add_years(offset_value, expected_result):
    assert timeless.datetime(1975, 1, 1).add(years=offset_value).year == expected_result


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1), (0, 12), (-1, 11)],
)
def test_add_months(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 12, 1).add(months=offset_value).month == expected_result
    )


def test_add_month_with_overflow():
    assert timeless.datetime(2012, 1, 31).add(months=1).month == 2


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1), (0, 31), (-1, 30)],
)
def test_add_days(offset_value, expected_result):
    assert timeless.datetime(1975, 5, 31).add(days=offset_value).day == expected_result


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1), (0, 0), (-1, 23)],
)
def test_add_hours(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).add(hours=offset_value).hour == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1), (0, 0), (-1, 59)],
)
def test_add_minutes(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).add(minutes=offset_value).minute
        == expected_result
    )


@pytest.mark.parametrize(
    "offset_value, expected_result",
    [(1, 1), (0, 0), (-1, 59)],
)
def test_add_seconds(offset_value, expected_result):
    assert (
        timeless.datetime(1975, 5, 21).add(seconds=offset_value).second
        == expected_result
    )
