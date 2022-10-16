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
@allure.story("公共模块测试用例")
@allure.description("启动页")
@allure.severity(allure.severity_level.MINOR)
def test_1_setup_page():
    """启动页"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    url = URL + "/h5/user.Index/index"
    res = requests.post(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("搜索历史记录")
@allure.severity(allure.severity_level.CRITICAL)
def test_2_search_story_record():
    """搜索历史纪录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1", #用户id
        "type":"1", #1.商品搜索 2.企查查搜索 3.店铺搜索
        "page":"1",
        "pagesize":"10" #每页展示数量
    }
    url = URL + "/h5/user.search_record/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("搜索记录删除")
@allure.severity(allure.severity_level.CRITICAL)
def test_3_search_record_delete():
    """搜索纪录删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "id": "1",  # 记录id
        "uid":"1", #用户id
        "type":"1", #1.商品搜索 2.企查查搜索 3.店铺搜索
    }
    url = URL + "/h5/user.search_record/del"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("物流公司信息")
@allure.severity(allure.severity_level.MINOR)
def test_4_logistics_company_message():
    """物流公司信息"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    url = URL + "/h5/user.common/express"
    res = requests.get(url=url, headers=headers).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200

if __name__ == '__main__':
    pytest.main()

























































