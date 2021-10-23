import requests
import pytest


url_DuckDuckGo = "https://api.duckduckgo.com/?q="

@pytest.mark.parametrize()

def test_presidents_of_the_USA(usa_president):
    resp = requests.get(url_DuckDuckGo + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
