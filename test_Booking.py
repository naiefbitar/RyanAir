from logging import log
import time
import unittest
import LoginAction
import BookingProcess

from Base import ryan


class TestBooking(ryan, unittest.TestCase):

    def setUp(self):
        ryan.set_up(self)

    def test_Booking_F(self):
        driver = self.driver
        login = LoginAction.LoginAction(driver)
        login.agree_btn()

        time.sleep(2)
        booking = BookingProcess.BookingProcess(driver)

        booking.trip_type_selection()
        time.sleep(2)
        booking.select_trip_details()
        booking.click_search()
        time.sleep(2)

        booking.flight_selection()
        booking.fare_selection()

        booking.passenger1_details("naief", "Bitar")
        booking.passenger2_details("bitar", "naief")
        booking.passenger3_details("naief j", "bitar")

        time.sleep(2)
        booking.seat_selection()
        time.sleep(2)
        booking.flight_features_selection()
        time.sleep(2)
        login.enter_email("fadi-ta@outlook.com")
        login.enter_password("Password1")
        login.click_login()
        time.sleep(1)
        booking.check_out("702857662", "5555 5555 5555 5557",
                          "test test", "265")
        time.sleep(1)
        booking.bill_info("harsfa", "Budapest", "Hungary", "1053")
        time.sleep(1)
        booking.final_step()
        time.sleep(10)

        # try:
        #     assert "Welcome Page" == driver.title
        # except Exception as e:
        #     raise
        #     print("Title is wrong", format(e))


if __name__ == '__main__':
    unittest.main()
