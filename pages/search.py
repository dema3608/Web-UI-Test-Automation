#pg obj for search page
#in order to be able to idetify pag elements
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage():
	#url
	URL = 'https://www.duckduckgo.com'

	#class level attribute to access search bar (locator)
	SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

	#initializer 

	def __init__(self, browser):
		self.browser = browser

	#loads taget url
	def load(self):
		self.browser.get(self.URL)

	#does web element interaction to search
	def search(self, phrase):
		#returns obj for found element on pg (* argument expansion B|c passing a tuple instead of two params)
		search_input = self.browser.find_element(*self.SEARCH_INPUT)
		#searches phrase
		search_input.send_keys(phrase + Keys.RETURN) #simulates enter key