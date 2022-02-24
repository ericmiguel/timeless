import timeless


dt = timeless.datetime(1994, 2, 26, hour=11, minute=15, zone="America/Sao_Paulo")
dt.set_zero()
# Datetime(1994, 2, 26, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))

# or use the equivalent property:
dt.zero
