from mcp.server import tool
import requests

@tool
def search_subsidy(keyword: str):
    """
    補助金をキーワードで検索するツール
    """
    url = f"https://www.jgrants-portal.go.jp/api/proxy/subsidy/public?keyword={keyword}"
    res = requests.get(url)
    data = res.json()

    return [
        {
            "title": item.get("subsidyName"),
            "start": item.get("receptionStartDate"),
            "end": item.get("receptionEndDate"),
            "url": item.get("applyUrl")
        }
        for item in data.get("list", [])
    ]
