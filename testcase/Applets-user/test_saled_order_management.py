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
@allure.story("售后订单管理模块测试用例")
@allure.description("退货退款同意后填写物流单号")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_fill_logistics_code():
    """退货退款同意后填写物流单号"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"22", #售后订单id
        "express":"SF20214612123", #物流单号
        "express_name":"顺丰快递" #快递公司名
    }
    url = URL + "/h5/user.order_return/logistics"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("售后订单管理模块测试用例")
@allure.description("售后申请")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_apply_after_sales():
    """售后申请"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "oid":"2",  #订单主键id
        "type":"2",  #1 仅退款 2.退货退款
        "remark":"申请退货退款",  #备注
        "refund_explain":"货物损坏", #售后原因
        "refund_img":"231556"  #退货凭据
    }
    url = URL + "/h5/user.order_return/apply"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("售后订单管理模块测试用例")
@allure.description("售后列表")
@allure.severity(allure.severity_level.NORMAL)
def test_3_after_sales_list():
    """售后列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1"  #用户id
    }
    url = URL + "/h5/user.order_return/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("售后订单管理模块测试用例")
@allure.description("售后详情")
@allure.severity(allure.severity_level.MINOR)
def test_4_after_sales_detail():
    """售后详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"22"  #售后订单id
    }
    url = URL + "/h5/user.order_return/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()






