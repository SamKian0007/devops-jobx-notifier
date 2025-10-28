# application/jobs_dataframe.py
import pandas as pd
from application.services_providers.jsearch import fetch_jobs


def devops_jobs_dataframe(keyword: str = "devops", limit: int = 50) -> pd.DataFrame:
    hits = fetch_jobs(keyword, limit)
    rows = [{
        "Title": h.get("headline"),
        "Employer": (h.get("employer") or {}).get("name"),
        "Published": h.get("publication_date"),
        "Type": h.get("employment_type"),
        "Extent": h.get("extent"),
        "City": (h.get("workplace_address") or {}).get("municipality")
        or (h.get("workplace_address") or {}).get("city")
        or "Unknown",
    } for h in hits]
    return pd.DataFrame(rows)
