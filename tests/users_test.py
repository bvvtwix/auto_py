import requests
from config import API_URL
from src.enums.global_enums import GlobalErrorMessage
from src.base_classes.response import Response
from src.schemas.get_user import GET_USER_THRESHOLDS_SCHEMA
from auth import get_auth

def test_get_user_thresholds():

    user_id = "fd596611-59c5-4d50-bd88-b7afbdf314b7"

    body = f"""
    query GET_USER {{
        accounts {{
                getOne(id: "{user_id}") {{
                    __typename 
                    ... on Person {{
                        thresholds {{
                            temperature {{
                                min
                                max
                            }},
                            pulse {{
                                min
                                max
                            }}
                            pressureSystolic {{
                                min
                                max
                            }}
                            pressureDiastolic {{
                                min
                                max
                            }}
                            alcohol {{
                                min
                                max
                            }}
                        }}
                    }}
                }}
            }}
        }}
    """

    auth_token = get_auth()    
    request_headers = {'authorization': f'Bearer {auth_token}'}

    r = requests.post(url=API_URL, headers=request_headers, json={"query": body})
    response = Response(r)
    response.assert_status_code(200).validate(GET_USER_THRESHOLDS_SCHEMA)
    print(request_headers)
    print("response status code: ", response.response_status)
    print("response : ", response.response_json)


    # temperature_min = response.response_json['data']['accounts']['getOne']['thresholds']['temperature']['min']
    # temperature_max = response.response_json['data']['accounts']['getOne']['thresholds']['temperature']['max']