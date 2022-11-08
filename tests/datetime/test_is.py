import pytest
import timeless


@pytest.mark.parametrize(
    "year, leap",
    [(2024, True), (2023, False)],
)
def test_is_leap(year, leap):
    assert timeless.datetime(year, 1, 1).is_leap() == leap
