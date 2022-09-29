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
@allure.feature("总后台")
@allure.story("商品管理模块测试用例")
@allure.description("商品分类新增/修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_commodity_type():
    """商品分类新增/修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "id":"1", #商品分类id（修改必传）
        "name":"商品分类929",
        "cover":"https://img.daidaipets.com/20220905/1662366245425.png",
        "sort":"1",
        "fid":"1"
    }
    url = URL + "/admin/product_classify/doSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("商品管理模块测试用例")
@allure.description("商品分类列表")
@allure.severity(allure.severity_level.MINOR)
def test_2_commodity_type_list():
    """商品分类列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "keywords":"屏风",
        "level":"2"
    }
    url = URL + "/admin/product_classify/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("商品管理模块测试用例")
@allure.description("商品分类删除")
@allure.severity(allure.severity_level.NORMAL)
def test_3_delete_commodity_type():
    """商品分类删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "id": "15"
    }
    url = URL + "/admin/product_classify/del"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("商品管理模块测试用例")
@allure.description("商品分类,新增获取上级分类")
@allure.severity(allure.severity_level.NORMAL)
def test_4_add_get_top_type():
    """商品分类,新增获取上级分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    url = URL + "/admin/product_classify/getClassTop"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200



if __name__ == '__main__':
    pytest.main()






