import requests

BASE_URL = "https://jobsearch.api.jobtechdev.se/search"



def get_params_from_user_posts(user_posts: dict) -> dict:
    params: dict = {}

    # Keywords -> q
    keywords = (user_posts.get("keywords") or "").strip()
    if keywords:
        params["q"] = keywords

    # Location -> municipality (simple mapping; API also supports county/region in docs)
    location = (user_posts.get("location") or "").strip()
    if location:
        params["workplace_address"] = location

    # remote employment
    remote = (user_posts.get("remote") or "").strip()
    if remote == "Yes":
        params["remote"] = "true"
    elif remote == "No":
        params["remote"] = "false"

    # limit
    try:
        limit = int(user_posts.get("limit", 20))
    except (TypeError, ValueError):
        limit = 20
    # basic bounds
    if limit <= 0:
        limit = 20
    if limit > 100:
        limit = 100
    params["limit"] = limit

    # offset
    try:
        offset = int(user_posts.get("offset", 0))
    except (TypeError, ValueError):
        offset = 0
    if offset < 0:
        offset = 0
    params["offset"] = offset

    return params

def fetch_jobs_with_filters(params: dict):
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json().get("hits", [])
