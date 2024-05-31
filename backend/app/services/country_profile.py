import requests
import locale

import app.config
from app.models.country_profile import CountryProfile

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def get_country_profile(country_code):
    r = requests.get(app.config.COUNTRY_PROFILE_BASE_URL + country_code).json()

    languages = list(set(language["nome"] for item in
                         r for language in item["linguas"]))

    currencies = list(set(currency["nome"] for item in r
                          for currency in item["unidades-monetarias"]))

    area = r[0]["area"]["total"]

    profile = CountryProfile(
        code=r[0]["id"]["ISO-3166-1-ALPHA-2"],
        name=r[0]["nome"]["abreviado"],
        area=locale.atof(area),
        region=r[0]["localizacao"]["regiao"]["nome"],
        languages=languages,
        currencies=currencies
    )

    return profile.model_dump()
