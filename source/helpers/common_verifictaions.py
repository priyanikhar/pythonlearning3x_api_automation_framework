# Common Verification
# Http Status
# Headers
# Data Verification
# JSON Schema
def verify_http_status_code(response_data,expected_data):
    assert response_data.status_code==expected_data,"FailedER!=AR"

def verify_response_key(key,expected_data):
    assert key==expected_data,"FailedER!=AR"


def verify_Json_response_key_not_null(key):
    assert key!=0,"Failed- Key is non empty" + key


def verif_response_delete(response):
    assert "created" in response

