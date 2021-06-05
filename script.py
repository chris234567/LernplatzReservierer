import sys
import re
from time import sleep

from utils import get_nonce, authenticate

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# login data

id = sys.argv[1]
pwd = sys.argv[2]

first_name = sys.argv[3]
last_name = sys.argv[4]
phone_number = sys.argv[5]

# room parameter 

seat_id = '394'
floor = 'hb-og-2'
date = '2021-06-06' # 2021-06-06  / YYY-MM-DD
time_slot = '1800' # 0800, 1400, 1800 / HHmm
nonce = get_nonce()

initial_url = 'https://reservierung.ub.fau.de/room/{0}/?room_id=385&seat_id=470&bookingdate={1}&timeslot={2}&nonce={3}'.format(floor, date, time_slot, nonce)

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(initial_url)

    # page 1 - authentication

    authenticate()

    # page 2 - booking

    new_url = re.sub(
        'bookingdate=\d{4}-\d{2}-\d{2}', 
        'bookingdate={}'.format(date), 
        driver.current_url
    )
    driver.get(new_url)

    sleep(.5)
    driver.find_element_by_id('rsvp_time_{}'.format(time_slot)).click()

    sleep(.5)
    driver.find_element_by_id('rsvp_seat_{}'.format(seat_id)).click()

    driver.find_element_by_name('rsvp_firstname').send_keys(last_name)
    driver.find_element_by_name('rsvp_lastname').send_keys(first_name)
    driver.find_element_by_name('rsvp_phone').send_keys(phone_number)

    sleep(.5) # alternativ wait.until() .. 
    driver.find_element_by_xpath("//input[@type='checkbox']").click()

    sleep(.5)
    driver.find_elements_by_xpath("//*[contains(text(), 'Buchung absenden')]")[0].click()

    sys.stdout.write('Buchung war erfolgreich. Email wird versandt.')  
    pass
except:
    sys.stdout.write('Raum ist zu gegebenem Datum und Timeslot nicht verfuegbar.')


# TODO: mabe call parameter in externem file speichern (zugangsdaten)
#       mabe outlook kalender events implementieren fuer bessere planung
#       mabe heroku scheduler

# AA:  006.A, 007.A, 008.A, 009.A, 010.A, 011.A
# EG:  001 A, 001 C, 002 A, 002 B, 002 C, 003 A, 003 B, 003 C, 004 A, 004 B, 004 C, 005 B, 005 C
# OG1: 109 A, 110 C, 111 A, 112 C, 113 A, 114 C, 115 A, 116 C, 117 A, 117 D, 117 H, 119 A, 119 D, 119 F, 120 B, 120 E, 120 H, 121 A, 121 B, 121 C, 121 D, 201 A, 202 C, 203 A, 204 C, 205 A, 206 C, 207 A, 207 G, 208 C, 208 E, 209 A, 209 G, 210 C, 210 E, 211 A, 211 E, 212 C, 212 G, 213 A, 213 E, 214 C, 214 G, 215 A, 215 D
# CIP: 216 C, 217 A ,218 C, 219 A, 220 C
# OG2: 301 C, 302 A, 303 C, 304 A, 304 E, 305 A, 305 D, 305 G, 305 J, 306 A, 307 A, 308 A, 311 A, 312 A, 313 A, 314 A, 315 A, 318 A, 320 A, 321 C, 322 A, 323 A, 324 C, 325 A, 326 F, 327 A, 327 D, 327 H, 328 A, 328 B, 328 C, 328 D, 401 A, 402 C, 403 A, 404 C, 405 A, 406 C, 407 A, 409 A, 409 D, 409 G, 410 A, 410 D, 410 G, 412 A, 413 A, 414 C, 414 G, 415 E, 416 A, 416 D, 416 G, 501 C, 501 G, 502 A, 503 C, 503 F, 504 A, 505 C, 506 A, 507 C, 508 A, 509 C, 510 F, 511 F, 602 A, 604 A, 606 A, 607 C, 608 A, 608 G, 609 C, 609 F, 610 C, 610 E, 610 G, 701 A, 702 A,703 A

# floors:
# hb-og-2
# hauptbibliothek-1-obergeschoss-cip-pool
# hb-og1
# hb-eg-1
# hb-eg-arbeitsabteile