import timeless


start = timeless.datetime(1900, 1, 1)
end = start.add(years=1).subtract(months=1)
time_range = timeless.period(start, end)
