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
@allure.story("商品管理模块测试用例")
@allure.description("商品评论")
@allure.severity(allure.severity_level.CRITICAL)
def test_1_commodity_comment():
    """商品评论"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "id":"1", #商品id
        "type":"2", #0.全部 1.有图 2.好评 3.差评
        "page":"1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.product_reply/getList"
    res = requests.post(url=url, headers=headers,json=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("商品管理模块测试用例")
@allure.description("商品详情")
@allure.severity(allure.severity_level.MINOR)
def test_2_commodity_detail():
    """商品详情"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
        # "Authorization": get_token_fixture
    }
    data = {
        "uid":"1",
        "id":"1"
    }
    url = URL + "/h5/user.Product/detail"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("商品管理模块测试用例")
@allure.description("获取二级分类")
@allure.severity(allure.severity_level.NORMAL)
def test_3_get_second_type():
    """获取二级分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "fid": "1",  # 上级id
        "page": "1",
        "pagesize":"10"
    }
    url = URL + "/h5/user.product_cate/getCateList"
    res = requests.post(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("商品管理模块测试用例")
@allure.description("首页分类跳转")
@allure.severity(allure.severity_level.NORMAL)
def test_4_first_page_type_skip():
    """首页分类跳转"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "classify_id": "1"  # 分类id
    }
    url = URL + "/h5/user.product_cate/getTopCate"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("商品管理模块测试用例")
@allure.description("搜索上、下级商品分类")
@allure.severity(allure.severity_level.NORMAL)
def test_5_up_down_level_commodity_type():
    """搜索上、下级商品分类"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "fid": "1"  # 上级分类 不传标识获取一级分类 传表示获取下级分类
    }
    url = URL + "/h5/user.Product/getProductClassify"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200
@allure.feature("小程序用户端")
@allure.story("商品管理模块测试用例")
@allure.description("获取商品列表")
@allure.severity(allure.severity_level.NORMAL)
def test_6_get_commodity_list():
    """获取商品列表"""
    # 通过Fixture函数获取get_token_fixture值，即token，再将token添加到请求头中
    headers = {
        "Content-Type": "application/json;charset=utf8",
    }
    data = {
        "page": "1",
        "pagesize": "1",
        # "keywords": "1", #搜索关键字
        # "classify_pid": "1", #分类上级id
        # "classify_id": "1", ##分类id
        # "sort": "1" #0. id 降序 1.销量 升序 2.销量 降序 3.价格 升序 4.价格 降序
    }
    url = URL + "/h5/user.Product/getList"
    res = requests.get(url=url, headers=headers,params=data).text
    res = json.loads(res)
    print(res)
    assert res["code"] == 200


if __name__ == '__main__':
    pytest.main()






