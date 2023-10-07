import requests
from config import API_URL
from src.enums.global_enums import GlobalErrorMessage
from src.base_classes.response import Response

def get_auth():
    
    body = """
        mutation (
            $input: LogInInput!
            ) {
            auth {
                logIn (input: $input) {
                ... on NeedToConfirm {
                    processToken {
                    value
                    expiresAt
                    }
                    type
                    delivery
                }
                
                ... on NeedToChooseAccount {
                    processToken {
                    value
                    expiresAt
                    }
                    options {
                    accountId
                    orgUnitName
                    personFullname
                    orgUnitLogo
                                accountType
                    }
                }
                
                ... on Token {
                    value
                    expiresAt
                }
                
                ... on TokenPair {
                    access {
                    value
                    expiresAt
                    }
                    refresh {
                    value
                    expiresAt
                    }
                }
                }
            }
            }
    """

    vars = {
                "input": {
                    "clientType": "WEB",
                    "login": "email::juice@mail.ru",
                    "secret": "password::abc456"
                }
            }

    r = requests.post(url=API_URL, json={"query": body, "variables": vars})
    response = Response(r)

    auth_token = response.response_json['data']['auth']['logIn']['access']['value']

    return auth_token