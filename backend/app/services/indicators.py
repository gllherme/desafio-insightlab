import requests

import app.config


def filter_groups(result):
    d = {}
    for item in result:
        group, s_name = item["indicador"].split(" - ")

        id = item["id"]
        name = s_name

        d.setdefault(group, []).append({"id": id, "name": name})

    return d


def get_all_indicators():
    r = requests.get(app.config.INDEXES_URL).json()

    return {"groups": filter_groups(r)}