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
@allure.story("企查查模块测试用例")
@allure.description("订阅添加")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_subscribe():
    """订阅添加"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "2",
        "classify_id": "4"
    }
    url = URL + "/h5/user.bidding/addSubscribe"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("订阅删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_delete_subscribe():
    """订阅删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "subscribe_id":"1" #订阅id主键
    }
    url = URL + "/h5/user.bidding/delSubscribe"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("我的订阅频道")
@allure.severity(allure.severity_level.NORMAL)
def test_3_my_subscribe_channel():
    """我的订阅频道"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "uid":"1" #用户id
    }
    url = URL + "/h5/user.bidding/subscribe"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("招投标任务分类")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_bid_task_type():
    """招投标任务分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    url = URL + "/h5/user.bidding/getClassify"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("招投标详情")
@allure.severity(allure.severity_level.MINOR)
def test_5_bid_detail():
    """招投标详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "id":"1" #投标id
    }
    url = URL + "/h5/user.bidding/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("招投标列表")
@allure.severity(allure.severity_level.MINOR)
def test_6_bid_list():
    """招投标列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "uid":"1", #用户id
        "classify_id":"1", #分类id
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.bidding/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("企查查模块测试用例")
@allure.description("企业信息查询")
@allure.severity(allure.severity_level.MINOR)
def test_7_query_company_message():
    """企业信息查询"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "keywords":"915000007935261598", #搜索关键字（企业名称）
        "uid":"1", #用户id
    }
    url = URL + "/h5/user.enterprise_inquiry/inquire"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()

























































