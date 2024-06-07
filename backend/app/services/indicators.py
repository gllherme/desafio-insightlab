import requests

import app.config


def filter_categories(result):
    categories = set({item["indicador"].split(" - ")[0] for item in result})

    filtered = [{"category": category, "values": []}
                for category in categories]

    return filtered


def organize_values(result):
    filtered = filter_categories(result)

    for i in result:
        category, name = i["indicador"].split(" - ")

        for c in filtered:
            if c["category"] == category:
                c["values"].append({"id": i["id"], "name": name})

    return filtered


def get_all_indicators():
    try:
        r = requests.get(app.config.INDEXES_URL).json()
    except:
        raise Exception()

    return organize_values(r)
