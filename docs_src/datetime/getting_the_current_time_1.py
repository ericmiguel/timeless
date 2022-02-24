import timeless


today = timeless.today()

# it's possible to use the `zone` keyword argument to specify the timezone
now = timeless.now(zone="America/Sao_Paulo")
