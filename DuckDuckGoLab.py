import requests
import pytest


url_ddg = "https://api.duckduckgo.com/?q="



def test_presidents_of_the_USA():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]