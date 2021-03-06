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

class TestTrello4():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_trello4(self):
    # Test name: trello4
    # Step # | name | target | value | comment
    # 1 | open | /login |  | 
    self.driver.get("https://trello.com/login")
    # 2 | setWindowSize | 950x691 |  | 
    self.driver.set_window_size(950, 691)
    # 3 | click | id=user |  | 
    self.driver.find_element(By.ID, "user").click()
    # 4 | type | id=user | moazam.rana@ucp.edu.pk | 
    self.driver.find_element(By.ID, "user").send_keys("moazam.rana@ucp.edu.pk")
    # 5 | click | id=password |  | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | type | id=password | return0; | 
    self.driver.find_element(By.ID, "password").send_keys("return0;")
    # 7 | click | id=login |  | 
    self.driver.find_element(By.ID, "login").click()
    # 8 | mouseOver | css=.boards-page-board-section:nth-child(1) .board-tile-details |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".boards-page-board-section:nth-child(1) .board-tile-details")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | css=.boards-page-board-section:nth-child(1) .boards-page-board-section-list-item:nth-child(1) .board-tile-details |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 10 | click | css=.\_27QKbGhxDkdNHq > .\_1T7jXM3PAP_MoF > .pgEbaAFZBA0N5R:nth-child(3) .\_3qwe2tMMFonNvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_27QKbGhxDkdNHq > .\\_1T7jXM3PAP_MoF > .pgEbaAFZBA0N5R:nth-child(3) .\\_3qwe2tMMFonNvf").click()
    # 11 | click | css=.\_27QKbGhxDkdNHq > .\_1T7jXM3PAP_MoF > .pgEbaAFZBA0N5R:nth-child(3) .\_3qwe2tMMFonNvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_27QKbGhxDkdNHq > .\\_1T7jXM3PAP_MoF > .pgEbaAFZBA0N5R:nth-child(3) .\\_3qwe2tMMFonNvf").click()
    # 12 | mouseDownAt | id=content | 1365,119 | 
    element = self.driver.find_element(By.ID, "content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 13 | mouseMoveAt | id=content | 1365,119 | 
    element = self.driver.find_element(By.ID, "content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | mouseUpAt | id=content | 1365,119 | 
    element = self.driver.find_element(By.ID, "content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 15 | click | css=.js-react-root > .pgEbaAFZBA0N5R .\_3qwe2tMMFonNvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-react-root > .pgEbaAFZBA0N5R .\\_3qwe2tMMFonNvf").click()
    # 16 | click | css=.\_32YjsxnLz_UuuS |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_32YjsxnLz_UuuS").click()
    # 17 | mouseOver | css=.pgEbaAFZBA0N5R:nth-child(1) > .IAUH08xqIilxIq > .\_3qwe2tMMFonNvf |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".pgEbaAFZBA0N5R:nth-child(1) > .IAUH08xqIilxIq > .\\_3qwe2tMMFonNvf")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 18 | mouseOut | css=.pgEbaAFZBA0N5R:nth-child(1) > .IAUH08xqIilxIq > .\_3qwe2tMMFonNvf |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 19 | click | css=.\_1T7jXM3PAP_MoF:nth-child(1) > .pgEbaAFZBA0N5R:nth-child(1) .\_3qwe2tMMFonNvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1T7jXM3PAP_MoF:nth-child(1) > .pgEbaAFZBA0N5R:nth-child(1) .\\_3qwe2tMMFonNvf").click()
    # 20 | click | css=.home-sticky-container |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".home-sticky-container").click()
    # 21 | click | css=.pgEbaAFZBA0N5R:nth-child(5) .\_3qwe2tMMFonNvf |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".pgEbaAFZBA0N5R:nth-child(5) .\\_3qwe2tMMFonNvf").click()
    # 22 | click | css=.\_3r1LXvjBp8zfAv |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3r1LXvjBp8zfAv").click()
    # 23 | mouseOver | css=li:nth-child(1) .\_2DBw9GxD3tha0R |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .\\_2DBw9GxD3tha0R")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 24 | mouseOut | css=li:nth-child(1) .\_2DBw9GxD3tha0R |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 25 | click | css=.\_3r1LXvjBp8zfAv |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3r1LXvjBp8zfAv").click()
    # 26 | mouseOver | css=.\_3r1LXvjBp8zfAv |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3r1LXvjBp8zfAv")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 27 | mouseOut | css=.\_3r1LXvjBp8zfAv |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 28 | mouseOver | css=li:nth-child(2) .\_2DBw9GxD3tha0R |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .\\_2DBw9GxD3tha0R")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 29 | mouseOut | css=li:nth-child(2) .\_2DBw9GxD3tha0R |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 30 | click | css=li:nth-child(3) .\_2DBw9GxD3tha0R |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) .\\_2DBw9GxD3tha0R").click()
    # 31 | mouseOver | css=.boards-page-board-section-list-item:nth-child(4) .board-tile-details-name > div |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".boards-page-board-section-list-item:nth-child(4) .board-tile-details-name > div")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 32 | mouseOut | css=.boards-page-board-section-list-item:nth-child(4) .board-tile-details-name > div |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 33 | click | id=1580122726054-create-team-org-display-name |  | 
    self.driver.find_element(By.ID, "1580122726054-create-team-org-display-name").click()
    # 34 | type | id=1580122726054-create-team-org-display-name | Hello World | 
    self.driver.find_element(By.ID, "1580122726054-create-team-org-display-name").send_keys("Hello World")
    # 35 | click | id=1580122726054-create-team-org-description |  | 
    self.driver.find_element(By.ID, "1580122726054-create-team-org-description").click()
    # 36 | type | id=1580122726054-create-team-org-description | hhdhiuaqdhwuaih | 
    self.driver.find_element(By.ID, "1580122726054-create-team-org-description").send_keys("hhdhiuaqdhwuaih")
    # 37 | click | css=.\_3UeOvlU6B5KUnS |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_3UeOvlU6B5KUnS").click()
    # 38 | mouseOver | css=.\_3UeOvlU6B5KUnS |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_3UeOvlU6B5KUnS")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 39 | mouseOut | css=.\_3UeOvlU6B5KUnS |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
