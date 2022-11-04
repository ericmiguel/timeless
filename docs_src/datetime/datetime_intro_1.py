import timeless


dt = timeless.datetime(1994, 2, 26)

dt.zone  # => 'UTC'
dt.tzinfo  # => zoneinfo.ZoneInfo(key='UTC')
