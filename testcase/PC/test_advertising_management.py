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
@allure.feature("总后台")
@allure.story("广告管理模块测试用例")
@allure.description("广告新增/修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_advertising():
    """广告新增/修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "id": "1", #修改必传
        "title": "广告929", #广告标题
        "sort": "1", #排序
        "type": "1", #1.用户端 2.服务商端
        "path": "https://img.daidaipets.com/20220905/1662366245425.png", #图片地址
    }
    url = URL + "/admin/Banner/doSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("广告管理模块测试用例")
@allure.description("广告列表")
@allure.severity(allure.severity_level.NORMAL)
def test_1_advertising_list():
    """广告列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "admin_id":1,
        "type": "1" #1.用户端 2.服务商端
    }
    url = URL + "/Banner/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("广告管理模块测试用例")
@allure.description("广告删除")
@allure.severity(allure.severity_level.NORMAL)
def test_1_delete_advertising():
    """广告删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "banner_id": "7"
    }
    url = URL + "/admin/Banner/del"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()