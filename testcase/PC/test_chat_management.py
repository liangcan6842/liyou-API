import requests, json, pytest, allure

URL = "http://liyou.api.sauou.com/"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("总后台")
@allure.story("聊天管理模块测试用例")
@allure.description("聊天列表")
@allure.severity(allure.severity_level.NORMAL)
def test_1_chat_list():
    """聊天列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "keywords": "热门推荐",
        # "moth": "2022-06-07",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/admin/Chat/getUserList"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("聊天管理模块测试用例")
@allure.description("聊天记录")
@allure.severity(allure.severity_level.NORMAL)
def test_2_chat_record():
    """聊天记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "keywords": "热门推荐",
        "chat_id": "3",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/admin/Chat/getChatRecord"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()