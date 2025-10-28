# application/jobs_dataframe.py
import pandas as pd
from application.services_providers.jsearch import fetch_jobs


def devops_jobs_dataframe(keyword: str = "devops", limit: int = 50) -> pd.DataFrame:
    hits = fetch_jobs(keyword, limit)
    rows = [{
        "Title": h.get("headline"),
        "Employer": h.get("employer", {}).get("name"),
        "City": h.get("workplace_address", {}).get("municipality"),
        "Published": h.get("publication_date"),
        "Employment": h.get("employment_type", {}).get("label"),
        "Duration": h.get("duration", {}).get("label"),
        "Experience Required": h.get("experience_required"),
        "Apply URL": h.get("webpage_url"),
    } for h in hits]
    return pd.DataFrame(rows)
