import requests,json,pytest,allure
URL = "http://192.168.110.167:566"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("小程序用户端")
@allure.story("店铺管理模块测试用例")
@allure.description("优惠券领取")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_get_coupon():
    """优惠券领取"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "coupon_id": "1", #优惠券id
        "store_id": "1", #店铺id
        "uid": "2"
    }
    url = URL + "/h5/user.coupon_user/doReceive"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("店铺管理模块测试用例")
@allure.description("店铺收藏")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_store_collect():
    """店铺收藏"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "store_id": "1",
        "status": "1" #0 取消收藏 1收藏
    }
    url = URL + "/h5/user.store_collect/doSave"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("店铺管理模块测试用例")
@allure.description("店铺详情")
@allure.severity(allure.severity_level.MINOR)
def test_3_store_detail():
    """店铺详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1",
        "uid": "1"
    }
    url = URL + "/h5/user.Store/storeDetail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("店铺管理模块测试用例")
@allure.description("店铺查找")
@allure.severity(allure.severity_level.NORMAL)
def test_4_store_find():
    """店铺查找"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "page": "1",
        "pagesize": "10",
        "keywords": ""
    }
    url = URL + "/h5/user.Store/getList"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()