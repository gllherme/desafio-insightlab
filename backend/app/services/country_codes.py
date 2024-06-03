import requests

import app.config
from app.models.country_code import CountryCode


def get_all_country_codes():
    req = requests.get(app.config.COUNTRY_PROFILE_BASE_URL + "TODOS").json()

    unfiltered = [{"code": country["id"]["ISO-3166-1-ALPHA-2"], "name": country["nome"]["abreviado"].split("(")[0].rstrip()}
                  for country in req]

    seen_codes = set()

    filtered = []
    for item in unfiltered:
        if item["code"] not in seen_codes:
            filtered.append(CountryCode(code=item["code"], name=item["name"]))
            seen_codes.add(item["code"])

    return filtered
