import json
import pytest
import requests
from config_2 import fetch_user_details_variables as fdapi
######################Valid_Case#######################################
def test_case_1_valid_request():
    case_1 = requests.get(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_1.status_code == 200,"Valid Request Failed"
######################Invalid_URL#####################################
def test_case_2_invalid_url():
    case_2 = requests.post(fdapi.invalid_url,headers=fdapi.valid_headers)
    assert case_2.status_code == 404, "API Request Failed on Invalid URL"
#######################API_Methods###################################
def test_case_3_post_method():
    case_3 = requests.post(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_3.status_code == 405, "API Request Failed on Post Method"
def test_case_4_put_method():
    case_4 = requests.put(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_4.status_code == 405,"API Request Failed on Put Method"
def test_case_5_patch_method():
    case_5 = requests.patch(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_5.status_code == 405, "API Request Failed on Patch Method"
def test_case_6_delete_method():
    case_6 = requests.delete(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_6.status_code == 405,"API Request Failed on Delete Method"
########################Invalid_User_ID##################################
def test_case_7_invalid_user_id():
    case_7 = requests.post(fdapi.valid_url,headers=fdapi.valid_headers)
    assert case_7.status_code == 404, "API Request Failed on Invalid User ID Search"
######################Invalid_Format#######################################
def test_case_8_invalid_format():
    case_8 = requests.get(fdapi.valid_url,headers=fdapi.invalid_headers)
    print(f"Response Message: {case_8.json().get('error')}")
    assert case_8.status_code == 406,"API Request Failed on Invalid Format"
######################XML_Format##########################################
def test_case_9_xml_format():
    case_9 = requests.post(fdapi.valid_url,headers=fdapi.invalid_xml_header)
    assert case_9.status_code == 406, "API Request Failed on XML Format"