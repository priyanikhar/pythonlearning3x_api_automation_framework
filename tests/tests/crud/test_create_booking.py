import allure
import pytest

from source.helpers.api_requests_wrapper import post_request
from source.constants.api_constants import APIConstants
from source.helpers.payload_manager import payload_create_booking
from source.helpers.common_verifictaions import *
from source.utils.utils import Utils
class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify taht craete Booking status and booking ID shouldn't be null")
    @allure.description("Craete a booking from the payload and verify that booking id should not be null")

    def test_create_booking_positive(self):
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False

             )
        booking_id=response.json()["bookingid"]
        verify_http_status_code(response_data=response,expected_data=200)
        verify_Json_response_key_not_null("booking_id")




