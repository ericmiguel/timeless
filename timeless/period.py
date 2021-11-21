from typing import List
from typing import Optional

from timeless.datetime import Datetime


class Period:
    def __init__(
        self,
        start: Datetime,
        end: Optional[Datetime] = None,
        periods: Optional[int] = None,
        unit: str = "days",
    ):
        self.start = start
        self.end = end
        self.periods = periods
        self.unit = unit

    def range(self, unit: str = "days"):
        def create_period(start: Datetime, end: Datetime, unit: str):
            while start <= end:
                yield start
                start = start.add(**{unit: 1})

        if self.end:
            period = create_period(self.start, self.end, unit)
        elif not self.end and self.periods:
            self.end = self.start.add(**{unit: self.periods})
            period = create_period(self.start, self.end, unit)
        else:
            raise ValueError("Either 'end' or 'periods' must be provided.")

        return period

    def __iter__(self):
        return self.range(self.unit)

    def add(self, amount: int, unit: str = "days"):
        for dt in self.range():
            yield dt.add(**{unit: amount})

    def subtract(self, amount: int, unit: str = "days"):
        for dt in self.range():
            yield dt.subtract(**{unit: amount})

    def to_list(self) -> List["Datetime"]:
        return list(self)
