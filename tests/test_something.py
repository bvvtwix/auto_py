import requests
from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessage
from src.base_classes.response import Response
from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post

def test_get_posts_data():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    # response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_status_code(200).validate(Post)

    print(response.response_json)


