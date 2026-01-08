from dashboard import get_google_url_location
from dashboard import status_color
import csv
import os
from dashboard import create_csv

def test_google_url():
    assert get_google_url_location("https://maps.app.goo.gl/UbevtGYfunmqQRfX9") == (6.808071, 79.907361)
    assert get_google_url_location("https://maps.app.goo.gl/y6u5SkfASfTeXcYY6") == (6.924389, 80.037204)
    assert get_google_url_location("https://maps.app.goo.gl/cRkz79gmvaqQESS77") == (6.7757621, 80.2298994)

def test_color_marker():
    assert status_color("Red") == [255, 0, 0]
    assert status_color("Yellow") == [255, 200, 0]
    assert status_color("Green") == [0, 180, 0]

def test_create_csv(monkeypatch, tmp_path):
    test_csv = tmp_path / "locations.csv"

    monkeypatch.setattr("project.CSV_FILE", str(test_csv))
    create_csv()
    assert test_csv.exists()
