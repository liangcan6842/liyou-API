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
@allure.story("购物车模块测试用例")
@allure.description("加入购物车")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_shopping_cart():
    """加入购物车"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1",
        "store_id": "1",
        "product_attr_id": "2",
        "cart_num": "1"
    }
    url = URL + "/h5/user.store_cart/add"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("购物车模块测试用例")
@allure.description("购物车列表")
@allure.severity(allure.severity_level.MINOR)
def test_2_shopping_cart_list():
    """购物车列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid": "1"
    }
    url = URL + "/h5/user.store_cart/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("购物车模块测试用例")
@allure.description("购物车修改商品数量")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_alter_shopping_commodity_number():
    """购物车修改商品数量"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "19",
        "cart_num": "2"
    }
    url = URL + "/h5/user.store_cart/setCartNum"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("购物车模块测试用例")
@allure.description("指定删除购物车商品")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_delete_shopping_cart_commodity():
    """指定删除购物车商品"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "ids": [
            1, 2
        ]
    }
    url = URL + "/h5/user.store_cart/del"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()