import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install()) # global driver

def get_nonce():
    driver.get('https://reservierung.ub.fau.de/room/hb-og-2/#availability') # could be any floor
    driver.find_elements_by_class_name('seat-link')[0].click() # get to any seat page
    authenticate(driver)

    url = driver.current_url
    return url[url.index('nonce=') + 6: -1]


def authenticate(curr_driver: webdriver):
    driver = curr_driver
    id = sys.argv[1]
    pwd = sys.argv[2]

    driver.find_element_by_id('username').send_keys(id)
    driver.find_element_by_id('password').send_keys(pwd)

    driver.find_element_by_name('submit_ldap').click()