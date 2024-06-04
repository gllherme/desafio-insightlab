from pydantic import ValidationError

from app.tests.test_main import client
from app.models.country_code import CountryCode
from app.models.country_data import CountryData, DataEntry


def test_read_country_codes():
    response = client.get("/country/codes")
    assert response.status_code == 200
    countries = response.json()

    assert isinstance(countries, list)

    for c in countries:
        assert isinstance(c, dict)

        assert CountryCode(**c)


def test_read_country_data():
    response = client.get("/country/BR/query/77849")
    assert response.status_code == 200
    country_data = response.json()

    assert isinstance(country_data, dict)

    assert CountryData(**country_data)

    assert country_data["values"]

    for c in country_data["values"]:
        assert DataEntry(**c)
