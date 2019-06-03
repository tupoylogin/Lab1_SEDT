from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from urllib.request import Request, urlopen
import os

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://rozetka.com.ua/')

driver.find_element_by_name('search').send_keys('Рубашка')
driver.find_element_by_css_selector('header > div > div.header-bottomline > div.header-search.js-app-search > form > button').click()

price_min = driver.find_element_by_xpath('//*[@id="price[min]"]')
price_min.send_keys(Keys.CONTROL + "a")
price_min.send_keys(Keys.DELETE)
price_min.send_keys('100')
price_max = driver.find_element_by_xpath('//*[@id="price[max]"]')
price_max.send_keys(Keys.CONTROL + "a")
price_max.send_keys(Keys.DELETE)
price_max.send_keys('2000')
driver.find_element_by_css_selector('#sort_price #submitprice').click()

driver.find_element_by_css_selector('#sort_producer > li:nth-child(3) > label > a').click()

driver.find_element_by_css_selector('#block_with_search > div > div.g-i-tile-l.clearfix > div:nth-child(1)').click()

driver.find_element_by_css_selector('rz-cart-button > rz-cart-button-simple > div > div > form > span > span > button').click()

driver.find_element_by_css_selector('.toOrder button[type=submit]').click()

driver.find_element_by_css_selector('button.btn-link-green').click()

driver.find_element_by_css_selector('#reciever_name').send_keys('Лионель Месси')
driver.find_element_by_css_selector('#reciever_phone').send_keys('+380671234567')
driver.find_element_by_css_selector('#reciever_email').send_keys('messi@mailforspam.com')

driver.find_element_by_css_selector('button#next_step').click()

driver.find_element_by_css_selector('#orders div.check-method-subl-i-inner > div.check-method-subl-select > div.inline.pos-fix.pickups-select-wrap > a').click()

driver.find_element_by_css_selector('#orders > div > div > div:nth-child(2) > div:nth-child(1) > div.check-f-i-field-indent > div > div > ul > li:nth-child(2) > div.check-method-subl-i-inner > div.check-method-subl-select > div.inline.pos-fix.pickups-select-wrap > a').click()

driver.find_element_by_css_selector('#orders > div > div > div:nth-child(2) > div:nth-child(1) > div.check-f-i-field-indent > div > div > ul > li:nth-child(2) > div.check-method-subl-i-inner > div.check-method-subl-select > div.inline.pos-fix.pickups-select-wrap > div > div.pickups-select-dropdown-wrap > div > ul > li:nth-child(27)').click()

driver.find_element_by_xpath('//*[@id="orders"]/div/div/div[4]/div/div[8]/div/div[2]/input').send_keys('Лионель')
driver.find_element_by_xpath('//*[@id="orders"]/div/div/div[4]/div/div[9]/div/div[2]/input').send_keys('Месси')

button = driver.find_element_by_css_selector('button#make-order')

if button.is_enabled():
	driver.close()