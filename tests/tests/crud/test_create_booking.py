import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.postive
    @allure.title("Verify taht craete Booking status and booking ID shouldn't be null")
    @allure.description("Craete a booking from the payload and verify that booking id should not be null")

    def test_create_booking_positive(self):
       pass


