import requests

import app.config
from app.models.country_profile import CountryProfile
from app.utils.string_to_float import string_to_float


def fetch_profile_data(country_code):
    url = app.config.COUNTRY_PROFILE_BASE_URL + country_code
    req = requests.get(url)
    return req.json()


def extract_unique_non_null_lists(data, key):
    return list(set(sub_item["nome"] for item in data
                    for sub_item in item[key]
                    if sub_item["nome"] is not None))


def extract_profile_data(data):
    code = data[0]["id"]["ISO-3166-1-ALPHA-2"]
    name = data[0]["nome"]["abreviado"]
    area = string_to_float(data[0]["area"]["total"])
    region = data[0]["localizacao"]["regiao"]["nome"]
    return code, name, area, region


def get_country_profile(country_code: str):
    fetched_profile = fetch_profile_data(country_code)

    code, name, area, region = extract_profile_data(fetched_profile)

    languages = extract_unique_non_null_lists(fetched_profile, "linguas")
    currencies = extract_unique_non_null_lists(
        fetched_profile, "unidades-monetarias")

    profile = CountryProfile(
        code=code,
        name=name,
        area=area,
        region=region,
        languages=languages,
        currencies=currencies
    )

    return profile
