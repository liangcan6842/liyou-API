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
@allure.story("订单管理模块测试用例")
@allure.description("订单评价")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_order_evaluate():
    """订单评价"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "oid":"2", #订单id
        "comment":"测试评论928", #评论
        "product_score":"7", #评分
        "pics":""
    }
    url = URL + "/h5/user.product_reply/appraise"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("订单管理模块测试用例")
@allure.description("订单详情")
@allure.severity(allure.severity_level.MINOR)
def test_2_order_detail():
    """订单详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"1"
    }
    url = URL + "/h5/user.order/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("订单管理模块测试用例")
@allure.description("我的订单")
@allure.severity(allure.severity_level.NORMAL)
def test_3_search_record_delete():
    """我的订单"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "uid": "1",  # 用户id
        "status":"0", #筛选状态 0.全部 1.待付款 2.待发货 3.待收货 4.待评价
        "page": "1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.order/getOrderList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()






