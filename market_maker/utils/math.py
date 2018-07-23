from decimal import Decimal
from datetime import timedelta

def toNearest(num, tickSize):
    """Given a number, round it to the nearest tick. Very useful for sussing float error
       out of numbers: e.g. toNearest(401.46, 0.01) -> 401.46, whereas processing is
       normally with floats would give you 401.46000000000004.
       Use this after adding/subtracting/multiplying numbers."""
    tickDec = Decimal(str(tickSize))
    return float((Decimal(round(num / tickSize, 0)) * tickDec))

def snap_time(t, aggro):
    snapped = t - timedelta(seconds=t.second, microseconds=t.microsecond)
    if aggro is '1m':
        # already rounded to the nearest 1m in the past since all aggros need this
        pass
    elif aggro is '5m':
        snapped = snapped - timedelta(minutes=(t.minute % 5))
    elif aggro is '1h':
        snapped = snapped - timedelta(minutes=t.minute)
    elif aggro is '1d':
        snapped = snapped - timedelta(hours=t.hour, minutes=t.minute)
    else:
        raise Exception("AGGRO setting '%s' is invalid." % aggro)
    return snapped
