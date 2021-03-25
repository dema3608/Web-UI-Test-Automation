import pytest

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


@pytest.mark.parametrize('phrase', ['Sanke', 'hopescotch', 'baloon', 'Wolf', 'brown bear'])
def test_basic_search(browser, phrase):
	search_page = DuckDuckGoSearchPage(browser)
	result_page = DuckDuckGoResultPage(browser)

	#load page
	search_page.load()

	#enter search phrase
	search_page.search(phrase)

	#make sure phrase in results page results
	assert phrase == result_page.search_input_values()

	#make sure phrase is in result links
	titles = result_page.result_link_titles()
	matches = [t for t in titles if phrase.lower() in t.lower()]
	#make suer there is at least one match
	assert len(matches) > 0

	#make sure phrase is in results page title
	assert phrase in result_page.title()
	#checking tittle last avoids race condition. as implicit wait applys to web elements but not attributes (such as title)

	#raise Exception("Incomplete test")


#will always pass
def test_the_tests(browser):
	assert True