import tiez


def test_now():
    now = tiez.now("America/Sao_Paulo")
    in_paris = tiez.now("Europe/Paris")

    assert now.hour != in_paris.hour


def test_add():
    date = tiez.datetime(2021, 1, 1)
    date_plus_one = date.add(days=1)
    assert date_plus_one.day == 2


def test_subtract():
    date = tiez.datetime(2021, 1, 1)
    date_plus_one = date.subtract(days=1)
    assert date_plus_one.day == 31
