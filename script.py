import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# id = sys.argv[1] # ub_nummer
# pwd = sys.argv[2]

# pip -m install webdriver-manager!!

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://reservierung.ub.fau.de/room/hb-og-2/?room_id=385&seat_id=428&bookingdate=2021-05-31&timeslot=18%3A00&nonce=0c7ceaea42&require-auth=9a686e1893')

username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

print('hello')
print(username_field)
print(password_field)