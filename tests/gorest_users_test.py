from config import GOREST_USERS_URL
import requests

resp = requests.get(GOREST_USERS_URL)
print(resp.json())