import requests

import app.config
from app.models.country_code import CountryCode


def get_all_country_codes():
    r = requests.get(app.config.COUNTRY_PROFILE_BASE_URL + "TODOS").json()

    return [CountryCode(code=country["id"]["ISO-3166-1-ALPHA-2"],
                        name=country["nome"]["abreviado"].split("(")[0].rstrip())
            for country in r]
