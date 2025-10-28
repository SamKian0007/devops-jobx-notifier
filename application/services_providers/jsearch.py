# application/services/providers/jsearch.py
import requests

BASE_URL = "https://jobsearch.api.jobtechdev.se/search"


def fetch_jobs(keyword="devops", limit=50):
    params = {
        "q": keyword,
        "limit": limit,
        "offset": 0
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json().get("hits", [])


if __name__ == "__main__":
    jobs = fetch_jobs("devops", 1)
    if jobs:
        print("Available keys:\n")
        for key in jobs[0].keys():
            print("-", key)
