import requests

import app.config
from app.models.country_data import CountryData, DataEntry
from app.exceptions.no_data_exception import NoDataException


def get_country_data_by_indicator(country_code: str, indicator_id: int) -> CountryData:
    r = requests.get(app.config.COUNTRY_URL + country_code +
                     "/indicadores/" + indicator_id).json()[0]

    id = r["id"]
    name = r["indicador"].split(" - ")[1]

    if not r["series"]:
        raise NoDataException(indicator_name=name)

    series = r["series"][0]["serie"]

    filtered_series = []
    for i in series:
        if any(value is not None for value in i.values()):
            filtered_series.append(
                DataEntry(
                    year=list(i.keys())[0],
                    value=list(i.values())[0]))

    return CountryData(
        indicator_id=id,
        indicator_name=name,
        values=filtered_series
    )
