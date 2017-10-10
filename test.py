import time
from selenium.webdriver.common.keys import Keys

MAIN_URL = 'localhost:8080'

# Utility functions
def wait():
  time.sleep(2)

def test_homepage(selenium):

  # Go to page and check title
  selenium.get(MAIN_URL)
  assert selenium.title == 'Check this title'

  # Check h1 tag
  h1 = selenium.find_element_by_tag_name('h1')
  assert h1.text == 'Learn pytest-selenium'

  # Get multiple elements by tag name
  elems = selenium.find_elements_by_tag_name('a')

  for e in elems:
    assert e.get_attribute('href') == 'http://localhost:8080/1.html'


def test_links(selenium):

  selenium.get(MAIN_URL)

  # Get single element by class
  link_with_class = selenium.find_element_by_class_name('linkclass')
  assert link_with_class.text == 'Link with class'

  # Get single element by ID
  link_with_id = selenium.find_element_by_id('linkid')
  assert link_with_id.text == 'Link with ID'

  wait()

  # Follow the link
  link_with_id.click()

  wait()

  assert selenium.title == 'Title of link page'

  # Check body
  body = selenium.find_element_by_css_selector('body')
  assert body.text == 'I am link 1'


def test_form(selenium):
  selenium.get(MAIN_URL)

  wait()

  text_input = selenium.find_element_by_name('coolie')
  text_input.send_keys('COOLIE')

  wait()

  text_input.send_keys(Keys.RETURN)

  wait()

  # test if our querystring was passed
  userinput = selenium.find_element_by_id('userinput')
  assert userinput.text == 'COOLIE'

  wait()
