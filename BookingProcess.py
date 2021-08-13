import time
from locators import Locators as Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BookingProcess:

    def __init__(self, driver):

        self.driver = driver
        self.tripType = Locators.trip_type_xpath
        self.destinationClk = Locators.destination_click_xpath
        self.airport = Locators.airport_xpath
        self.tripDate = Locators.calander_day_xpath
        self.adult = Locators.adult_counter_xpath
        self.child = Locators.child_counter_xpath
        self.search = Locators.search_btn_xpath
        self.flight = Locators.flight_xpath
        self.fare = Locators.fare_xpath
        self.nologin = Locators.no_login_btn_xpath
        self.p1titleClk = Locators.passenger1_title_icon_xpath
        self.p1title = Locators.passenger1_drop_xpath
        self.p1fname = Locators.passenger1_fname_xpath
        self.p1lname = Locators.passenger1_lname_xpath
        self.p2titleClk = Locators.passenger2_title_icon_xpath
        self.p2title = Locators.passenger2_drop_xpath
        self.p2fname = Locators.passenger2_fname_xpath
        self.p2lname = Locators.passenger2_lname_xpath
        self.p3fname = Locators.passenger3_fname_xpath
        self.p3lname = Locators.passenger3_lname_xpath
        self.cotinue1 = Locators.continue1_btn_xpath
        self.seat_ok = Locators.family_seating_btn_xpath
        self.seat1 = Locators.seat1_btn_xpath
        self.seat2 = Locators.seat2_btn_xpath
        self.seat2 = Locators.seat2_btn_xpath
        self.seat3 = Locators.seat3_btn_xpath
        self.seat_continue = Locators.continue2_btn_xpath
        self.random_seat_continue = Locators.continue3_btn_xpath
        self.fast_track = Locators.fast_track_xpath
        self.small_bag = Locators.small_bag_xpath
        self.bag_continue = Locators.continue4_btn_xpath
        self.deals_continue = Locators.continue5_btn_xpath
        self.transport_continue = Locators.continue6_btn_xpath
        self.cart = Locators.cart_xpath
        self.checkOut = Locators.checkout_xpath
        self.mobile = Locators.mobile_number_xpath
        self.insurance = Locators.insurance_xpath
        self.cardNum = Locators.card_number_xpath
        self.cardName = Locators.cardholder_name_xpath
        self.cvv = Locators.security_code_xpath
        self.exmonthClk = Locators.expiry_month_drop_xpath
        self.exmonth = Locators.expiry_month_xpath
        self.exyearClk = Locators.expiry_year_drop_xpath
        self.exyear = Locators.expiry_year_xpath
        self.address = Locators.address_line_xpath
        self.city = Locators.city_xpath
        self.country = Locators.country_xpath
        self.postalcode = Locators.postalcode_xpath
        self.confirm = Locators.confirm_xpath
        self.pay = Locators.pay_now_xpath

    def trip_type_selection(self):
        self.driver.find_element_by_xpath(self.tripType).click()

    def select_trip_details(self):
        elem = self.driver.find_element_by_xpath(self.destinationClk)
        elem.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.airport).click()
        self.driver.find_element_by_xpath(self.tripDate).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.adult).click()
        self.driver.find_element_by_xpath(self.child).click()

    def click_search(self):
        self.driver.find_element_by_xpath(self.search).click()

    def flight_selection(self):
        self.driver.find_element_by_xpath(self.flight).click()

    def fare_selection(self):
        self.driver.find_element_by_xpath(self.fare).click()

    def passenger1_details(self, fname, lname):

        self.driver.find_element_by_xpath(self.nologin).click()
        element = self.driver.find_element_by_xpath(self.p1titleClk)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

        self.driver.find_element_by_xpath(self.p1title).click()
        self.driver.find_element_by_xpath(self.p1fname).send_keys(fname)
        self.driver.find_element_by_xpath(self.p1lname).send_keys(lname)

    def passenger2_details(self, fname, lname):

        element = self.driver.find_element_by_xpath(self.p2titleClk)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

        self.driver.find_element_by_xpath(self.p2title).click()
        self.driver.find_element_by_xpath(self.p2fname).send_keys(fname)
        self.driver.find_element_by_xpath(self.p2lname).send_keys(lname)

    def passenger3_details(self, fname, lname):

        element = self.driver.find_element_by_xpath(self.p3fname)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.send_keys(fname)
        self.driver.find_element_by_xpath(self.p3lname).send_keys(lname)
        self.driver.find_element_by_xpath(self.cotinue1).click()

    def seat_selection(self):

        self.driver.find_element_by_xpath(self.seat_ok).click()
        time.sleep(1)
        element = self.driver.find_element_by_xpath(self.seat1)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        element.click()
        self.driver.find_element_by_xpath(self.seat2).click()
        self.driver.find_element_by_xpath(self.seat3).click()
        self.driver.find_element_by_xpath(self.seat_continue).click()
        # self.driver.find_element_by_xpath(self.random_seat_continue).click()

    def flight_features_selection(self):

        self.driver.find_element_by_xpath(self.fast_track).click()
        self.driver.find_element_by_xpath(self.small_bag).click()
        time.sleep(1)
        element = self.driver.find_element_by_xpath(self.bag_continue)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath(self.deals_continue)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath(self.transport_continue)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.cart).click()
        self.driver.find_element_by_xpath(self.checkOut).click()

    def check_out(self, mobile, cardNum, cardName, cvv):

        self.driver.find_element_by_xpath(self.mobile).send_keys(mobile)
        self.driver.find_element_by_xpath(self.insurance).click()
        time.sleep(2)
        element = self.driver.find_element_by_xpath(self.pay)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element_by_xpath(self.cardNum)
        element.clear()
        element.send_keys(cardNum)

        element = self.driver.find_element_by_xpath(self.cardName)
        element.clear()
        element.send_keys(cardName)

        element = self.driver.find_element_by_xpath(self.cvv)
        element.clear()
        element.send_keys(cvv)

        self.driver.find_element_by_xpath(self.exmonthClk).click()
        self.driver.find_element_by_xpath(self.exmonth).click()
        self.driver.find_element_by_xpath(self.exyearClk).click()
        self.driver.find_element_by_xpath(self.exyear).click()

    def bill_info(self, address, city, country, postalcode):

        element = self.driver.find_element_by_xpath(self.address)
        element.clear()
        element.send_keys(address)

        element = self.driver.find_element_by_xpath(self.city)
        element.clear()
        element.send_keys(city)

        self.driver.find_element_by_xpath(self.country).send_keys(country)
        self.driver.find_element_by_xpath(self.country).send_keys(Keys.ENTER)
        time.sleep(1)

        element = self.driver.find_element_by_xpath(self.postalcode)
        element.clear()
        element.send_keys(postalcode)

    def final_step(self):
        self.driver.find_element_by_xpath(self.confirm).click()
        self.driver.find_element_by_xpath(self.pay).click()
