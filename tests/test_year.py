from .what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch
import urllib.request
import json
import io


def create_file_json_str(dict_obj):
    """Create file-like object to mock JSON response from API"""
    json_str = json.dumps(dict_obj)
    return io.StringIO(json_str)


date_v1 = create_file_json_str({"currentDateTime": "2077-10-27T11:28:16.641021+03:00"})
date_v2 = create_file_json_str({"currentDateTime": "27.10.2077 11:28:17"})
date_v3 = create_file_json_str({"currentDateTime": "27.10.2222 11:28:17"})
date_fail = create_file_json_str({"currentDateTime": "22-22-22 11:28:17"})


class YearTestCase(unittest.TestCase):
    def test_v1(self):
        with patch("urllib.request") as mocked_api:
            mocked_api.urlopen.return_value = date_v1
            assert what_is_year_now() == 2077

    def test_v2(self):
        with patch("urllib.request") as mocked_api:
            mocked_api.urlopen.return_value = date_v2
            assert what_is_year_now() == 2077


if __name__ == "__main__":
    API_URL = "http://worldtimeapi.org/api/ip"
    with patch("urllib.request") as mocked_api:
        mocked_api.urlopen.return_value = date_v1
        with urllib.request.urlopen(API_URL) as resp:
            print(resp, type(resp))
            resp_json = json.load(resp)
            print(resp_json, type(resp_json))
