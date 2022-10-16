import requests,json,pytest,allure
URL = "http://liyou.api.sauou.com/"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("店铺点击在线聊天")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_store_build_online_chat():
    """店铺点击建立在线聊天"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "store_id":"1" #店铺id
    }
    url = URL + "/h5/user.Chat/distribute"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("获取消息用户列表")
@allure.severity(allure.severity_level.NORMAL)
def test_2_get_message_user_list():
    """获取消息用户列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1" #用户id
    }
    url = URL + "/h5/user.Chat/getUserLine"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("移除消息列表")
@allure.severity(allure.severity_level.NORMAL)
def test_3_delete_message_list():
    """移除消息列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"1" #消息列表id
    }
    url = URL + "/h5/user.Chat/chatRemove"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("获取指定用户连天记录")
@allure.severity(allure.severity_level.MINOR)
def test_4_get_user_chat_list():
    """获取用户聊天记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"2", #用户uid
        "get_uid":"1", #获取对应用户uid
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.Chat/getRecordList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("保存发送消息")
@allure.severity(allure.severity_level.NORMAL)
def test_5_save_send_message():
    """保存发送消息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"2", #发送者uid
        "picture":"1", #图片
        "id":"1", #接收者id
        "text":"", #内容
        "chat_id":"3" #聊天主表主键id
    }
    url = URL + "/h5/user.Chat/chatSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("标记消息已读")
@allure.severity(allure.severity_level.NORMAL)
def test_6_mark_message_red():
    """标记消息已读"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "send_uid":"2", #发送消息的人
        "get_uid":"1" #接受消息的人
    }
    url = URL + "/h5/user.Chat/setRead"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("聊天室模块测试用例")
@allure.description("悬赏任务服务商点击聊天")
@allure.severity(allure.severity_level.CRITICAL)
def test_7_reward_service_build_online_chat():
    """悬赏任务服务商点击聊天"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"2", #用户id
        "service_uid":"1" #服务商id
    }
    url = URL + "/h5/user.Chat/distribute"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()





