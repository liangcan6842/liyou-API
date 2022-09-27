import pytest,requests,json,allure
URL = "http://192.168.110.173:8885"

@pytest.fixture(scope="session")
def get_token_fixture():
    '''
    作用域为session的fixture函数，返回token
    :return:
    '''
    headers = {"Content-Type": "application/json;charset=utf8"}
    data = {
        "code": "omejC5QxHUjb8DydrjzWEWiZOwno"  # 微信授权code
    }
    url = URL + "/h5/user.we_chat_auth/index"
    res = requests.get(url=url, headers=headers, params=data).text
    res = json.loads(res)
    token = res["data"]["token"]
    return token
