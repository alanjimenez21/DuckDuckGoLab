import requests
import pytest


url_DuckDuckGo = "https://api.duckduckgo.com/?q="

@pytest.mark.parametrize("usapresidents", ["Washington", "Adams", "Jefferson", "Madison",
                                            "Monroe", "Quincy Adams", "Jackson", "Van Buren",
                                            "Harrison", "Tyler", "Polk", "Taylor", "Filmore",
                                            "Pierce", "Buchanan", "Lincoln", "Filmore", "Grant",
                                            "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison",
                                            "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson",
                                            "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman",
                                            "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
                                            "Reagan", "H. W. Bush", "Clinton", "W. Bush", "Obama",
                                            "Trump", "Biden"])

def test_presidents_of_the_USA(usapresidents):
    resp = requests.get(url_DuckDuckGo + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']
    for i in range(len(related_topics)):
        assert usapresidents in related_topics