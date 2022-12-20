"""Preprocessing and Transformation functions that need to be done on our results data"""

import datetime


def unix_timestamp_to_datetime(timestamp: float) -> datetime.datetime:
    """Convert a unix timestamp to a Date object.

    Args:
        timestamp: The unix timestamp. This is what pytest uses.

    Returns:
        The Date object representation of the timestamp. This makes it more usable in Python and MongoDB.

    Example:
    ```
        unix_time = 1671487835.169075
        date = transform.unix_timestamp_to_datetime(unix_time)
        assert date.year == 2022
    ```
    """
    return datetime.datetime.fromtimestamp(timestamp)
