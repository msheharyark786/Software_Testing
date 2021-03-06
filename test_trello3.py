# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTrello3():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_trello3(self):
    # Test name: trello3
    # Step # | name | target | value | comment
    # 1 | open | /ranamoazam/boards |  | 
    self.driver.get("https://trello.com/ranamoazam/boards")
    # 2 | setWindowSize | 950x691 |  | 
    self.driver.set_window_size(950, 691)
    # 3 | mouseOver | css=.icon-add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".icon-add")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | click | css=.icon-add |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".icon-add").click()
    # 5 | mouseOut | css=.icon-add |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | click | id=1580122619338-create-team-org-display-name |  | 
    self.driver.find_element(By.ID, "1580122619338-create-team-org-display-name").click()
    # 7 | type | id=1580122619338-create-team-org-display-name | hamza_state | 
    self.driver.find_element(By.ID, "1580122619338-create-team-org-display-name").send_keys("hamza_state")
    # 8 | click | id=1580122619338-create-team-org-description |  | 
    self.driver.find_element(By.ID, "1580122619338-create-team-org-description").click()
    # 9 | type | id=1580122619338-create-team-org-description | hello | 
    self.driver.find_element(By.ID, "1580122619338-create-team-org-description").send_keys("hello")
    # 10 | click | css=.\_3UeOvlU6B5KUnS |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3UeOvlU6B5KUnS").click()
    # 11 | type | css=.autocomplete-input | moazam.rana@ucp.edu.pk | 
    self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-input").send_keys("moazam.rana@ucp.edu.pk")
    # 12 | mouseDown | css=.autocomplete-btn |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 13 | mouseUp | css=.multi-select-autocomplete-container |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".multi-select-autocomplete-container")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 14 | click | css=.autocomplete-btn |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-btn").click()
    # 15 | mouseOver | css=.autocomplete-btn |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".autocomplete-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 16 | mouseOut | css=.autocomplete-btn |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 17 | click | css=.\_24AWINHReYjNBf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_24AWINHReYjNBf").click()
    # 18 | click | css=li:nth-child(8) > .\_2jR0BZMM5cBReR |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(8) > .\\_2jR0BZMM5cBReR").click()
  
