class fetch_user_details_variables:
    valid_url="http://localhost:5000/api/user_details/2009"
    invalid_url="http://localhost:5000/api/user_detailz/2009"
    invalid_user="http://localhost:5000/api/user_details/200929665"
    valid_headers={
        "Accept":"application/json"
    }
    invalid_headers={
        "Accept":"application/jsons"
    }
    invalid_xml_header={
        "Accept": "application/xml"
    }