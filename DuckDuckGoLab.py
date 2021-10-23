"""
*Name: Alan Ivan Jimenez Gallardo
*Instructor: Phillip Enkema
*Assignment: Lab - US Presidents
*Due: 10/24/2021

*The presidents should be listed in the RelatedTopics returned field.
RelatedTopics is a list, and you should check the Text entries of RelatedTopics to search for presidents.
We’ll only look for the last name of a president.  That means that we won’t distinguish between John Adams and his son,
John Quincy Adams, or George Bush the senior and ‘W.’
"""

import requests
import pytest


url_DuckDuckGo = "https://api.duckduckgo.com/?q="

#Iterate
@pytest.mark.parametrize("usa_presidents",
                         ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Van Buren",
                          "Harrison", "Tyler", "Polk", "Taylor", "Filmore", "Pierce", "Buchanan", "Lincoln", "Filmore", "Grant",
                          "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson",
                          "Harding", "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
                          "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"])

#Define the Test Function
def test_presidents_of_the_USA(usa_presidents):
    resp = requests.get(url_DuckDuckGo + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']
    for i in range(len(related_topics)):
        assert usa_presidents in related_topics