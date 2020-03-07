import datetime as dt


def datetime(querystring):
    if querystring is None:
        raise AttributeError('Not found week_start or week_end GET parameters!')

    querystring = querystring.split('-')
    if len(querystring) != 3:
        raise AttributeError('Invalid week_start or week_end. Please use YYYY-MM-DD format.')

    try:
        return dt.datetime(year=int(querystring[0]), month=int(querystring[1]), day=int(querystring[2]))
    except:
        raise AttributeError('Invalid week_start or week_end. Please use YYYY-MM-DD format.')


def test():
    assert datetime('2020-03-08') == dt.datetime(year=2020, month=3, day=8)
    assert datetime('2020-2-14') == dt.datetime(year=2020, month=2, day=14)

    threw = False
    try:
        datetime('2020-03-xx')
    except:
        threw = True
    assert threw


if __name__ == '__main__':
    test()
