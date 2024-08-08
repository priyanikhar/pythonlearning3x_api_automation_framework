#Create Token
#Create Booking ID
#Update the booking (Put)-BookingID,Token
#Delete the Booking

#Verify that carete booking id when weupdate we asre able to update it and delete it
import allure
import pytest

from source.helpers.api_requests_wrapper import post_request
from source.constants.api_constants import APIConstants
from source.helpers.payload_manager import payload_create_booking
from source.helpers.common_verifictaions import *
from source.utils.utils import Utils
class TestCRUDBooking(object):
    @pytest.mark.positive
    @allure.title("Verify taht craete Booking status and booking ID shouldn't be null")
    @allure.description("Craete a booking from the payload and verify that booking id should not be null")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False

        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expected_data=200)
        verify_Json_response_key_not_null("booking_id")

    @pytest.mark.Negative
    @allure.title("Verify that craete Booking status and booking ID shouldn't be generated with empty payload")
    @allure.description("Create booking from the empty payload and verify that booking id should not be generated")
    def test_create_token_booking_without_payload_Negative(self,):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False

        )

        verify_http_status_code(response_data=response, expected_data=500)




