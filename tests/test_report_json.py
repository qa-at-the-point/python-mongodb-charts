from metrics.commands import report


def test_read_report_json():
    _report = report.read_report_json("tests/example.report.json")
    assert _report["duration"]
