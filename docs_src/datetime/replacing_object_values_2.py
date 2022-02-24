import timeless


dt = timeless.datetime(1994, 2, 26, hour=11, minute=15, zone="America/Sao_Paulo")
dt.set(year=2100, zone="America/Sao_Paulo")
# Datetime(2100, 2, 26, 11, 15, tzinfo=zoneinfo.ZoneInfo(key='America/Sao_Paulo'))
