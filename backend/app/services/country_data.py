import requests
from abc import ABC, abstractmethod

import app.config
from app.models.country_data import CountryData, DataEntry
from app.exceptions.no_data_exception import NoDataException

# Utilizando strategy pattern para o filtro de datas dos valores


class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, series: list):
        pass


class FilterFromStartYear(FilterStrategy):
    def __init__(self, start_year: int):
        self.start_year = start_year

    def filter(self, series: list):
        return [entry for entry in series if int(entry.year) >= self.start_year]


class FilterUntilEndYear(FilterStrategy):
    def __init__(self, end_year: int):
        self.end_year = end_year

    def filter(self, series: list):
        return [entry for entry in series if int(entry.year) <= self.end_year]


class FilterBetweenStartAndEndYears(FilterStrategy):
    def __init__(self, start_year: int, end_year: int):
        self.start_year = start_year
        self.end_year = end_year

    def filter(self, series: list):
        return [entry for entry in series
                if int(entry.year) >= self.start_year
                and int(entry.year) <= self.end_year]


class NoFilter(FilterStrategy):
    def filter(self, series: list):
        return series


class FilterContext:
    def __init__(self, strategy: FilterStrategy):
        self.strategy = strategy

    def apply_filter(self, series: list) -> list:
        return self.strategy.filter(series)


def fetch_country_data(country_code: str, indicator_id: int):
    url = f"{app.config.COUNTRY_URL}{country_code}/indicadores/{indicator_id}"
    req = requests.get(url)
    return req.json()[0]


def remove_nulls(series) -> list[DataEntry]:
    return [DataEntry(year=list(i.keys())[0], value=list(i.values())[0])
            for i in series
            if list(i.values())[0]]


def extract_series(data) -> tuple[int, str, dict]:
    id = data["id"]
    name = data["indicador"].split(" - ")[1]

    if not data["series"]:
        raise NoDataException(indicator_name=name)

    series = remove_nulls(data["series"][0]["serie"])

    return id, name, series


def get_country_data_by_indicator(country_code: str, indicator_id: int, start_year: int | None = None, end_year: int | None = None) -> CountryData:
    fetched_country_data = fetch_country_data(country_code, indicator_id)

    id, name, series = extract_series(fetched_country_data)

    if start_year and end_year:
        filter_strategy = FilterBetweenStartAndEndYears(start_year, end_year)
    elif start_year:
        filter_strategy = FilterFromStartYear(start_year)
    elif end_year:
        filter_strategy = FilterUntilEndYear(end_year)
    else:
        filter_strategy = NoFilter()

    context = FilterContext(filter_strategy)
    series = context.apply_filter(series)

    return CountryData(
        indicator_id=id,
        indicator_name=name,
        values=series
    )
