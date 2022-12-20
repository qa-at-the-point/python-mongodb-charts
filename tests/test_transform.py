from metrics import transform


def test_transform_unix_time_to_date():
    unix_time = 1671487835.169075
    date = transform.unix_timestamp_to_datetime(unix_time)
    assert date.year == 2022
