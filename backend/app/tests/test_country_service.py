from pydantic import ValidationError

from app.tests.test_main import client
from app.models.country_code import CountryCode
from app.models.country_data import CountryData, DataEntry
from app.exceptions.no_data_exception import NoDataException


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


def test_read_country_data_without_values():
    response = client.get("/country/AF/query/77818")
    assert response.status_code == 200
    country_data = response.json()

    assert isinstance(country_data, dict)


def test_read_country_data_filters():
    start_year, end_year = 2000, 2008
    base_url = "/country/BR/query/77818"

    def check_values_in_range(values, start_year=None, end_year=None):
        for i in values:
            year = int(i["year"])
            if start_year:
                assert year >= start_year
            if end_year:
                assert year <= end_year

    # start_year e end_year
    url = f"{base_url}?start_year={start_year}&end_year={end_year}"
    response = client.get(url)
    assert response.status_code == 200
    country_data = response.json()
    assert country_data["values"]
    check_values_in_range(country_data["values"], start_year, end_year)

    # soment start_year
    url = f"{base_url}?start_year={start_year}"
    response = client.get(url)
    assert response.status_code == 200
    country_data = response.json()
    assert country_data["values"]
    check_values_in_range(country_data["values"], start_year=start_year)

    # end_year
    url = f"{base_url}?end_year={end_year}"
    response = client.get(url)
    assert response.status_code == 200
    country_data = response.json()
    assert country_data["values"]
    check_values_in_range(country_data["values"], end_year=end_year)

    # start_year maior que end_year
    start_year, end_year = 2010, 2000
    url = f"{base_url}?start_year={start_year}&end_year={end_year}"
    response = client.get(url)
    country_data = response.json()
    assert response.status_code == 400

    assert country_data == {
        "message": "ERRO - 'start_year deve ser menor ou igual a end_year'"
    }
