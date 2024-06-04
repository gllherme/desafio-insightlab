from app.tests.test_main import client
from app.models.country_profile import CountryProfile


def test_read_country_profile():
    response = client.get("/country/profile/BR")
    assert response.status_code == 200
    profile = response.json()

    assert isinstance(profile, dict)

    assert CountryProfile(**profile)

    assert profile["languages"]
    assert profile["currencies"]

    for l in profile["languages"]:
        assert isinstance(l, str) and not None

    for c in profile["currencies"]:
        assert isinstance(c, str) and not None
