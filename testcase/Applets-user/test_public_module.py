import requests,json,pytest,allure
URL = "http://192.168.110.167:566"
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("启动页")
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
def test_2_search_story_record(get_token_fixture):
    """搜索历史纪录"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        "Authorization": get_token_fixture
    }
    data = {
        "uid":"", #用户id
        "type":"", #1.商品搜索 2.企查查搜索 3.店铺搜索
        "page":"",
        "pagesize":"" #每页展示数量
    }
    url = URL + "/h5/user.search_record/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("搜索记录删除")
def test_3_search_record_delete():
    """搜索纪录删除"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "id": "",  # 记录id
        "uid":"", #用户id
        "type":"", #1.商品搜索 2.企查查搜索 3.店铺搜索
    }
    url = URL + "/h5/user.search_record/del"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("公共模块测试用例")
@allure.description("物流公司信息")
def test_3_logistics_company_message():
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

























































