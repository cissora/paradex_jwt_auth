
import requests
from jwt_helper import get_jwt_token

def get_authenticated_session():
    session = requests.Session()
    token = get_jwt_token()
    session.headers.update({ "Authorization": f"Bearer {token}" })
    return session

if __name__ == "__main__":
    session = get_authenticated_session()
    response = session.get("https://api.prod.paradex.trade/api/v1/account")
    print(f"\n✅ Response: {response.status_code}\n{response.text}\n")
