import time

from SeleniumCode.wrappercode.base_file import *
from SeleniumCode.wrappercode.locator_data import *
from SeleniumCode.wrappercode.test_data import *

def provide_user_details(first_name, last_name):
    send_text(first_name_loc, first_name)
    send_text(last_name_loc, last_name)

def provide_src_dest(src, dest):
    send_text(fromcity, src)
    send_text(destinationCity, dest)

def male_female_details():
    click_element(male_locator)
    click_element(female_locator)

def provide_billing_details(name, phone, email):
    send_text(billing_name, name)
    send_text(billing_phone, phone)
    send_text(billing_email, email)


def test1_book_ticket(input_data):
    provide_user_details(input_data['first_name'], input_data['last_name'])
    provide_src_dest(input_data['fromcity'], input_data['destinationCity'])
    male_female_details()
    provide_billing_details(input_data['billing_name'], input_data['billing_phone'], input_data['billing_email'])


test1_book_ticket(test1)
time.sleep(10)
test1_book_ticket(test2)