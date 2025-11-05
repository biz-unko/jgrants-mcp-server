import requests
from mcp.server import tool

@tool
def search_grants(keyword: str):
    """
    Search subsidy info from jGrants by keyword.
    """
    url = f"https://www.jgrants-portal.go.jp/api/proxy/subsidy/public?keyword={keyword}"
    res = requests.get(url)
    data = res.json()

    results = []
    for item in data.get("list", []):
        results.append({
            "title": item.get("subsidyName"),
            "start": item.get("receptionStartDate"),
            "end": item.get("receptionEndDate"),
            "url": item.get("applyUrl")
        })

    return results
