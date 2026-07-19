import json
from pathlib import Path

REPORT = Path("/app/report.json")

def load_report():
    """Load the report."""
    assert REPORT.exists(), "no report.json found"
    return json.loads(REPORT.read_text())

def test_report_is_valid_json():
    """Success criteria 1: /app/report.json exists and contains a single valid JSON object."""
    report = load_report()
    assert isinstance(report, dict)

def test_total_requests():
    """Success criteria 2: total_requests equals the number of requests in the log."""
    assert load_report()["total_requests"] == 6

def test_unique_ips():
    """Success criteria 3: unique_ips equals the count of distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3

def test_top_path():
    """Success criteria 4: top_path equals the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"