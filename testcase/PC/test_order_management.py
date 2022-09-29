import requests, json, pytest, allure
URL = "http://192.168.110.167:566"
"""@allure.severity装饰器按严重性级别来标记case　　　
执行指定测试用例 --allure-severities blocker
BLOCKER = 'blocker'　　阻塞缺陷(功能未实现，无法下一步)
CRITICAL = 'critical'　严重缺陷(功能点缺失)
NORMAL = 'normal'　　  一般缺陷(边界情况，格式错误)
MINOR = 'minor'　　    次要缺陷(界面错误与ui需求不符)
TRIVIAL = 'trivial'　　轻微缺陷(必须项无提示，或者提示不规范)　
标记用例等级：@allure.severity(allure.severity_level.TRIVIAL)"""
@allure.feature("总后台")
@allure.story("订单管理模块测试用例")
@allure.description("订单列表")
@allure.severity(allure.severity_level.NORMAL)
def test_1_order_list():
    """订单列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "real_name": "测试",  #名称
        # "user_phone": "17623400167",  # 电话
        # "order_sn": "2022071549511014",  # 订单号
        # "month": "2022-06-07",  # 月份2022-06-07
        # "status": "0",  #0:全部 1:待付款 2:待发货 3:待收货 4:待评价 5.已完成 6:已取消 8.已关闭
        "page": "1",
        "pagesize": "1"
    }
    url = URL + "/admin/order/getList"
    res = requests.post(url=url, headers=headers, json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
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
        "id": "1"
    }
    url = URL + "/admin/order/detail"
    res = requests.post(url=url, headers=headers, params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()