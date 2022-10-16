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
@allure.story("招投标信息管理模块测试用例")
@allure.description("招投标分类新增/修改")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_add_bid_type():
    """招投标分类新增/修改"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "id": "1", #修改必传
        "name": "招投标929", #投标分类名称
        "sort": "1", #排序
        "is_del_no": "1" #H5前端 0 可删除 1.不可删除
    }
    url = URL + "/admin/bidding_classify/doSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("招投标信息管理模块测试用例")
@allure.description("招投标分类列表")
@allure.severity(allure.severity_level.NORMAL)
def test_2_bid_type_list():
    """招投标分类列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "keywords": "热门推荐"
    }
    url = URL + "/admin/bidding_classify/doSave"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("招投标信息管理模块测试用例")
@allure.description("招投标分类删除")
@allure.severity(allure.severity_level.NORMAL)
def test_3_delete_bid_type():
    """招投标分类删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "8"
    }
    url = URL + "/admin/bidding_classify/del"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("招投标信息管理模块测试用例")
@allure.description("招投标信息列表")
@allure.severity(allure.severity_level.NORMAL)
def test_4_bid_message_list():
    """招投标信息列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        # "keywords": "热门推荐",
        "page": "1",
        "pagesize": "10"
    }
    url = URL + "/admin/bidding/getList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("总后台")
@allure.story("招投标信息管理模块测试用例")
@allure.description("招投标信息详情")
@allure.severity(allure.severity_level.MINOR)
def test_5_bid_message_detail():
    """招投标信息详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id": "1"
    }
    url = URL + "/admin/bidding/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()