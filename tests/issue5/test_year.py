import io
import json
import unittest
from unittest.mock import patch

from ..what_is_year_now import what_is_year_now

JSONResponse = dict[str, str]
ResponseFile = io.StringIO
ExpYear = int
TestCase = tuple[ResponseFile, ExpYear]


def create_file_json_str(dict_obj: JSONResponse) -> io.StringIO:
    """Create file-like object to mock JSON response from API"""
    json_str = json.dumps(dict_obj)
    return io.StringIO(json_str)


dates: list[TestCase] = [
    (
        create_file_json_str(
            {
                "currentDateTime": "2077-10-27T11:28:16.641021+03:00",
                "currentdateTime": "5",  # должен игнорироваться
            }
        ),
        2077,
    ),
    (
        create_file_json_str(
            {
                "currentDateTime": "27.10.2077 11:28:17",
                "currentdatetime": "5",
            }
        ),
        2077,
    ),
    (
        create_file_json_str(
            {
                "currentDateTime": "2222-10-27T11:28:16.641021+03:00",
                "currentDatetime": "5",
            }
        ),
        2222,
    ),
    (
        create_file_json_str(
            {
                "currentDateTime": "27.10.2222 11:28:17",
                "Currentdatetime": "5",
            }
        ),
        2222,
    ),
]
date_fail = create_file_json_str({"currentDateTime": "22-22-22 11:28:17"})


class YearTestCase(unittest.TestCase):
    def what_is_year_patched(self, value: io.StringIO) -> int:
        """Return year from patched function with provided file-like object"""
        with patch("urllib.request") as mocked_api:
            mocked_api.urlopen.return_value = value
            return what_is_year_now()

    def test_dates(self):
        """Parsing year from function"""
        for api_date, exp_date in dates:
            with self.subTest(
                msg="testing correct parsing of year",
                api_date=api_date,
                exp_date=exp_date,
            ):
                self.assertEqual(self.what_is_year_patched(api_date), exp_date)

    def test_fail(self):
        "Invalid format raises exception"
        with self.assertRaisesRegex(ValueError, "Invalid format"):
            self.what_is_year_patched(date_fail)


if __name__ == "__main__":  # тестирование monkey patching
    API_URL = "http://__this_definitely_doesnt_work___worldtimeapi.org/api/ip"
    with patch("urllib.request") as mocked_api:
        mocked_api.urlopen.return_value = dates[0][0]
        print("current_year:", what_is_year_now())
