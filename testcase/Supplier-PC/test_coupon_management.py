import requests, json, pytest, allure
++2;URL = "http://liyou.api.sauou.com/"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("总后台")
@allure.story("优惠券管理模块测试用例")
@allure.description("优惠券同意")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_agreement_coupon():
    """优惠券同意"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "coupon_id": "1"
    }
    url = URL + "/admin/coupon_issue/pass"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("优惠券管理模块测试用例")
@allure.description("优惠券拒绝")
@allure.severity(allure.severity_level.NORMAL)
def test_2_reject_coupon():
    """优惠券拒绝"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "coupon_id": "1"
    }
    url = URL + "/admin/coupon_issue/reject"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("优惠券管理模块测试用例")
@allure.description("优惠券列表")
@allure.severity(allure.severity_level.NORMAL)
def test_3_coupon_list():
    """优惠券列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "keywords": "测试店铺", #关键字
        # "month": "2022-06-07", #月份
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/admin/coupon_issue/getList"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()