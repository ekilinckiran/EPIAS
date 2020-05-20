from datetime import datetime, timezone, timedelta

def toEpoch(epiasTime):
    """Converts EPIAS time format to EPOCH seconds

    Arguments:
        strTime {str} -- Time with EPIa format of "2020-02-12T01:00" or
                                                  "2020-04-24T01:00:00.000+0300"

    Returns:
        int -- EPOCH seconds
    """
    if len(epiasTime)==16:
        t = datetime.strptime(epiasTime, f"%Y-%m-%dT%H:%M")
    elif len(epiasTime)==28:
        t = datetime.strptime(epiasTime, f"%Y-%m-%dT%H:%M:%S.%f%z")
    else:
        t = datetime.strptime("1970-01-01T00:00", f"%Y-%m-%dT%H:%M")
    return int(t.timestamp())


def toEpiasShort(epochTime):
    """Converts EPOCH seconds to EPIAS time format

    Arguments:
        epochTime {int} -- Time with EPOCH seconds

    Returns:
        str -- Time with EPIAS format ie: 2020-02-12T01:00
    """
    t = datetime.fromtimestamp(epochTime, tz=timezone(+timedelta(hours=3)))
    return t.isoformat("T", "minutes")[:-6]

def toEpiasLong(epochTime):
    """Converts EPOCH seconds to EPIAS time format

    Arguments:
        epochTime {int} -- EPOCH seconds

    Returns:
        str -- Time with Json Format 2020-01-01T00:00:00.000+0300
    """
    t = datetime.fromtimestamp(epochTime, tz=timezone(+timedelta(hours=3)))
    return t.isoformat("T", "milliseconds")