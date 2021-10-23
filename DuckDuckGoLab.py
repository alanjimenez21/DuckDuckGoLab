import requests
import pytest


url_DuckDuckGo = "https://api.duckduckgo.com/?q="


def test_presidents_of_the_USA():
    resp = requests.get(url_DuckDuckGo + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()