import pytest 
from application.services_providers.search_with_filters import get_params_from_user_posts 

def test_get_params_from_user_posts():
    params = get_params_from_user_posts({
        "keywords": "devops python",
        "location": "Stockholm",
        "remote": "true",
        "limit": "25",
        "offset": "5",
    })
    assert params["q"] == "devops python"
    assert params["municipality"] == "Stockholm"
    assert params["remote"] == "true"
    assert params["limit"] == 25
    assert params["offset"] == 5