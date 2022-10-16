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
@allure.feature("供应商后台")
@allure.story("资金管理模块测试用例")
@allure.description("店铺绑定uid的余额")
@allure.severity(allure.severity_level.NORMAL)
def test_1_store_uid_balance():
    """店铺绑定uid的余额"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1"  # 用户id
    }
    url = URL + "/Supplier/Supplier/userMoney"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("供应商后台")
@allure.story("资金管理模块测试用例")
@allure.description("提现记录")
@allure.severity(allure.severity_level.MINOR)
def test_2_withdrawal_record():
    """提现记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",  # 用户id
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/Supplier/Withdraw/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("供应商后台")
@allure.story("资金管理模块测试用例")
@allure.description("流水记录")
@allure.severity(allure.severity_level.MINOR)
def test_3_flow_record():
    """流水记录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",  # 用户id
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/Supplier/capital_flow/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("供应商后台")
@allure.story("资金管理模块测试用例")
@allure.description("提现申请")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_withdraw_apply():
    """提现申请"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",   #用户id
        "money": "10",   #提现金额
        "account_name": "测试",  #姓名
        "account": "17623400167"  #支付宝账号
    }
    url = URL + "/Supplier/Withdraw/apply"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


















if __name__ == '__main__':
    pytest.main()





