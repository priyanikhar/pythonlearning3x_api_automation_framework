import openpyxl
import allure
import pytest
from source.helpers.api_requests_wrapper import post_request
from source.constants.api_constants import APIConstants
from source.helpers.payload_manager import payload_create_token
from.source.helpers.payload_manager import payload_create_booking
from source.helpers.common_verifictaions import *
from source.utils.utils import Utils


@pytest.fixture(scope="session")
def create_token():

    response =post_request(
        url=APIConstants.url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False

    )
    verify_http_status_code(response_data=response,expected_data=200)
@pytest.fixture(scope="session")
def get_booking_id():
    response=post_request(
        url=APIConstants.url_create_booking(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False

    )
    verify_http_status_code(response_data=response,expected_data=200)


