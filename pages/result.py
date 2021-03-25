#pg obj for result page

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage():

	#locators

  	#to access search input on results page (ie the correct pohrase was sarched)
	RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
	#to access retult links
	SEARCH_INPUT = (By.ID, 'search_form_input')

	#initializer
	def __init__(self, browser):
		self.browser = browser

	#interaction(s)

	def result_link_titles(self):
		#finds all links and puts them in list
		links = self.browser.find_elements(*self.RESULT_LINKS)
		# get title scripts from elements in lists (map from elements to element titles)
		titles = [link.text for link in links]
		#return list of strings
		return titles

	def search_input_values(self):
		search_input = self.browser.find_element(*self.SEARCH_INPUT)
		#get attribute named value due to HTML weirdness
		val = search_input.get_attribute('value')
		return val

	def title(self):
		#attribute of pg instead of element 
		return self.browser.title