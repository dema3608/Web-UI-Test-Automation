#contains fixtures
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope = 'session'): #called once
	#readfile
	with open('config.json') as config_file:
		config = json.load(config_file)

	#check values
	assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
	assert isinstance(config['implicit_wait'], int)
	assert config['implicit_wait'] > 0

	return config


@pytest.fixture
#generator gives sequence of elements 
def browser(config):
	# initializing webdriver
	if config['browser'] == 'Firefox': # fire fox has not been added yet, will fail
		b = selenium.webdriver.Firefox()
	elif config['browser'] == 'Chrome':
		b = selenium.webdriver.Chrome()
	elif config['browser'] == 'Headless Chrome':
		opts = selenium.webdriver.ChromeOptions()
		opts.add_argument('headless')
		b = selenium.webdriver.Chrome(options = opts)
	else:
		raise Exception(f'Browser "{config["browser"]}" is not supported')


	#wait 10 seconds for elements to appear after making calls
	b.implicitly_wait(config['implicit_wait'])

	#return webdriver instance for setup
	#before yeild executes in setup, after yeild executes in cleanup 
	yield b

	#quick webdriver instance fro cleanup
	b.quit()